import pytest
from base_test import BaseTest
from pages.login_page import LoginPage
from pages.cart_page import CartPage

class TestCart(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_pages(self, page):
        self.login_page = LoginPage(page)
        self.cart_page = CartPage(page)
        
        # Log in before every cart test
        self.login_page.login(self.username, self.password)

    def test_add_item_to_cart(self):
        """Adding an item updates the cart badge to 1"""
        self.cart_page.add_item_to_cart()
        assert self.cart_page.get_cart_badge_count() == "1"

    def test_cart_badge_visible_after_add(self):
        """Cart badge appears after adding an item"""
        self.cart_page.add_item_to_cart()
        assert self.cart_page.is_cart_badge_visible()

    def test_navigate_to_cart(self):
        """Clicking cart icon takes you to cart page"""
        self.cart_page.add_item_to_cart()
        self.cart_page.go_to_cart()
        assert self.cart_page.get_cart_title() == "Your Cart"

    def test_item_appears_in_cart(self):
        """Added item appears in cart page"""
        self.cart_page.add_item_to_cart()
        self.cart_page.go_to_cart()
        assert self.cart_page.is_item_in_cart()

    def test_remove_item_from_cart(self):
        """Removing item from cart hides the badge"""
        self.cart_page.add_item_to_cart()
        self.cart_page.go_to_cart()
        self.cart_page.remove_item_from_cart()
        assert not self.cart_page.is_cart_badge_visible()