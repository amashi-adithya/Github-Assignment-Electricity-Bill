print("Electricity Bill Calculator")
client_type = input("Enter consumer type (domestic/corporate/religious): ")
units = float(input("Enter electricity units used: "))
bill = 0

#Calculation Feature
if client_type == 'domestic':
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + (units - 100) * 15
    else:
        bill = (100 * 10) + (100 * 15) + (units - 200) * 20

elif client_type == "corporate":
    bill = units * 25

elif client_type == "religious":
    bill = units * 5

# SSCL Tax
sscl = bill * 0.025
total_bill = bill + sscl