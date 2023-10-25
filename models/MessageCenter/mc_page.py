class MessageCenter:
    def __init__(self, page):
        self.page = page
        self.message_center = page.get_by_text("Message Center", exact=True)

    def open_message_center(self):
        self.message_center.click()






