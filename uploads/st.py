#body weight index
wt=float(input("Enter your  weight in kilograms:"))
ht=float(input("Enter your height in meters"))
if ht<=0 or ht>4 or wt<=0 or wt>700:
    print("Invalid input")
else:
    index = wt/(ht*ht)
    print("Your BMI is",index)
#-------------------------------------------------------------------------------------------------------------------------

#among three largest number
try:
    a = int(input("Enter the first number (1-300): "))
    if not (1 <= a <= 300):
        print("Invalid Input")
    else:
        b = int(input("Enter the second number (1-300): "))
        if not (1 <= b <= 300):
            print("Invalid Input")
        else:
            c = int(input("Enter the third number (1-300): "))
            if not (1 <= c <= 300):
                print("Invalid Input")
            else:
                result = max(a, b, c)
                print("The largest number is:", result)
except ValueError:
    print("Please enter valid integers.")
#-------------------------------------------------------------------------------------------------------------------------

#number in ascending order
while True:
    n1=int(input("Enter First Number:"))
    if 0 < n1 <=100:
        break
    else:
        print("Number should be between range 1 to 100")

while True:
    n2=int(input("Enter First Number:"))
    if 0 < n2 <=100:
        break
    else:
        print("Number should be between range 1 to 100")

while True:
    n3=int(input("Enter First Number:"))
    if 0 < n3 <=100:
        break
    else:
        print("Number should be between range 1 to 100")
        

num=[n1,n2,n3]
num.sort()
 
print(num)
#-------------------------------------------------------------------------------------------------------------------------

#insuarance policy/agency
try:

    age = int(input("Enter age: "))

    num_claims = int(input("Enter number of claims: "))

    premium_increase = 0

    send_warning = False

    cancel_policy = False

    if age <= 25:

        if num_claims == 0:

            premium_increase = 50

        elif num_claims == 1:

            premium_increase = 100

        elif 2 <= num_claims <= 4:

            premium_increase = 400

        elif num_claims >= 5:

            premium_increase = 200

            send_warning = True

            cancel_policy = True

    else:

        if num_claims == 0:

            premium_increase = 25

        elif num_claims == 1:

            premium_increase = 50

        elif 2 <= num_claims <= 4:

            premium_increase = 200

        elif num_claims >= 5:

            premium_increase = 200

            send_warning = True

            cancel_policy = True

    print(f"Age: {age}, Claims: {num_claims}")

    print(f"  Premium Increase: ${premium_increase}")

    if send_warning:

        print("  Warning Letter: Yes")

    if cancel_policy:

        print("  Cancel Policy: Yes")

    print()

except ValueError:

    print("Invalid input. Please enter numeric values for age and number of claims.")
#-------------------------------------------------------------------------------------------------------------------------

#rail card
def determine_discount(over_60_card, family_card, traveling_with_child):
    if over_60_card and family_card:
        return "Error: You can only hold one type of rail card."
    elif over_60_card:
        return 34
    elif family_card and traveling_with_child:
        return 50
    elif traveling_with_child:
        return 10
    else:
        return 0

def main():
    over_60_card = input("Do you have an 'Over 60s' rail card? (yes/no): ").strip().lower() == 'yes' 
    family_card = input("Do you have a family rail card? (yes/no): ").strip().lower() == 'yes' 
    traveling_with_child = input("Are you traveling with a child (under 16)? (yes/no): ").strip().lower() == 'yes'
    discount = determine_discount(over_60_card, family_card, traveling_with_child)
    if isinstance(discount, str):
        print(discount)
    elif discount > 0:
        print(f"You are eligible for a {discount}% discount.")
    else:
        print("You are not eligible for any discount.")
if __name__ == "__main__":
    main()
#-------------------------------------------------------------------------------------------------------------------------

#University Exam
def determine_pass_status(attendance, internal_test_1, internal_test_2, internal_test_3, external_exam):
    if attendance < 80:
        return "Fail"
    
    avg_test_1_3 = (internal_test_1 + internal_test_2 + internal_test_3) / 3
    avg_test_2_3 = (internal_test_1 + internal_test_2) / 2
    
    if avg_test_1_3 >= 10 or avg_test_2_3 >= 15:
        if external_exam > 35:
            return "Pass"
        else:
            return "Fail"
    else:
        return "Fail"

