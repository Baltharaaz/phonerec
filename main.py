from unittest import case

from pyswip import Prolog

import knowledge_base as kb
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def runtime():
    kb.kb_declare()
    running = True
    clear_screen()
    while running:
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
                                   "5. Old School\n"
                                   "6. Multimedia\n"
                                   "7. Large Screen\n"
                                   "8. Small Screen\n"
                                   "9. Return to Main Menu\n"
                                   "10. Exit Application\n")
                match phone_type: # Runtime for the application; results are sorted alphabetically
                    case "1":
                        results = Prolog.query("good-cpu(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones are classified as having a good CPU due to their CPU being 1 GHz "
                              "or faster!\n\n"
                              "Press Enter to return to Main Menu")
                    case "2":
                        results = Prolog.query("good-ram(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones are classified as having good RAM due to having at or over 4 GB of RAM!\n\n"
                             "Press Enter to return to Main Menu")
                    case "3":
                        results = Prolog.query("high-end(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones are classified as \"high end\" due to fulfilling the requirements\n"
                              "for good RAM (>=4GB) and a good CPU (>=1GHz). Additionally, these phones have cameras with \n"
                              "at or over 5 megapixels of quality; this number is chosen due to the age of this dataset.\n\n"
                              "Press Enter to return to Main Menu")
                    case "4":
                        results = Prolog.query("modern(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones are classified as \"modern\" because they fulfill the requirements\n"
                              "for a high end phone (>=4GB RAM, >=1GHz CPU, >=5MP camera). Additionally, \n"
                              "these phones are as slimmer than 0.5 inches and have storage at or over 16 GB.\n\n"
                              "Press Enter to return to Main Menu")
                    case "5":
                        results = Prolog.query("old-school(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones are considered \"old school\" because they lack a GPS feature, have\n"
                              "CPUs slower than 1 GHz, and have less than 2 GB of Ram. They are also as wide as\n"
                              "or wider/bulkier than 0.6 inches!\n\n"
                              "Press Enter to return to Main Menu")
                    case "6":
                        results = Prolog.query("multimedia(X)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones are considered \"multimedia\" because they have a camera at or over 10 megapixels\n"
                              "and they have over 24GB of storage space!\n\n"
                              "Press Enter to return to Main Menu")
                    case "7":
                        results = Prolog.query("greater-width(X, 0.5)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones have a screen larger than 5 inches!\n\n"
                              "Press Enter to return to Main Menu")

                    case "8":
                        results = Prolog.query("lesser-width(X, 0.4)")
                        sorted_results = sorted(results, key=lambda result: result['X'].casefold())
                        for result in sorted_results:
                            print(result["X"])
                        input("\nThese phones have a screen smaller than 4 inches!\n\n"
                              "Press Enter to return to Main Menu")

                    case "9":
                        pass
                    case "10":
                        running = False
                    case _:
                        pass
            case "2":
                running = False
            case _:
                pass

        clear_screen()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runtime()
