import random


class Inbox:
    def __init__(self, page):
        self.page = page
        self.inbox = page.get_by_role('link', name="Inbox")
        self.message_textbox = page.locator('xpath=//div[@aria-placeholder="Your message"]')
        self.answerID = random.randint(1, 1000)
        self.answer = f"Hi! This is example of answer number {self.answerID}"

    def open_inbox(self):
        self.inbox.click()

    def answer_to_customer(self, page, message):
        message.click()
        self.message_textbox.fill(self.answer)
        page.keyboard.press("Enter")








