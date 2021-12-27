import time
import datetime


def create_id(id):
    with open("create_id.txt", "r") as file:
        nxtid = ""
        record = file.readline().strip().split(", ")
        index = 0

        if id == "MEM":
            index = 0
        if id == "CAR":
            index = 1
        if id == "BKU":
            index = 2
        if id == "PMU":
            index = 3

        nxtid = record[index]

        temp = str(int(nxtid[3:]) + 1)
        if len(temp) == 1:
            nxtid = id + "000" + temp
        elif len(temp) == 2:
            nxtid = id + "00" + temp
        elif len(temp) == 3:
            nxtid = id + "0" + temp

    with open("create_id.txt", "w") as file:
        record[index] = nxtid
        file.write(", ".join(record))

    return nxtid


# Registered member
def register():
    print("You will be redirected to the register page...\n")
    time.sleep(1)
    while True:
        member_name = input("Please enter your name: ")
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        email = input("Please enter a valid email address: ")
        hp_num = input("Please enter a valid phone number: ")

        with open("memberdetails.txt") as file:
            file = file.readline()
            line = file.strip("\n").split("|")

            if username in line[2]:
                print("Username is taken.\n")
                continue

            elif email in line[4]:
                print("Email is associated with another account.\n")
                continue

            elif hp_num in line[5]:
                print("Phone number is associated with another account.\n")
                continue

            else:
                mem_id = create_id("MEM")
                with open("memberdetails.txt", "a") as memberfile:
                    memberfile.write(mem_id)
                    memberfile.write("|")
                    memberfile.write(member_name)
                    memberfile.write("|")
                    memberfile.write(username)
                    memberfile.write("|")
                    memberfile.write(password)
                    memberfile.write("|")
                    memberfile.write(email)
                    memberfile.write("|")
                    memberfile.write(hp_num)
                    memberfile.write("\n")
                    print("You have been registered.\n")
                    return True


def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        for line in open("memberdetails.txt"):
            member_info = line.strip("\n").split("|")

            if username == member_info[2] and password == member_info[3]:
                print("\nLoading...")
                time.sleep(1)

                print("\nYou are logged in! Welcome,", username + "\n")
                login_menu(username)
                return False
        print("\nWrong credentials.\n")


