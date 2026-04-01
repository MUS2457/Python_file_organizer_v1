from LOGIC import organizer

def main () :
    while True:
        user = input("Please enter the folder path or 'exit' to quit : ").strip()

        if user == "exit" :
            print("Quitting...")
            break

        elif not user :
            print("Please enter a valid folder path or 'exit' to quit : ")
            continue

        organizer.organize_folder(user)


if __name__ == "__main__" :
    main()
