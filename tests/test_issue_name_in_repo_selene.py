from selene import browser, have
from selene.support import by
from selene.support.shared.jquery_style import s


def test_issue_name():
    browser.open("https://github.com")

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s('#issues-tab').click()

    s('#issue_84_link').should(have.exact_text('Issue_created_to_test_allure_reports'))


