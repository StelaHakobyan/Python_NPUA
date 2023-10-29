while True:
    try:
        file_name = input("Enter the name of the text file you want to open: ")
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("File content:")
            print(file_content)

        write_option = input("Do you want to write to the same file (enter 'yes' or 'no')? ").lower()

        if write_option == 'yes':
            new_content = input("Enter the new content you want to write to the file: ")
            with open(file_name, 'a') as file:
                file.write("\n" + new_content)
            print("Content has been successfully written to the file.")
        else:
            new_file_name = input("Enter the name of the new file: ")
            try:
                with open(new_file_name, 'w') as new_file:
                    new_content = input("Enter the content you want to write to the new file: ")
                    new_file.write(new_content)
                    print("Content has been successfully written to the new file.")
            except FileNotFoundError:
                print("File not found. Please enter a valid filename.")

    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except ValueError:
        print("Invalid input. Please enter a valid filename.")
    else:
        break
    finally:
        print("File has been closed.")