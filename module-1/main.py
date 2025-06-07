#Blaise Johnson, 6/7/2025
#Assignment 1.3 On the wall

#The pruspose of this program is to take a given number of bottles of beer and countdown from that number to 1.

def countdown(bottle_start):
#This function takes the number of bottles and counts down.
    
    while bottle_start > 1:
        print(f"{bottle_start} bottles of beer on the wall, {bottle_start} bottles of beer!")
        bottle_start -=1
        print(f"Take one down, pass it around, {bottle_start} bottles of beer on the wall.")
        # This subtracts one bottle from the total and prints the new total.

    if bottle_start == 1:
        print(f"1 bottle of beer on the wall, {bottle_start} bottle of beer!")
        print("Take one down, pass it around, no more bottles of beer on the wall.")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store or order some more, we need 99 bottles of beer on the wall.")
    
        return
        # covers the case where there is only one bottle left. reminds the user to order more beer, and ends the program.
def main():
    try:
        bottles = int(input("How many bottles of beer are on your wall?"))
        if bottles <= 0:
            print("Please enter a number greater than 0.")
            return
            
    except ValueError:
            print("Please enter a valid number.")
            return

    countdown(bottles)

main()

    