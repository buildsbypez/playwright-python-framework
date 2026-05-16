import pytest
from base_test import BaseTest

class TestLogin(BaseTest):

    def test_valid_login(self, login_page):
        """Standard user can log in successfully"""
        login_page.login(self.username, self.password)
        assert login_page.is_logged_in(), "Expected to be logged in but inventory was not visible"

    def test_invalid_password(self, login_page):
        """Wrong password shows error message"""
        login_page.login(self.username, "wrongpassword")
        error = login_page.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_username(self, login_page):
        """Empty username shows error message"""
        login_page.login("", self.password)
        error = login_page.get_error_message()
        assert "Username is required" in error

    def test_locked_out_user(self, login_page):
        """Locked out user sees error message"""
        login_page.login("locked_out_user", self.password)
        error = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error
        