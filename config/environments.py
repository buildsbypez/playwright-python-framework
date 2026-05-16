environments = {
    "qa": {
        "base_url": "https://www.saucedemo.com",
        "username": "standard_user",
        "password": "secret_sauce"
    },
    "staging": {
        "base_url": "https://www.saucedemo.com",
        "username": "standard_user",
        "password": "secret_sauce"
    }
}

ACTIVE_ENV = "qa"

def get_env():
    return environments[ACTIVE_ENV]