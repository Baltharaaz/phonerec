import knowledge_base as kb
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def runtime():
    while True:
        running = True
        choice = input("Welcome to Phonerec! \n"
                       "Please select from the following options:\n"
                       "1. Get Phone by Classification\n"
                       "2. \n"
                       "3. Exit\n")
        clear_screen()
        match choice:
            case "1":
                phone_type = input("Select a type of phone to receive suggestions: \n"
                                   "1. \n"
                                   "2. \n"
                                   "3. \n"
                                   "4. \n"
                                   "5. \n"
                                   "6. \n"
                                   "7. \n"
                                   "8. \n"
                                   "9. \n"
                                   "10. \n")
                match phone_type:
                    case "1":



        clear_screen()




        if not running:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kb.kb_declare()
    runtime()
