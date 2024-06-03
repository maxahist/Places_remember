from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.gis.geos import Point
from django.contrib.gis.forms.fields import PointField
from django.urls import reverse
from django import forms
from allauth.socialaccount.providers.vk.provider import VKProvider
from allauth.socialaccount.models import SocialAccount, SocialApp

from ..models import Remember
from users.models import User


class TestRememberModel(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="auth", password="auth")
        cls.remember = Remember.objects.create(
            name="имя",
            description="описаник",
            location=Point(30.5, 30.555),
            author=cls.user,
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(
            username="tester", password="tester"
        )
        self.auth_client = Client()
        # self.auth_client.force_login(self.user)
        SocialAccount.objects.create(
            user=self.user, provider=VKProvider.id, uid="12345"
        )
        self.auth_client.force_login(self.user)
        Remember.objects.create(
            name="Место",
            description="Описание места",
            location=Point(60.56, 40.333),
            author=self.user,
        )

    def test_verbose_name(self):
        remember = TestRememberModel.remember
        remember_verbose = {
            "name": "Название",
            "description": "Описание",
            "location": "Локация",
            "author": "Автор",
        }

        for field, value in remember_verbose.items():
            with self.subTest(field=field):
                self.assertEqual(
                    remember._meta.get_field(field).verbose_name, value
                )

    def test_guest_access(self):
        path_list = (
            reverse("remembers:main"),
            reverse(
                "remembers:remember_edit",
                kwargs={"remember_id": Remember.objects.get(name="Место").id},
            ),
            reverse("remembers:remember_create"),
        )

        for path in path_list:
            with self.subTest(reverse_name=path):
                response = self.guest_client.get(path)
                self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_guest_redirect(self):
        path_list = (
            reverse("remembers:main"),
            reverse(
                "remembers:remember_edit",
                kwargs={"remember_id": Remember.objects.get(name="Место").id},
            ),
            reverse("remembers:remember_create"),
        )

        for path in path_list:
            with self.subTest(reversed_name=path):
                response = self.guest_client.get(path, follow=True)
                self.assertRedirects(
                    response, f'{reverse("users:login")}' f"?next={path}"
                )

    def test_remember_edit_and_create(self):
        path_list = (
            reverse("remembers:remember_create"),
            reverse(
                "remembers:remember_edit",
                kwargs={"remember_id": Remember.objects.get(name="Место").id},
            ),
        )
        for path in path_list:
            with self.subTest(reversed_name=path):
                response = self.auth_client.get(path)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_edit_post_context(self):
        response = self.auth_client.get(
            reverse(
                "remembers:remember_edit",
                kwargs={"remember_id": Remember.objects.get(name="Место").id},
            )
        )
        form_fields = {
            "name": forms.fields.CharField,
            "description": forms.fields.CharField,
            "location": PointField,
        }
        for value, form in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get("form").fields.get(value)
                self.assertIsInstance(form_field, form)

    def test_remember_appear(self):
        remember = Remember.objects.latest("created")
        response = self.auth_client.get(reverse("remembers:main"))
        self.assertEqual(response.context["remembers"][0].id, remember.id)