def main():
    attendance = float(input("Enter attendance percentage: "))
    internal_test_1 = float(input("Enter marks for Internal Test 1: "))
    internal_test_2 = float(input("Enter marks for Internal Test 2: "))
    internal_test_3 = float(input("Enter marks for Internal Test 3: "))
    external_exam = float(input("Enter marks for External Exam: "))
    
    result = determine_pass_status(attendance, internal_test_1, internal_test_2, internal_test_3, external_exam)
    print(f"The student has: {result}")

if __name__ == "__main__":
    main()
#-------------------------------------------------------------------------------------------------------------------------

#Time Display
class TimeDisplayDevice:
    def __init__(self):
        self.state = 'S1'  
        self.state_map = {
            'S1': 'T',  
            'S2': 'D',  
            'S3': 'AT', 
            'S4': 'AD'  
        }

    def change_mode(self):
        """Change the mode of the device."""
        if self.state == 'S1':
            self.state = 'S2'
        elif self.state == 'S2':
            self.state = 'S1'
        print(f"State: {self.state_map[self.state]}")

    def reset(self):
        """Reset the device to a different state based on current state."""
        if self.state == 'S1':
            self.state = 'S3'
        elif self.state == 'S2':
            self.state = 'S4'
        print(f"State: {self.state_map[self.state]}")

    def time_set(self):
        """Set the time, transitioning to state S1."""
        if self.state == 'S3':
            self.state = 'S1'
        print(f"State: {self.state_map[self.state]}")

    def date_set(self):
        """Set the date, transitioning to state S2."""
        if self.state == 'S4':
            self.state = 'S2'
        print(f"State: {self.state_map[self.state]}")

    def handle_input(self, command):
        """Handle user input commands."""
        if command == 'CM':
            self.change_mode()
        elif command == 'R':
            self.reset()
        elif command == 'TS':
            self.time_set()
        elif command == 'DS':
            self.date_set()
        else:
            print("Invalid command")

def main():
    device = TimeDisplayDevice()
    print("Welcome to the Time Display Device")
    print("Commands: CM (Change Mode), R (Reset), TS (Time Set), DS (Date Set), Q (Quit)")

    while True:
        command = input("Enter command: ").strip().upper()
        if command == 'Q':
            print("Exiting...")
            break
        device.handle_input(command)

if __name__ == "__main__":
    main()
#-------------------------------------------------------------------------------------------------------------------------

#Shopping
class ShoppingBasket:
    def __init__(self):
        self.state = 'empty'  
        self.basket = [] 
        self.total_cost = 0  

    def add_item(self, item, price):
        if self.state == 'empty' or self.state == 'shopping':
            self.basket.append(item)
            self.total_cost += price
            self.state = 'shopping'
            print(f"Added {item} to basket. Total cost: {self.total_cost}")
        else:
            print("Can't add items in the current state.")

    def remove_item(self, item, price):
        if self.state == 'shopping' and item in self.basket:
            self.basket.remove(item)
            self.total_cost -= price
            print(f"Removed {item} from basket. Total cost: {self.total_cost}")
            if not self.basket:
                self.state = 'empty'  
        else:
            print("Can't remove items in the current state or item not found.")

    def checkout(self):
        if self.state == 'shopping':
            self.state = 'summary'
            print(f"Checking out. Items in basket: {self.basket}. Total cost: {self.total_cost}")
        else:
            print("Can't checkout in the current state.")

    def ok(self):
        if self.state == 'summary':
            self.state = 'payment'
            print("Proceeding to payment system.")
        else:
            print("Can't proceed to payment in the current state.")

    def not_ok(self):
        if self.state == 'summary':
            self.state = 'shopping'
            print("Returning to shopping to modify basket.")
        else:
            print("Can't return to shopping in the current state.")

def generate_test_case():
    basket = ShoppingBasket()  
    print("State Transition Test for Shopping Basket")

    while True:
        print("\nCurrent state:", basket.state)
        print("Choose an option:")
        print("1: Add item")
        print("2: Remove item")
        print("3: Checkout")
        print("4: Confirm (OK)")
        print("5: Not OK (return to shopping)")
        print("6: Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            basket.add_item(item, price)
        elif choice == '2':
            item = input("Enter item name to remove: ")
            price = float(input("Enter item price: "))
            basket.remove_item(item, price)
        elif choice == '3':
            basket.checkout()
        elif choice == '4':
            basket.ok()
        elif choice == '5':
            basket.not_ok()
        elif choice == '6':
            print("Exiting test case generation.")
            break
        else:
            print("Invalid input, please try again.")

# Start the test case generation
generate_test_case()
