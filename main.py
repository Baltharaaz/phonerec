from unittest import case

from pyswip import Prolog

import knowledge_base as kb
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def runtime():
    kb.kb_declare()
    while True:
        running = True
        choice = input("Welcome to the Phone Recommendation System! \n"
                       "Please select from the following options:\n"
                       "1. Get Phone by Classification\n"
                       "2. Exit\n")
        clear_screen()
        match choice:
            case "1":
                phone_type = input("Select a type of phone to receive suggestions: \n"
                                   "1. Good CPU\n"
                                   "2. Good RAM\n"
                                   "3. High End Phone\n"
                                   "4. Modern Phone\n"
                                   "5. \n"
                                   "6. \n"
                                   "7. \n"
                                   "8. \n"
                                   "9. \n"
                                   "10. \n")
                match phone_type:
                    case "1":
                        results = Prolog.query("good_cpu(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'])
                        for result in sorted_results:
                            print(result["X"] + '\n')
                            input("These phones are classified as having a good CPU due to their CPU being 1"
                                  "or faster\n"
                                  "Press Enter to return to Main Menu")
                        break
                    case "2":
                        break
                    case "3":
                        break
            case "2":
                running = False

        clear_screen()

        if not running:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kb.kb_declare()
