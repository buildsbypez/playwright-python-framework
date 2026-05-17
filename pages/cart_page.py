from playwright.sync_api import Page

class CartPage:
    
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.add_to_cart_button = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_icon = ".shopping_cart_link"
        self.cart_item = ".cart_item"
        self.remove_button = "[data-test='remove-sauce-labs-backpack']"
        self.cart_title = ".title"
        self.inventory_container = "#inventory_container"

    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button)
    
    def get_cart_badge_count(self):
        return self.page.inner_text(self.cart_badge)
    
    def go_to_cart(self):
        self.page.click(self.cart_icon)
    
    def is_item_in_cart(self):
        return self.page.is_visible(self.cart_item)
    
    def remove_item_from_cart(self):
        self.page.click(self.remove_button)
    
    def is_cart_badge_visible(self):
        return self.page.is_visible(self.cart_badge)
    
    def get_cart_title(self):
        return self.page.inner_text(self.cart_title)