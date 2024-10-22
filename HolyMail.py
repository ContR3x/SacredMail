import json
import random
import os
from colorama import Fore, Style, init

# Initialize Colorama for colored terminal text
init(autoreset=True)

# Load religions from JSON file
def load_religions():
    with open('data/religions.json', 'r') as f:
        return json.load(f)

# Generate a random email
def generate_email(religion):
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
    domain = religion.lower().replace(' ', '') + ".org"
    email = f"{username}@{domain}"
    return email

# Save the generated email to a text file
def save_email(email):
    with open('emails_generated.txt', 'a') as f:
        f.write(email + '\n')

# Export emails to JSON
def export_emails_to_json():
    with open('emails_generated.txt', 'r') as f:
        emails = f.read().splitlines()
    with open('emails.json', 'w') as f:
        json.dump(emails, f, indent=4)
    print(Fore.GREEN + "Emails exported to emails.json")

# Display email generation history
def show_history():
    if os.path.exists('emails_generated.txt'):
        with open('emails_generated.txt', 'r') as f:
            print(Fore.CYAN + "Email Generation History:")
            print(f.read())
    else:
        print(Fore.RED + "No emails generated yet.")

# Display the main menu
def show_menu():
    print(Fore.YELLOW + "\n--- HolyMail: Religious Email  ---")
    print("1. Generate Email")
    print("2. View History")
    print("3. Export Emails to JSON")
    print("4. Exit")

# Main program logic
def main():
    religions = load_religions()
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == '1':
            print(Fore.BLUE + "\nSelect a religion:")
            for i, religion in enumerate(religions, 1):
                print(f"{i}. {religion}")

            try:
                selection = int(input("Number: ")) - 1
                if selection < 0 or selection >= len(religions):
                    raise ValueError("Selection out of range.")
                email = generate_email(religions[selection])
                print(Fore.GREEN + f"Generated Email: {email}")
                save_email(email)
            except ValueError as e:
                print(Fore.RED + f"Invalid input: {e}")

        elif choice == '2':
            show_history()

        elif choice == '3':
            export_emails_to_json()

        elif choice == '4':
            print(Fore.YELLOW + "Exiting the program...")
            break

        else:
            print(Fore.RED + "Invalid option, try again.")

if __name__ == '__main__':
    main()
