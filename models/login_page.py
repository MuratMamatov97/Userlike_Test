class LoginPage:
    def __init__(self, page):
        self.page = page
        self.button_to_login = page.locator('li.login > button')    # Unclear, to change
        self.username_textbox = page.locator("#login-username")
        self.password_textbox = page.locator("#login-password")
        self.submit_login = page.locator('#form-login > div:nth-child(4) > div > button')    # Unclear, to change

    def open_page(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.button_to_login.click()
        self.username_textbox.fill(username)
        self.password_textbox.fill(password)
        self.submit_login.click()


