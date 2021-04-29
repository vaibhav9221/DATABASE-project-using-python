from dbhelper import DBHelper


def main():
    help = DBHelper()
    while True:
        print("****************WELCOME****************")
        print()
        print("PRESS 1 TO INSERT DATA")
        print("PRESS 2 TO display DATA")
        print("PRESS 3 TO  delete DATA")
        print("PRESS 4 TO update DATA")
        print("PRESS 5 TO exit DATA")
        print()

        try:
            choice = int(input("Enter you choice :"))
            if choice == 1:
                userid = int(input("Enter user id :"))
                username = input("Enter username :")

                phone = input("Enter user phone :")
                help.insert_user(userid, username, phone)

            elif choice == 2:
                help.fetchAll()

            elif choice == 3:
                userid=int(input("Enter id you want to delete"))
                help.deleteData(userid)

            elif choice == 4:
                userid = int(input("Enter user id :"))
                username = input("new name :")
                help.updateTable(userid, username)

            elif choice == 5:
                break
            else:
                print("PLEASE ENTER VALID OUTPUT")
        except Exception as e:
            print(e)
            print("Invalid output")


if __name__ == "__main__":
    main()