def rent_car(file4):
    member = file4
    condition = ""
    payment_status = ""
    delta = ""
    cardholder_name = ""
    card_no = ""
    while True:

        car_name = input("Please enter full car name as shown in list: ")
        for file in open("cardetails.txt"):
            file = file.strip("\n").split("|")
            while car_name in file:
                user_name = input("Please enter your name: ").strip()
                for userfile in open("memberdetails.txt"):
                    userfile = userfile.strip("\n").split("|")

                    if user_name in userfile[1] and member in userfile[2]:
                        print("\nPlease Enter Renting Duration:- ")
                        start_day = int(input("Start Date: "))
                        start_month = int(input("Start Month: "))
                        start_year = int(input("Start Year: "))
                        start_date = datetime.date(start_year, start_month, start_day)
                        print("Start of rent: ", start_date)

                        end_day = int(input("\nReturn Date: "))
                        end_month = int(input("Return Month: "))
                        end_year = int(input("Return Year: "))
                        end_date = datetime.date(end_year, end_month, end_day)
                        print("Return date: ", end_date)
                        for rent_details in open("rentedCar.txt"):
                            rent_details = rent_details.strip("\n").split("|")
                            start_rent = rent_details[4]
                            end_rent = rent_details[5]
                            check_start = str(start_date)
                            check_start = datetime.datetime.strptime(check_start, '%Y-%m-%d')
                            check_end = str(end_date)
                            check_end = datetime.datetime.strptime(check_end, '%Y-%m-%d')
                            existing_rent = datetime.datetime.strptime(start_rent, '%Y-%m-%d')
                            existing_return = datetime.datetime.strptime(end_rent, '%Y-%m-%d')

                            if car_name in file:
                                if "Deposit Paid @ ShopeePay E-Wallet (Deposit)" or "Deposit Paid @ Credit/Debit Card" or "Deposit Paid @ TnG E-Wallet (Deposit)" in file[7]:
                                    if existing_rent <= check_start <= existing_return or existing_rent <= check_end <= existing_return:
                                        print("Car is currently rented on", existing_rent, "to", existing_return)
                                        condition = True
                                        break
                            else:
                                condition = False

                        if condition is False:
                            delta = end_date - start_date
                            print("\nDuration of tenure: ", delta)
                            print("Deposit is MYR500.00")
                            print("\nSelect a Payment Method")
                            print("\t1 Credit/Debit Card")
                            print("\t2 TnG E-Wallet")
                            print("\t3 ShopeePay")
                            payment_method = input("\nPlease enter a response: ")
                            if payment_method == "1":

                                cardholder_name = input("Full Name (as shown on card): ").upper()
                                cardholder_address = input("Enter street: ").upper()
                                cardholder_zip = input("Enter zip code: ")
                                cardholder_city = input("Enter City: ").upper()
                                cardholder_state = input("Enter State: ").upper()
                                card_no = input("Card Number: ")
                                tac_no = input("TAC Code: ")

                                for cardfile in open("cardDetails.txt"):
                                    cardfile = cardfile.strip("\n").split("|")
                                    if len(card_no) == 16 and len(tac_no) == 3:
                                        if cardholder_name in cardfile[0]:
                                            if cardholder_address in cardfile[1]:
                                                if cardholder_zip in cardfile[2]:
                                                    if cardholder_city in cardfile[3]:
                                                        if cardholder_state in cardfile[4]:
                                                            if card_no in cardfile[5]:
                                                                if tac_no in cardfile[6]:
                                                                    payment_status = False
                                                                else:
                                                                    print("Wrong details entered.")
                                                                    continue
                                                            else:
                                                                print("Wrong details entered.")
                                                                continue
                                                        else:
                                                            print("Wrong details entered.")
                                                            continue
                                                    else:
                                                        print("Wrong details entered.")
                                                        continue
                                                else:
                                                    print("Wrong details entered.")
                                                    continue
                                            else:
                                                print("Wrong details entered.")
                                                continue
                                        else:
                                            print("Wrong details entered.")
                                            continue
                                    else:
                                        print("Wrong details entered.")
                                        continue

                            elif payment_method == "2":
                                print("Redirecting to merchant's page...")
                                time.sleep(2)
                                print("Please scan QR code.")
                                time.sleep(2)
                                print("Payment successful\n")
                                payment_status = 1

                            elif payment_method == "3":
                                print("Redirecting to merchant's page...")
                                time.sleep(2)
                                print("Please scan QR code.")
                                time.sleep(2)
                                print("Payment successful\n")
                                payment_status = 2

                            else:
                                print("Please enter a valid response.")
                                continue

                        if payment_status == 1:
                            booking_id = create_id("BKU")
                            payment_id = create_id("PMU")
                            with open("rentedCar.txt", "a") as renting:
                                renting.write(booking_id)
                                renting.write("|")
                                renting.write(user_name)
                                renting.write("|")
                                renting.write(member)
                                renting.write("|")
                                renting.write(car_name)
                                renting.write("|")
                                renting.write(str(start_date))
                                renting.write("|")
                                renting.write(str(end_date))
                                renting.write("|")
                                renting.write(str(delta))
                                renting.write("|")
                                renting.write("Deposit Paid @ TnG E-Wallet (Deposit)")
                                renting.write("|")
                                renting.write(payment_id)
                                renting.write("\n")
                                print(booking_id, "is your payment receipt ID.\n")
                                return False

                        if payment_status == 2:
                            booking_id = create_id("BKU")
                            payment_id = create_id("PMU")
                            with open("rentedCar.txt", "a") as renting:
                                renting.write(booking_id)
                                renting.write("|")
                                renting.write(user_name)
                                renting.write("|")
                                renting.write(member)
                                renting.write("|")
                                renting.write(car_name)
                                renting.write("|")
                                renting.write(str(start_date))
                                renting.write("|")
                                renting.write(str(end_date))
                                renting.write("|")
                                renting.write(str(delta))
                                renting.write("|")
                                renting.write("Deposit Paid @ ShopeePay E-Wallet (Deposit)")
                                renting.write("|")
                                renting.write(payment_id)
                                renting.write("\n")
                                print(booking_id, "is your payment receipt ID.\n")
                                return False

                        if payment_status == False:
                            booking_id = create_id("BKU")
                            payment_id = create_id("PMU")
                            with open("rentedCar.txt", "a") as renting:
                                renting.write(booking_id)
                                renting.write("|")
                                renting.write(user_name)
                                renting.write("|")
                                renting.write(member)
                                renting.write("|")
                                renting.write(car_name)
                                renting.write("|")
                                renting.write(str(start_date))
                                renting.write("|")
                                renting.write(str(end_date))
                                renting.write("|")
                                renting.write(str(delta))
                                renting.write("|")
                                renting.write("Deposit Paid @ Credit/Debit Card")
                                renting.write("|")
                                renting.write(payment_id)
                                renting.write("\n")
                                print("\n" + booking_id, "is your payment receipt ID.\n")
                                return False
        print("Car not in database.")


