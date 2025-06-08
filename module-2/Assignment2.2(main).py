def calculate_cable_cost():
    print("Welcome to Blaise-ing Fast Fiber Optics")
    cable = float(input("How much cable do you need? "))

    if cable > 500:
        cost_of_cable = cable * 0.50
    elif cable > 250 and cable <= 500:
        cost_of_cable = cable * 0.70
    elif cable > 100 and cable <= 250:
        cost_of_cable = cable * 0.80
    else:
        cost_of_cable = cable * 0.87

    print("Your cost is: $" + str(round(cost_of_cable, 2)) + " for " + str(cable) + " ft of cable.")
    print("Thank you for choosing Blaise-ing Fast Fiber Optics!")

# Call the function
calculate_cable_cost()