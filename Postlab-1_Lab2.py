userpin = input (" enter a 4 digit pin")
def verify_pin(pin):
    if pin== userpin:
        return True
    else:
        return false
    def log_in():
        print("Police arrest you if you had 3 successive failure")
        tries = 0
        while tries < 3:
            pin = input("Enter you 4 digit pin:")
            if verify_pin(pin):
                print ("Accepted")
