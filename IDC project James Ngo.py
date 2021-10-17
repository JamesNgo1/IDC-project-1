import math
print("Welcome to Osprey car rentals.\n")

#Inform customer about inputs and then ask to continue.
print("At the prompts,  please enter the following:")
print("\tCustomer's classification code (a character: BDW)")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)\n")

#Ask if customer wants to continue and while loop for if customer watns to continue..
should_continue = input("Would you like to continue (Y/N) ?: ")
while should_continue == "y" or should_continue == "Y":
    customer_code = input("\nCustomer code (BDW): ")
    #This is while loop to weed out invalid customer codes.
    while customer_code != "B" and customer_code != "D" and customer_code != "W":
        #Display Error message.
        print("\n\t**** Invalid customer code. Try again. ****")
        #Need to reassign for new input.....
        customer_code = input("\nCustomer Code (BDW): ") 
    print("") #use this print statement as sepration
    #Below is the input statements for the user to enter
    number_of_days = int(input("Number of days:"))
    odometer_start = int(input("Odometer reading at the start:"))
    odometer_end = int(input("Odometer reading at the end:"))
    print("")
    #This variable use of operands to deal with average miles and number of miles driven
    number_of_miles_driven = (odometer_end - odometer_start) * 0.10
    average_miles = number_of_miles_driven / number_of_days
    number_of_weeks = number_of_days / 7
    average_mile_a_week = number_of_miles_driven / (math.ceil(number_of_weeks))
    base_charge = 190
    
    print("Customer summary:")
    print("\tclassification code:", customer_code)
    #The below is the use of if else statments to help divide code for each variable either the user picks
    # "B" , "D" , or "W"
    #Below is the code for "B" with the value to its variable.
    if customer_code == "B" and odometer_start < odometer_end:
        base_charge = 40.00
        mileage_charge = 0.25
        amount_due = (base_charge * number_of_days) + (mileage_charge * number_of_miles_driven)
    else:
        if odometer_end < odometer_start:
            base_charge = 40.00
            maxi = 1000000
            change = 0.10
            mileage_charge = 0.25
            subracto = odometer_end + maxi 
            outcome = subracto - odometer_start
            number_of_miles_driven = outcome * 0.10
            amount_due = (base_charge * number_of_days) + (mileage_charge * outcome * change)
        else:
            if customer_code == "D" and average_miles <= 100:
                base_charge = 60.00
                amount_due = format(base_charge * number_of_days,'.1f')
            else:
                limit = 100
                due = 0.25
                base_charge = 60.00
                left = average_miles - limit
                mileage_charge = left * due * number_of_days
                amount_due = format((base_charge * number_of_days) + mileage_charge , '.2f')
                
                if customer_code == "W" and average_mile_a_week <= 900:
                    number_of_weeks = number_of_days / 7
                    average_mile_a_week = number_of_miles_driven / (math.ceil(number_of_weeks))
                    base_charge = 190
                    amount_due = format (base_charge * (math.ceil(number_of_weeks)),'.1f')
                else:          
                     if 1500 > average_mile_a_week > 900:
                         due = 100
                         base_charge = 190
                         average_mile_a_week = number_of_miles_driven / (math.ceil(number_of_weeks))
                         mileage_charge = due * ( math.ceil(number_of_weeks))
                         amount_due = format((base_charge * math.ceil(number_of_weeks)) + due*(math.ceil(number_of_weeks)) , '.1f')
                     else:
                         if average_mile_a_week > 1500:
                             limit = 1500
                             due = 200
                             base_charge = 190
                             costo = due * (math.ceil(number_of_weeks))
                             left = number_of_miles_driven - (limit*(math.ceil(number_of_weeks)))
                             charge = 0.25
                             amount_due = base_charge*(math.ceil(number_of_weeks))+ costo + (left * charge)
                            
    #Below is going to be the output of the information gather and process.                             
    print("\trental period (days):", number_of_days)
    print("\todometer reading at start:", odometer_start)
    print("\todometer reading at end:", odometer_end)
    print("\tnumber of miles driven:",format( number_of_miles_driven , '.1f'))
    print("\tamount due: $", (amount_due))
    print("")
    should_continue = input("Would you like to continue (Y/N) ?: ")
    
    
#Print goodbye message if the user doesn't want to continue...
print("Thank you for your loyalty!")
    