def view_rentCar(file3):
    member = file3
    print("Loading...")
    time.sleep(1)

    i = 1
    while i != 0:
        with open("cardetails.txt") as car_details:
            car_details = car_details.readlines()
            for line in car_details:
                line = line.split("|")

                car_name = line[1]
                car_engine = line[2]
                car_segment = line[3]
                car_type = line[4]
                car_colour = line[5]

                print("\n--------------- CAR", i, "---------------")
                print("Car Name\t\t: ", car_name)
                print("Engine Capacity\t: ", car_engine)
                print("Car Segment\t\t: ", car_segment)
                print("Car Type\t\t: ", car_type)
                print("Colour\t\t\t: ", car_colour)

                print("\n\t1 View Next Record")
                print("\t2 Rent this car")
                print("\t0 Return to menu\n")
                viewRentcar_status = input("Please enter a response: ")

                if viewRentcar_status == "1":
                    i += 1

                if viewRentcar_status == "2":
                    i = 0
                    condition = True

                else:
                    return False

                if condition is True:
                    rent_car(member)
                    return False


def view_rentalhistory(file2):
    member = file2
    i = 1
    while i != 0:
        with open("rentedCar.txt") as detail:
            detail = detail.readlines()
            for line in detail:
                line = line.split("|")

                if member in line:
                    booking_id = line[0]
                    payment_id = line[8]
                    name = line[1]
                    car_name = line[3]
                    rent_date = line[4]
                    return_date = line[5]
                    duration = line[6]
                    status = line[7]

                    print("\n--------------- CAR", i,"---------------")
                    print("Booking ID\t\t: ", booking_id)
                    print("Renter\t\t\t: ", name)
                    print("Car Name\t\t: ", car_name)
                    print("Rent Date\t\t: ", rent_date)
                    print("Return Date\t\t: ", return_date)
                    print("Rent Duration\t: ", duration)
                    print("Current status\t: ", status)
                    print("Payment ID\t\t: ", payment_id)

                    print("\t1 View Next Record")
                    print("\t0 Return to menu\n")
                    subStatus = input("Please enter a response: ")

                    if subStatus == "1":
                        i += 1

                    else:
                        print("You will be redirected to menu\n")
                        return False

            print("\n---------------No more available record---------------")
            print("\n\t1 Return to Main Menu.\n")
            miniStatus = input("Please enter a response: ")

            if miniStatus == "1":
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False

            else:
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False


def modify_personal_details(file7):
    criteria = file7
    data = []
    user_id = ""
    user_name = ""
    newusername = ""
    password = ""
    email = ""
    number = ""
    while True:
        if criteria == "PASS":
            user_pass = input("Please enter old password: ")
            new_userpass = input("Please enter new password: ")

            with open("memberdetails.txt") as filehandle:
                filehandle = filehandle.readlines()
                for line in filehandle:
                    line = line.strip("\n").split("|")

                    if user_pass in line[3]:
                        line.pop(3)
                        line.insert(3, new_userpass)
                        user_id = line[0]
                        user_name = line[1]
                        newusername = line[2]
                        password = line[3]
                        email = line[4]
                        number = line[5]

                for line in filehandle:
                    if user_pass in line:
                        filehandle.remove(line)
                        data.append(filehandle)

                        with open("memberdetails.txt", "w") as new_car:
                            new_car.writelines(filehandle)
                            new_car.write(user_id)
                            new_car.write("|")
                            new_car.write(user_name)
                            new_car.write("|")
                            new_car.write(newusername)
                            new_car.write("|")
                            new_car.write(password)
                            new_car.write("|")
                            new_car.write(email)
                            new_car.write("|")
                            new_car.write(number)
                            new_car.write("\n")
                            print("Details successfully changed.\n")
                            return False

        if criteria == "EMAIL":
            user_email = input("Please enter old email: ")
            new_useremail = input("Please enter new email: ")

            with open("memberdetails.txt") as filehandle:
                filehandle = filehandle.readlines()
                for line in filehandle:
                    line = line.strip("\n").split("|")

                    if user_email in line[4]:
                        line.pop(4)
                        line.insert(4, new_useremail)
                        user_id = line[0]
                        user_name = line[1]
                        newusername = line[2]
                        password = line[3]
                        email = line[4]
                        number = line[5]

                for line in filehandle:
                    if user_email in line:
                        filehandle.remove(line)
                        data.append(filehandle)

                        with open("memberdetails.txt", "w") as new_car:
                            new_car.writelines(filehandle)
                            new_car.write(user_id)
                            new_car.write("|")
                            new_car.write(user_name)
                            new_car.write("|")
                            new_car.write(newusername)
                            new_car.write("|")
                            new_car.write(password)
                            new_car.write("|")
                            new_car.write(email)
                            new_car.write("|")
                            new_car.write(number)
                            new_car.write("\n")
                            print("Details successfully changed.\n")
                            return False

        if criteria == "HP":
            user_hp = input("Please enter old phone number: ")
            new_userhp = input("Please enter new phone number: ")

            with open("memberdetails.txt") as filehandle:
                filehandle = filehandle.readlines()
                for line in filehandle:
                    line = line.strip("\n").split("|")

                    if user_hp in line[5]:
                        line.pop(5)
                        line.insert(5, new_userhp)
                        user_id = line[0]
                        user_name = line[1]
                        newusername = line[2]
                        password = line[3]
                        email = line[4]
                        number = line[5]

                for line in filehandle:
                    if user_hp in line:
                        filehandle.remove(line)
                        data.append(filehandle)

                        with open("memberdetails.txt", "w") as new_car:
                            new_car.writelines(filehandle)
                            new_car.write(user_id)
                            new_car.write("|")
                            new_car.write(user_name)
                            new_car.write("|")
                            new_car.write(newusername)
                            new_car.write("|")
                            new_car.write(password)
                            new_car.write("|")
                            new_car.write(email)
                            new_car.write("|")
                            new_car.write(number)
                            new_car.write("\n")
                            print("Details successfully changed.\n")
                            return False


