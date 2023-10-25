from playwright.sync_api import expect, Playwright
from models.login_page import LoginPage
from models.MessageCenter.mc_page import MessageCenter
from models.MessageCenter.mc_settings_page import MessageCenterSettings
from models.customer_chat_page import CustomerChat
from models.MessageCenter.mc_inbox_page import Inbox
import pytest

widgetID = 0
agent_page = None


@pytest.fixture(scope="function", autouse=True)
def test_login(playwright: Playwright):
    browser = playwright.chromium.launch()
    agent_context = browser.new_context()
    global agent_page
    agent_page = agent_context.new_page()
    login_page = LoginPage(agent_page)
    login_page.open_page("https://www.userlike.com/")
    login_page.login("mamatovmurat0@gmail.com", "cgfcb,jVehfne1234Q")
    agent_page.screenshot(path="test1.png")
    expect(agent_page.locator('#subview-menu')).to_be_visible(timeout=4000)


@pytest.fixture(scope="function", autouse=True)
def test_open_message_center():
    message_center = MessageCenter(agent_page)
    agent_page.screenshot(path="test.png")
    message_center.open_message_center()
    expect(agent_page.get_by_role('button', name="Operator options")).to_be_visible(timeout=4000)


@pytest.fixture(name="create_website")
def test_create_website():
    settings = MessageCenterSettings(agent_page)
    settings.open_setting("website")
    settings.delete_widget()
    expect(settings.delete_button).not_to_be_visible(timeout=5000)
    settings.add_widget("website")
    expect(agent_page.get_by_text("Configure widget", exact=True)).to_be_visible(timeout=4000)
    global widgetID
    widgetID = agent_page.url.rsplit('/', 1)[-1]


@pytest.mark.usefixtures("create_website")
def test_chat(playwright: Playwright):
    browser = playwright.chromium.launch()
    customer_context = browser.new_context()
    customer_page = customer_context.new_page()
    login_page = LoginPage(customer_page)
    login_page.open_page("https://www.userlike.com/en/um/debug/" + str(widgetID))

    customer_chat = CustomerChat(customer_page)
    expect(customer_chat.button_to_chat).to_be_visible(timeout=10000)
    customer_chat.start_chat(customer_page)

    inbox = Inbox(agent_page)
    inbox.open_inbox()
    expect(agent_page.get_by_text(customer_chat.message)).to_be_visible()
    inbox.answer_to_customer(agent_page, agent_page.get_by_text(customer_chat.message))
    customer_page.wait_for_timeout(5000)
    customer_page.screenshot(path="test2.png")

    expect(customer_page.frame_locator('iframe[title="Messenger"]').locator("p").get_by_text(inbox.answer, exact=True).filter()).to_be_visible(timeout=10000)





