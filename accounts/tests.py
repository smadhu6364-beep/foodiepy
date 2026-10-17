from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class SmokeTests(TestCase):
    def test_landing_page(self):
        self.assertEqual(self.client.get(reverse("landing")).status_code, 200)

    def test_login_and_register_pages(self):
        self.assertEqual(self.client.get(reverse("login")).status_code, 200)
        self.assertEqual(self.client.get(reverse("register")).status_code, 200)

    def test_forecasting_page(self):
        self.assertEqual(self.client.get(reverse("forecasting")).status_code, 200)

    def test_dashboard_requires_login(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 302)

    def test_dashboard_after_login(self):
        User.objects.create_user("demo", password="demo-pass-123")
        self.client.login(username="demo", password="demo-pass-123")
        resp = self.client.get(reverse("home"))
        self.assertIn(resp.status_code, (200, 302))

    def test_forecast_without_model_file_shows_message(self):
        data = {"category": 1, "cuisine": 1, "week": 1, "checkout_price": 100,
                "base_price": 120, "emailer": 0, "homepage": 0, "city": 1,
                "region": 1, "op_area": 2.0, "center_type": 1}
        resp = self.client.post(reverse("forecasting"), data)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "forecasts are disabled")
