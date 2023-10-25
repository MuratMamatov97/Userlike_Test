class MessageCenterSettings:
    def __init__(self, page):
        self.page = page
        self.settings = page.get_by_role('link', name="Settings")
        self.website = page.get_by_text("Website", exact=True)
        self.channels = page.get_by_text("Channels", exact=True)
        self.widget_add_button = page.get_by_text("Add", exact=True)
        self.next_button = page.get_by_text("Next", exact=True)
        self.widget_action_menu = page.get_by_role('button', name="Open action menu")
        self.widget_delete_button = page.get_by_role('menuitem', name="Delete")
        self.delete_button = page.get_by_role('button', name="Delete")
        #self.cancel_button = page.get_by_role('reset', name="Cancel")

    def open_setting(self, setting):
        self.settings.click()
        if setting == "website":
            self.channels.click()
            self.website.click()

    def delete_widget(self):
        self.widget_action_menu.locator('nth=0').click()
        self.widget_delete_button.click()
        self.delete_button.click()

    def add_widget(self, setting):
        self.widget_add_button.click()
        if setting == "website":
            self.next_button.click()