def login_menu(file1):
    member = file1
    while True:
        print("---------- LOGIN MENU ----------")
        print("\t1 Modify Personal Details")
        print("\t2 View Rental History")
        print("\t3 View Car Details/Rent Car")
        print("\t4 Log Out")
        response = input("\nPlease enter a response: ").strip()

        if response == "1":
            print("\n-------- MODIFY --------")
            print("\t1 Password")
            print("\t2 E-Mail")
            print("\t3 Phone Number")
            choice = input("\nPlease enter a response: ")

            if choice == "1":
                modify_personal_details("PASS")
                continue
            if choice == "2":
                modify_personal_details("EMAIL")
                continue
            if choice == "3":
                modify_personal_details("HP")
                continue

        if response == "2":
            view_rentalhistory(member)
            continue

        if response == "3":
            view_rentCar(member)
            continue

        if response == "4":
            print("\nYou will be logged out.")
            time.sleep(1)
            print("You are logged out. Good-bye.")
            return False

        else:
            print("Please enter a valid response")
            continue


def view_car():
    print("Loading...")
    time.sleep(2)

    i = 1
    while i != 0:
        with open("cardetails.txt") as car_details:
            car_details = car_details.readlines()
            for line in car_details:
                line = line.split("|")

                car_name = line[1]
                car_engine = line[2]
                car_segment = line[3]
                car_type = line[4]
                car_colour = line[5]

                print("\n--------------- CAR", i, "---------------")
                print("Car Name\t\t: ", car_name)
                print("Engine Capacity\t: ", car_engine)
                print("Car Segment\t\t: ", car_segment)
                print("Car Type\t\t: ", car_type)
                print("Colour\t\t\t: ", car_colour)

                print("\n\t1 View Next Record")
                print("\t0 Return to menu\n")
                viewcar_status = input("Please enter a response: ")

                if viewcar_status == "1":
                    i += 1

                else:
                    return False

            print("\n---------------No more available record---------------")
            print("\n\t1 Return to Main Menu.\n")
            miniStatus = input("Please enter a response: ")

            if miniStatus == "1":
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False

            else:
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False


# Admin
def adminview_rentcar():
    print("Loading...")
    time.sleep(2)

    i = 1
    while i != 0:
        with open("cardetails.txt") as car_details:
            car_details = car_details.readlines()
            for line in car_details:
                line = line.split("|")

                car_id = line[0]
                car_name = line[1]
                car_engine = line[2]
                car_segment = line[3]
                car_type = line[4]
                car_colour = line[5]

                print("\n--------------- CAR", i, "---------------")
                print("Car ID\t\t\t: ", car_id)
                print("Car Name\t\t: ", car_name)
                print("Engine Capacity\t: ", car_engine)
                print("Car Segment\t\t: ", car_segment)
                print("Car Type\t\t: ", car_type)
                print("Colour\t\t\t: ", car_colour)

                print("\n\t1 View Next Record")
                print("\t0 Return to menu\n")
                viewcar_status = input("Please enter a response: ")

                if viewcar_status == "1":
                    i += 1

                else:
                    return False
            print("\n---------------No more available record---------------")
            print("\n\t1 Return to Main Menu.\n")
            miniStatus = input("Please enter a response: ")

            if miniStatus == "1":
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False

            else:
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False


def car_modify(file5):
    search = file5
    while True:
        with open("cardetails.txt", "r") as carfile:
            modify_list = carfile.readlines()

            for line in open("cardetails.txt"):
                line = line.strip("\n").split("|")

                if search in line:
                    existing = input("Enter exact existing details: ")
                    new = input("Enter new details: ")
                    for file in open('cardetails.txt'):
                        while existing in file:
                            oldline = file
                            newline = file.replace(existing, new)
                            modify_list.remove(oldline)
                            modify_list.append(newline)
                            with open("cardetails.txt", "w") as car_file:
                                car_file.writelines(modify_list)

                            print("Details has been changed successfully")
                            print("You will be redirected to main menu.")
                            time.sleep(1)
                            return False

                    print("Invalid details")
                    continue


