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