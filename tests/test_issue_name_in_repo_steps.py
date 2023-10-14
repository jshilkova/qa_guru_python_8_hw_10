import allure
from allure_commons.types import Severity
from selene import browser, have
from selene.support import by
from selene.support.shared.jquery_style import s


def test_issue_name_steps_dynamic():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Issues in the repository")
    allure.dynamic.story("Not authenticated user can see issues in the repository")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step("Open the GitHub main page"):
        browser.open("https://github.com")

    with allure.step("Search for the repo"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step("Open the repo by link"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Open the Issues tab"):
        s('#issues-tab').click()

    with allure.step("Check that issue #84 has name Issue_created_to_test_allure_reports"):
        s('#issue_84_link').should(have.exact_text('Issue_created_to_test_allure_reports'))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Issues in the repository")
@allure.story("Not authenticated user can see issues in the repository")
@allure.link("https://github.com", name="Testing")
def test_issue_name_decorator_steps():
    open_main_page()

    search_for_repo('eroshenkoam/allure-example')
    open_repo()
    open_issues_tab()

    check_issue_name("84", 'Issue_created_to_test_allure_reports')


@allure.step("Open the GitHub main page")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Search for repository {repo}")
def search_for_repo(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()


@allure.step("Open the repo by link")
def open_repo():
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step("Open the Issues tab")
def open_issues_tab():
    s('#issues-tab').click()


@allure.step("Check that issue {issue_number} has name {name}")
def check_issue_name(issue_number, name):
    s(f'#issue_{issue_number}_link').should(have.exact_text(name))