def return_car():
    while True:
        print("Loading...\n")
        time.sleep(1)

        print("--------- RETURN CAR --------- ")
        username = input("Please enter customer username: ")
        car_name = input("Please enter rented car name: ")
        rent_date = input("Please enter rent date: ")
        return_date = input("Please enter return date: ")

        for line in open("rentedCar.txt"):
            line = line.strip("\n").split("|")
            if username in line[2] and car_name in line[3] and rent_date in line[4] and return_date in line[5]:
                if "Deposit Paid" in line[7]:
                    book_id = line[0]
                    customer_name = line[1]
                    customer_username = line[2]
                    rented_car = line[3]
                    start_rent = line[4]
                    end_rent = line[5]
                    duration = line[6]
                    duration = duration[:6]
                    payment_status = line[7]
                    payment_id = line[8]

                    print("\nBooking ID\t\t\t\t: ", book_id)
                    print("Customer Name\t\t\t: ", customer_name)
                    print("Customer Username\t\t: ", customer_username)
                    print("Rented Car Name\t\t\t: ", rented_car)
                    print("Rent Date\t\t\t\t: ", start_rent)
                    print("Return Date\t\t\t\t: ", end_rent)
                    print("Rent Duration\t\t\t: ", duration)
                    print("Current Payment Status\t: ", payment_status)
                    print("Payment ID\t\t\t\t: ", payment_id)

                    print("\n\tDaily Rate is RM70")
                    payment_amount = int(input("\nPlease enter correct duration: "))
                    payment_checking = str(payment_amount) + " days"

                    if payment_checking == duration:
                        if payment_amount <= 5:
                            price = 70 * payment_amount
                        elif payment_amount <= 20:
                            price = 65 * payment_amount
                        elif payment_amount > 21:
                            price = 55 * payment_amount

                        print("\tRM" + str(price), "is to be paid")
                        print("\nSelect a Payment Method:\n")
                        print("\t1 Credit/Debit Card")
                        print("\t2 TnG E-Wallet")
                        print("\t3 ShopeePay")

                        payment_method = input("\nPlease enter a response: ")
                        if payment_method == "1":

                            cardholder_name = input("Full Name (as shown on card): ").upper()
                            cardholder_address = input("Enter street: ").upper()
                            cardholder_zip = input("Enter zip code: ")
                            cardholder_city = input("Enter City: ").upper()
                            cardholder_state = input("Enter State: ").upper()
                            card_no = input("Card Number: ")
                            tac_no = input("TAC Code: ")

                            for cardfile in open("cardDetails.txt"):
                                cardfile = cardfile.strip("\n").split("|")
                                if len(card_no) == 16 and len(tac_no) == 3:
                                    if cardholder_name in cardfile[0]:
                                        if cardholder_address in cardfile[1]:
                                            if cardholder_zip in cardfile[2]:
                                                if cardholder_city in cardfile[3]:
                                                    if cardholder_state in cardfile[4]:
                                                        if card_no in cardfile[5]:
                                                            if tac_no in cardfile[6]:
                                                                payment_status = False
                                                            else:
                                                                print("Wrong details entered.")
                                                                continue
                                                        else:
                                                            print("Wrong details entered.")
                                                            continue
                                                    else:
                                                        print("Wrong details entered.")
                                                        continue
                                                else:
                                                    print("Wrong details entered.")
                                                    continue
                                            else:
                                                print("Wrong details entered.")
                                                continue
                                        else:
                                            print("Wrong details entered.")
                                            continue
                                    else:
                                        print("Wrong details entered.")
                                        continue
                                else:
                                    print("Wrong details entered.")
                                    continue

                        elif payment_method == "2":
                            print("Redirecting to merchant's page...")
                            time.sleep(2)
                            print("Please scan QR code.")
                            time.sleep(2)
                            print("Payment successful\n")
                            payment_status = 1

                        elif payment_method == "3":
                            print("Redirecting to merchant's page...")
                            time.sleep(2)
                            print("Please scan QR code.")
                            time.sleep(2)
                            print("Payment successful\n")
                            payment_status = 2

                        else:
                            print("Please enter a valid response.")
                            continue

                        if payment_status == 1:
                            data = []
                            existing = "Deposit Paid"
                            new = ("RM" + str(price) + " paid @ TNG E-Wallet")

                            with open("rentedCar.txt") as filehandle:
                                filehandle = filehandle.readlines()
                                for line in filehandle:
                                    line = line.strip("\n").split("|")
                                    if car_name in line[3] and rent_date in line[4] and return_date in line[5]:
                                        if existing in line[7]:
                                            line.pop(7)
                                            line.insert(7, new)
                                            booking_id = line[0]
                                            cust_name = line[1]
                                            cust_username = line[2]
                                            carName = line[3]
                                            start_date = line[4]
                                            end_date = line[5]
                                            duration = line[6]
                                            status = line[7]
                                            paymentID = line[8]


                                    for line in filehandle:
                                        if existing in line:
                                            filehandle.remove(line)
                                            data.append(filehandle)

                                            with open("rentedCar.txt", "w") as new_rent:
                                                new_rent.writelines(filehandle)
                                                new_rent.write(booking_id)
                                                new_rent.write("|")
                                                new_rent.write(cust_name)
                                                new_rent.write("|")
                                                new_rent.write(cust_username)
                                                new_rent.write("|")
                                                new_rent.write(carName)
                                                new_rent.write("|")
                                                new_rent.write(start_date)
                                                new_rent.write("|")
                                                new_rent.write(end_date)
                                                new_rent.write("|")
                                                new_rent.write(duration)
                                                new_rent.write("|")
                                                new_rent.write(status)
                                                new_rent.write("|")
                                                new_rent.write(paymentID)
                                                new_rent.write("\n")
                                                print("Car is returned, payment received.")
                                                return False

                        if payment_status == 2:
                            data = []
                            existing = "Deposit Paid"
                            new = ("RM" + str(price) + " paid @ ShopeePay")

                            with open("rentedCar.txt") as filehandle:
                                filehandle = filehandle.readlines()
                                for line in filehandle:
                                    line = line.strip("\n").split("|")
                                    if car_name in line[3] and rent_date in line[4] and return_date in line[5]:
                                        if existing in line[7]:
                                            line.pop(7)
                                            line.insert(7, new)
                                            booking_id = line[0]
                                            cust_name = line[1]
                                            cust_username = line[2]
                                            carName = line[3]
                                            start_date = line[4]
                                            end_date = line[5]
                                            duration = line[6]
                                            status = line[7]
                                            paymentID = line[8]


                                    for line in filehandle:
                                        if existing in line:
                                            filehandle.remove(line)
                                            data.append(filehandle)

                                            with open("rentedCar.txt", "w") as new_rent:
                                                new_rent.writelines(filehandle)
                                                new_rent.write(booking_id)
                                                new_rent.write("|")
                                                new_rent.write(cust_name)
                                                new_rent.write("|")
                                                new_rent.write(cust_username)
                                                new_rent.write("|")
                                                new_rent.write(carName)
                                                new_rent.write("|")
                                                new_rent.write(start_date)
                                                new_rent.write("|")
                                                new_rent.write(end_date)
                                                new_rent.write("|")
                                                new_rent.write(duration)
                                                new_rent.write("|")
                                                new_rent.write(status)
                                                new_rent.write("|")
                                                new_rent.write(paymentID)
                                                new_rent.write("\n")
                                                print("Car is returned, payment received.")
                                                return False

                        if payment_status is False:
                            data = []
                            existing = "Deposit Paid"
                            new = ("RM" + str(price) + " paid @ Credit/Debit Card")

                            with open("rentedCar.txt") as filehandle:
                                filehandle = filehandle.readlines()
                                for line in filehandle:
                                    line = line.strip("\n").split("|")
                                    if car_name in line[3] and rent_date in line[4] and return_date in line[5]:
                                        if existing in line[7]:
                                            line.pop(7)
                                            line.insert(7, new)
                                            booking_id = line[0]
                                            cust_name = line[1]
                                            cust_username = line[2]
                                            carName = line[3]
                                            start_date = line[4]
                                            end_date = line[5]
                                            duration = line[6]
                                            status = line[7]
                                            paymentDetail = line[8]
                                            paymentID = line[9]
                                            cardholder_name = line[10]
                                            card_no = line[11]

                                    for line in filehandle:
                                        if existing in line:
                                            filehandle.remove(line)
                                            data.append(filehandle)

                                            with open("rentedCar.txt", "w") as new_rent:
                                                new_rent.writelines(filehandle)
                                                new_rent.write(booking_id)
                                                new_rent.write("|")
                                                new_rent.write(cust_name)
                                                new_rent.write("|")
                                                new_rent.write(cust_username)
                                                new_rent.write("|")
                                                new_rent.write(carName)
                                                new_rent.write("|")
                                                new_rent.write(start_date)
                                                new_rent.write("|")
                                                new_rent.write(end_date)
                                                new_rent.write("|")
                                                new_rent.write(duration)
                                                new_rent.write("|")
                                                new_rent.write(status)
                                                new_rent.write("|")
                                                new_rent.write(paymentDetail)
                                                new_rent.write("|")
                                                new_rent.write(paymentID)
                                                new_rent.write("|")
                                                new_rent.write(cardholder_name)
                                                new_rent.write("|")
                                                new_rent.write(card_no)
                                                new_rent.write("\n")
                                                print("Car is returned, payment received.")
                                                return False


