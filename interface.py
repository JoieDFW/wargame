def display_hand(hum, cpu):
    print("Your card is {}! Computer's card is {}!".format(hum, cpu))

def output(string="", wait=False, prompt=">>"):
    print(string, end="")
    if wait:
        input(prompt)
    
