import datetime
import time
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


def rent_car():
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
                user = input("\nPlease enter username: ").strip()
                user_name = input("Please enter your name: ").strip()
                for userfile in open("memberdetails.txt"):
                    userfile = userfile.strip("\n").split("|")
                    if user_name in userfile[1] and user in userfile[2]:
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
                            start_rent = rent_details[3]
                            end_rent = rent_details[4]
                            check_start = str(start_date)
                            check_start = datetime.datetime.strptime(check_start, '%Y-%m-%d')
                            check_end = str(end_date)
                            check_end = datetime.datetime.strptime(check_end, '%Y-%m-%d')
                            existing_rentdate = datetime.datetime.strptime(start_rent, '%Y-%m-%d')
                            existing_return = datetime.datetime.strptime(end_rent, '%Y-%m-%d')
                            if car_name in file and existing_rentdate <= check_start <= existing_return or existing_rentdate <= check_end <= existing_return:

                                print("Car is currently rented on", start_date, "to", end_date)
                                condition = True
                                break

                            else:
                                condition = False

                        if not condition:
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
                            payment_id = create_id("BKU")
                            with open("rentedCar.txt", "a") as renting:
                                renting.write(payment_id)
                                renting.write("|")
                                renting.write(user_name)
                                renting.write("|")
                                renting.write(user)
                                renting.write("|")
                                renting.write(str(start_date))
                                renting.write("|")
                                renting.write(str(end_date))
                                renting.write("|")
                                renting.write(str(delta))
                                renting.write("|")
                                renting.write("Deposit Paid @ TnG E-Wallet")
                                renting.write("\n")
                                print(payment_id, "is your payment receipt ID.\n")
                                return False

                        if payment_status == 2:
                            payment_id = create_id("BKU")
                            with open("rentedCar.txt", "a") as renting:
                                renting.write(payment_id)
                                renting.write("|")
                                renting.write(user_name)
                                renting.write("|")
                                renting.write(user)
                                renting.write("|")
                                renting.write(str(start_date))
                                renting.write("|")
                                renting.write(str(end_date))
                                renting.write("|")
                                renting.write(str(delta))
                                renting.write("|")
                                renting.write("Deposit Paid @ Shopee Pay E-Wallet")
                                renting.write("\n")
                                print(payment_id, "is your payment receipt ID.\n")
                                return False

                        if payment_status is False:
                            payment_id = create_id("BKU")
                            with open("rentedCar.txt", "a") as renting:
                                renting.write(payment_id)
                                renting.write("|")
                                renting.write(user_name)
                                renting.write("|")
                                renting.write(user)
                                renting.write("|")
                                renting.write(str(start_date))
                                renting.write("|")
                                renting.write(str(end_date))
                                renting.write("|")
                                renting.write(str(delta))
                                renting.write("|")
                                renting.write("Deposit Paid @ Credit/Debit Card")
                                renting.write("|")
                                renting.write(cardholder_name)
                                renting.write("|")
                                renting.write(card_no)
                                renting.write("\n")
                                print("\n" + payment_id, "is your payment receipt ID.\n")
                                return False
        print("Car not in database.")


rent_car()
