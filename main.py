from utils.console_helper import pause, clear_screen, required_input
from services.test_case_service import TestCaseService
from dialogs.test_case_dialog import TestCaseDialog


def main():
    
    test_case_service = TestCaseService(test_case_service)
    test_case_dialog = TestCaseDialog(test_case_dialog)

    clear_screen()

    print("#### Main menu - Test case registrator ####")
    print("1. Create test case")
    print("2. Show test cases")
    print("0. Exit")

    option: str = input("Choose an option")

    match option:
        case "1":
            test_case_dialog.create_test_case()

        case "2":
            test_case_dialog.show_test_case()

        case "0":
            return

        case _:
            print("Invalid option. Try again")
            pause()

if __name__ == "__main__":
    main()