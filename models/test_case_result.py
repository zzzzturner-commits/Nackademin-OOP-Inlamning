from models.test_case import TestCase

class TestCaseResult:
    def __init__(self, succeded: bool, message: str, testcase: TestCase):
        self.succeded: bool = succeded
        self.message: str = message
        self.testcase: TestCase = testcase