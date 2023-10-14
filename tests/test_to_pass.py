import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Issues in the repository")
@allure.story("Not authenticated user can see issues in the repository")
@allure.link("https://github.com", name="Testing")
def test_issue_name_decorator_steps():
    pass