import random


class CustomerChat:
    def __init__(self, page):
        self.page = page
        self.button_to_chat = page.frame_locator('iframe[title="Messenger button"]').get_by_role('button', name="Open")
        self.start_new_chat = page.frame_locator('iframe[title="Messenger"]').get_by_text("Start new conversation")
        self.chat_textbox = page.frame_locator('iframe[title="Messenger"]').get_by_placeholder("Your message")
        self.message_id = random.randint(0, 1000)
        self.message = f"Hi! This is the test message number {self.message_id}"

    def start_chat(self, page):
        self.button_to_chat.click()
        self.start_new_chat.click()
        self.chat_textbox.fill(self.message)
        page.keyboard.press("Enter")





