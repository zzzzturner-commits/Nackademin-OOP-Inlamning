from models.test_case import TestCase
from models.test_case_result import TestCaseResult

class TestCaseService:
    def __init__(self):
        self.testcase: list[TestCase] = []

    def create_test_case(self, testcase: TestCase) -> TestCaseResult:
        if not testcase.id:
            return TestCaseResult(False, "Test case id is required.", None)

        if not testcase.title:
            return TestCaseResult(False, "Title for the test case is required.", None)

        if not testcase.purpose:
            return TestCaseResult(False, "Purpose for the test case is required.", None)

        if not testcase.acceptance_critera:
            return TestCaseResult(False, "Acceptance criteria for the test case is required.", None)

        if not testcase.preconditions:
            return TestCaseResult(False, "Preconditions for the test case is required.", None)

        if not testcase.test_data:
            return TestCaseResult(False, "Test data for the test case is required.", None)

        if not testcase.steps:
            return TestCaseResult(False, "Steps for the test case is required.", None)

        if not testcase.expectedresult:
            return TestCaseResult(False, "Expected result for the test case is required.", None)

        self.testcase.append(testcase)
        return TestCaseResult(True, f"Test case with the title '{testcase.title}' has been added successfully", testcase)

    def get_test_cases(self) -> list[TestCase]:
        return self.testcase.copy()