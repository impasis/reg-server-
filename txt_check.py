"""def txt_write_user(username):
    with open("data2.txt", 'a') as file:
        file.write(f"{username}\n")

def txt_read_file():
    with open("data2.txt") as file:
        print(file.read())

def txt_delete_user(username):
    text = ""
    with open("data2.txt") as file:
        for name in file:
            name = name.split()
            name = name[0]

            if name != username:
                text += name + "\n"
    
    with open("data2.txt", 'w') as file:
        file.write(text)"""

# TEST