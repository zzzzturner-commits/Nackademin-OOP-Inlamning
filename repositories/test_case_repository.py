from models.test_case import TestCase


class TestCaseRepository:
    cases : list[TestCase]

    def try_create_test_case(self, test_case: TestCase) -> None:
        self.cases.append(test_case)

    def get_test_cases(self) -> list[TestCase]:
        return self.cases.copy()