def admin_login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        for line in open("admindetails.txt"):
            admin_info = line.strip("\n").split("|")

            if username == admin_info[0] and password == admin_info[1]:
                print("\nYou are logged in! Welcome,", username)
                admin_menu()
                return False

        print("Wrong credentials.")


def subadmin_menu():
    with open("cardetails.txt", "r") as carfile:
        file = carfile.readline()
        file = file.strip("\n").split("|")

    while True:
        print("\n\t1 Add Car")
        print("\t2 View Car")
        print("\t3 Modify Car Details")
        print("\t4 Return Car")
        print("\t5 Return to Main Menu\n")
        submenu_status = input("Please enter a response: ").strip()

        if submenu_status == "1":
            car_name = input("Please enter car name: ")
            car_engine = input("Please enter car engine capacity: ").upper()
            car_segment = input("Please car segment: ").upper()
            car_type = input("Please enter car type: ").capitalize()
            car_colour = input("Please enter car colour: ").capitalize()
            car_plate = input("Please enter car plate number: ").upper()

            if car_plate == file[6]:
                print("Car is already in database.")
                print("Please re-enter details.")
                continue

            else:
                car_id = create_id("CAR")
                with open("cardetails.txt", "a") as car_file:
                    car_file.write(car_id)
                    car_file.write("|")
                    car_file.write(car_name)
                    car_file.write("|")
                    car_file.write(car_engine)
                    car_file.write("|")
                    car_file.write(car_segment + " Segment")
                    car_file.write("|")
                    car_file.write(car_type)
                    car_file.write("|")
                    car_file.write(car_colour)
                    car_file.write("|")
                    car_file.write(car_plate)
                    car_file.write("\n")

                    print("\n", car_name, "has been added to database.")

                    print("\nYou will be redirected to main menu\n")
                    time.sleep(1)
                    continue

        elif submenu_status == "2":
            detail_list = ['Car ID, Car Name, Engine Capacity, Segment, Type, Colour, Car Plate']
            print(detail_list)
            with open("cardetails.txt") as file:
                file = file.read()
                print(file)
                print("You will be redirected to menu")
                time.sleep(1)
                continue

        elif submenu_status == "3":
            print("Loading...")
            time.sleep(1)
            while True:
                print("\n\t1 Car ID\n\t2 Car Plate\n\t3 Return to Menu\n")
                modify_status = input("Please enter a response: ")
                if modify_status == "1":
                    oldsearch = input("Please enter Car ID or Car Plate: CAR")
                    search = "CAR" + oldsearch
                    print(search)
                    car_modify(search)

                elif modify_status == "2":
                    search = input("Please enter Car Plate: ")
                    car_modify(search)

                elif modify_status == "3":
                    return False

                else:
                    print("Please enter a valid response")

        elif submenu_status == "4":
            return_car()
            continue

        elif submenu_status == "5":
            print("You will be redirected to main menu")
            time.sleep(1)
            return False

        else:
            print("Please enter a valid response.")
            continue


