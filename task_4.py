def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Невірна команда. Будь ласка, введіть ім'я користувача та номер телефону."
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Невірна команда. Будь ласка, введіть ім'я користувача та новий номер телефону."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def get_phone(args, contacts):
    if len(args) != 1:
        return "Невірна команда. Будь ласка, введіть ім'я користувача."
    name = args[0]
    if name in contacts:
        return f"Номер телефону для {name}: {contacts[name]}."
    else:
        return "Контакт не знайдено."

def list_all_contacts(contacts):
    if not contacts:
        return "Контакти не знайдено."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Ласкаво просимо до бота-асистента!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["закрити", "вихід"]:
            print("До побачення!")
            break
        elif command == "привіт":
            print("Як я можу вам допомогти?")
        elif command == "додати":
            print(add_contact(args, contacts))
        elif command == "змінити":
            print(change_contact(args, contacts))
        elif command == "телефон":
            print(get_phone(args, contacts))
        elif command == "всі":
            print(list_all_contacts(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
