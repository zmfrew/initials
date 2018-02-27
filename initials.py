def get_initials(fullname):
    fullname_list = fullname.split()
    initials = ""
    index = 0
    for i in fullname_list:
        initials += fullname_list[index][0]
        index += 1
    return initials.upper()

def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))

if __name__ == "__main__":
    main()