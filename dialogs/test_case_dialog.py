from utils.console_helper import clear_screen, pause, required_input
from models.test_case import TestCase
from services.test_case_service import TestCaseService


class TestCaseDialog:
    def __init__ (self, test_case_service: TestCaseService):
        self.test_case_service = test_case_service

    def create_test_case(self):

        while True:
            clear_screen()

            print("#### Create a test case - Test case registrator ####")
            print("1. Create a test case.")
            print("0. Back")
            print("")

            option = input("Choose an option: ").strip()

            if option == "0":
                return

            clear_screen()

            match option:
                case "1":
                    self.create_test_case()

                case _:
                    print("Invalid option. Please try again.")
                    pause()

            testcase = TestCase()
            testcase.title = required_input("Enter a title for the testcase, e.g. TC-001.")
            testcase.purpose = required_input("Enter the purpose of the test case, e.g The purpose is to test .... of the .... ")
            testcase.acceptance_criteria = required_input("Enter the acceptance criteria for the test case, e.g. Acceptance criteria ....")
            testcase.preconditions = required_input("Enter the preconditions for the test case, e.g. 1. Windows version, 2. Browser version 3. .... and so on.")
            testcase.test_data = required_input("Enter the test data for the test case, e.g. 1. .... , 2. .... and so on.")
            testcase.steps = required_input("Enter the steps to recreate the test case, e.g. 1. Do this .... 2. Do this .... and so on")
            testcase.expected_result = required_input("Enter the expected result for the test case, e.g. This is what we expect the end result will show")

            result = self.test_case_service.create_test_case(testcase)
            print(result.message)
            pause()

    def get_test_cases(self):

        while True:
            clear_screen()

            print("#### List management - Test case registrator ####")
            print("1. Show the list of registered test cases.")
            print("0. Back")
            print("")

            option = input("Choose an option: ").strip()

            if option == "0":
                return

            clear_screen()

            match option:
                case "1":
                    self.get_test_cases()

                case _:
                    print("Invalid option. Please try again.")

            result = self.test_case_service.get_test_cases(TestCase)
            print(result.message)
            pause()