def view_customer_booking():
    i = 1
    while i != 0:
        with open("rentedCar.txt") as rented_details:
            rented_details = rented_details.readlines()
            for line in rented_details:
                line = line.split("|")

                booking_id = line[0]
                customer_name = line[1]
                username = line[2]
                car_name = line[3]
                rent_date = line[4]
                return_date = line[5]
                duration = line[6]
                payment_method = line[8]
                payment_details = line[9]

                print("\n--------------- CAR", i, "---------------")
                print("Booking ID\t\t: ", booking_id)
                print("Customer Name\t: ", customer_name)
                print("Username\t\t: ", username)
                print("Rented Car Name\t: ", car_name)
                print("Rent Date\t\t: ", rent_date)
                print("Return Date\t\t: ", return_date)
                print("Rent Duration\t: ", duration)
                print("Payment Method\t: ", payment_method)
                print("Payment Details\t: ", payment_details)

                print("\n\t1 View Next Record")
                print("\t0 Return to menu\n")
                viewcar_status = input("Please enter a response: ")

                if viewcar_status == "1":
                    i += 1

                else:
                    return False

            print("\n---------------No more available record---------------")
            print("\n\t1 Return to Main Menu.\n")
            miniStatus = input("Please enter a response: ")

            if miniStatus == "1":
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False

            else:
                print("You will be redirected to menu...\n")
                time.sleep(1)
                return False


