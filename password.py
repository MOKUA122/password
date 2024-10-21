import random
import string
import time

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_access_time(amount):
    """Return the access time based on the amount paid."""
    if amount == 10:
        return 2 * 60 
    elif amount == 40:
        return 6 * 60  
    elif amount == 50:
        return 24 * 60  
    elif amount == 150:
        return 7 * 24 * 60  
    elif amount == 450:
        return 30 * 24 * 60  
    else:
        return 0  

def start_timer(minutes):
    """Run a timer for the given number of minutes."""
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"Time remaining: {timer}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\nTime is up! The WiFi access has expired.")

def main():
    """Main program to generate password and start timer."""
    # Get user details
    phone_number = input("Enter your phone number: ")
    try:
        amount_paid = int(input("Enter the amount you want to pay: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    
    mpesa_pin = input("Enter your M-Pesa PIN : ")

    total_minutes = get_access_time(amount_paid)

    if total_minutes == 0:
        print("Invalid payment amount. Please choose one of the valid amounts: 10, 40, 50, 150, or 450 KSH.")
        return

    
    password = generate_password()

    
    print(f"Generated WiFi password: {password}")
    print(f"WiFi access granted for {total_minutes} minutes.")

     
    start_timer(total_minutes)

if __name__ == "__main__":
    main() 