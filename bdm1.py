class BloodDonorRegistration:

    def __init__(self):
        # Store users and donors in lists
        self.users = []
        self.donors = []

    # ---------------- Register ----------------
    def register(self):
        print("\n--- Register ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        self.users.append({"username": username, "password": password})
        print("Registration Successful!\n")

    # ---------------- Login ----------------
    def login(self):
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user["username"] == username and user["password"] == password:
                print("Login Successful!\n")
                return True

        print("Invalid Login!\n")
        return False

    # ---------------- Add Donor ----------------
    def add_donor(self):
        print("\n--- Add Donor ---")
        name = input("Name: ")
        blood = input("Blood Group: ")
        phone = input("Phone: ")
        city = input("City: ")

        donor = {
            "name": name,
            "blood": blood,
            "phone": phone,
            "city": city
        }

        self.donors.append(donor)
        print("Donor Added Successfully!\n")

    # ---------------- View Donors ----------------
    def view_donors(self):
        print("\n--- Donor List ---")

        if not self.donors:
            print("No donors available!\n")
            return

        for d in self.donors:
            print(f"Name: {d['name']} | Blood: {d['blood']} | Phone: {d['phone']} | City: {d['city']}")
        print()

    # ---------------- Search Donor ----------------
    def search_donor(self):
        print("\n--- Search Donor ---")
        blood = input("Enter Blood Group: ")

        found = False
        for d in self.donors:
            if d["blood"] == blood:
                print(f"Name: {d['name']} | Phone: {d['phone']} | City: {d['city']}")
                found = True

        if not found:
            print("No donors found!")

        print()

    # ---------------- Main Menu ----------------
    def menu(self):
        while True:
            print("===== Blood Donor System =====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.register()

            elif choice == '2':
                if self.login():
                    while True:
                        print("\n--- Menu ---")
                        print("1. Add Donor")
                        print("2. View Donors")
                        print("3. Search Donor")
                        print("4. Logout")

                        option = input("Enter option: ")

                        if option == '1':
                            self.add_donor()
                        elif option == '2':
                            self.view_donors()
                        elif option == '3':
                            self.search_donor()
                        elif option == '4':
                            break
                        else:
                            print("Invalid choice!")

            elif choice == '3':
                print("Thank you!")
                break

            else:
                print("Invalid choice!")


# Run program
obj = BloodDonorRegistration()
obj.menu()