def search_file(file6):
    search = file6
    i = 1
    while i != 0:
        for file in open("rentedCar.txt"):
            file = file.strip("\n").split("|")
            booking_id = file[0]
            customer_name = file[1]
            username = file[2]
            car_name = file[3]
            rent_date = file[4]
            return_date = file[5]
            duration = file[6]
            payment_method = file[8]
            payment_details = file[9]

            if search in file:
                print("\n--------------- CAR", i, "---------------")
                print("Booking ID\t\t: ", booking_id)
                print("Customer Name\t: ", customer_name)
                print("Username\t\t: ", username)
                print("Rented Car Name\t: ", car_name)
                print("Rent Date\t\t: ", rent_date)
                print("Return Date\t\t: ", return_date)
                print("Rent Duration\t: ", duration)
                print("Payment Method\t: ", payment_method)
                print("Payment Details\t: ", payment_details)

                print("\n\t1 View Next Car")
                print("\t0 Return To Menu")
                choice = input("\nPlease enter a response: ")
                if choice == "1":
                    i += 1
                else:
                    print("You will be redirected back to menu...\n")
                    time.sleep(1)
                    return False

        print("\n---------------No more available record---------------")
        print("\n\t1 Return to Main Menu.\n")
        miniStatus = input("Please enter a response: ")

        if miniStatus == "1":
            print("You will be redirected to menu...\n")
            time.sleep(1)
            return False

        else:
            print("You will be redirected to menu...\n")
            time.sleep(1)
            return False


def subadmin_menu2():
    while True:
        print("--------------- Details ---------------")
        print("Press 1 to view Cars Rented Out")
        print("Press 2 to view car available to rent")
        print("Press 3 to view all customer bookings")
        print("Press 4 to view specified customer bookings")
        print("Press 5 to view customer bookings for a specific time duration")
        print("Press 6 to return to main menu\n")
        choice = input("Please enter response: ").strip()

        if choice == "1":
            rented = "Deposit Paid"
            print("Loading...")
            time.sleep(1)
            search_file(rented)
            continue

        if choice == "2":
            adminview_rentcar()
            continue

        if choice == "3":
            view_customer_booking()
            continue

        if choice == "4":
            print("\n\t1 Booking ID")
            print("\t2 Username")
            print("\t3 Customer Name")
            print("\t4 Car Name")
            print("\t5 Payment ID")
            print("\t6 Return to Menu")
            search = input("\nPlease enter a response: ")
            if search == "1":
                book_id = input("Please enter Booking ID: BKU")
                book_id = "BKU" + book_id
                search_file(book_id)
                continue

            if search == "2":
                username = input("Please enter username: ")
                search_file(username)
                continue

            if search == "3":
                cust_name = input("Please enter customer name: ")
                search_file(cust_name)
                continue
            if search == "4":
                car_name = input("Please enter car name: ")
                search_file(car_name)
                continue

            if search == "5":
                pay_id = input("Please enter Payment ID: PMU")
                pay_id = "PMU" + pay_id
                search_file(pay_id)
                continue

            else:
                print("")
                continue

        if choice == "5":
            print("1 YYYY/MM/DD (Rent/Return Date)")
            print("2 YYYY/MM")
            year = input("Please enter a response: ")

            if year == "1":
                search_year = input("Please enter YYYY/MM/DD (Rent/Return Date): ")
                search_file(search_year)
                continue

            if year == "2":
                search_year = input("Please enter YYYY/MM: ")
                search_file(search_year)
                continue

            else:
                print("Please enter a valid response: ")
                continue

        if choice == "6":
            return False

        else:
            print("Please enter a valid response.")
            continue


def admin_menu():
    while True:
        print("\n\t1 Cars\n\t2 Details\n\t3 Log Out\n")
        menu_status = input("Please enter a response: ").strip()
        if menu_status == "1":
            print("Loading...")
            time.sleep(1)
            subadmin_menu()

        elif menu_status == "2":
            print("Loading...")
            time.sleep(1)
            subadmin_menu2()

        elif menu_status == "3":
            print("You will be logged out.")
            time.sleep(1)
            print("\nYou are logged out. Good-bye")
            return True

        else:
            print("Please enter a valid response.")
            continue


def main():
    print("Loading...\n")
    time.sleep(2)
    while True:
        print("-----------SUPER CAR RENTAL SERVICES-------------")
        print("What would you like to do?\n")
        print("\t0 View Cars\n\t1 Login/Register\n\t2 Quit\n")
        main_status = input("Please enter a response: ").strip()
        if main_status == "0":
            view_car()
            continue

        if main_status == "1":
            print("Would you like to login or register?\n")
            print("\t1 Login as Member\n\t2 Register\n\t3 Login as Admin\n")
            sub_status = input("Please enter a response: ")

            if sub_status == "1":
                login()
                return False

            elif sub_status == "2":
                register()
                print("Would you like to login?")
                print("Y for Yes\nN for No")
                status = input("Please enter a response: ").strip().upper()

                if status == "Y":
                    login()
                    return False

                else:
                    continue

            elif sub_status == "3":
                admin_login()
                return False

            else:
                print("Please enter a valid response.")
                continue

        elif main_status == "2":
            print("You will be logged out.")
            time.sleep(1)
            print("\nYou are logged out. Good-bye")
            return False


main()
