total = 0
balance = 0
again = True
cart = 0
pmoney = 0
tmoney = 0
amoney = 0
mmoney = 0
totalp = 0
totalt = 0
totala = 0
totalm = 0
newp = 0
newt = 0
newa = 0
newm = 0
while again == True:
	print("Welcome to the CS110 Supermarket! \n", "1. Potatoes ($0.25 per potato) \n", "2. Tomatoes ($1.25 per tomato) \n", "3. Apples ($0.75 per apple) \n", "4. Mangoes (1.75 per mango) \n", "5. Checkout")
	user = int(input("Please enter an option:"))
	if user == 1:
		p = int(input("How many potatos?"))
		while (p <= 0):
                        print("Please enter a valid number!")
                        p = int(input("How many potatos?"))
		pmoney = p * 0.25
		totalp += pmoney
		newp += p
		total = totalp + totalt + totala + totalm
		cart = newm + newa + newt + newp
		print("Your cost for", newp, "potatoes is $", pmoney, ".", "You have", cart, "items in your cart.", "Your total is now $", total)
	elif user == 2:
		t = int(input("How many tomatoes?"))
		while (t <= 0):
                        print("Please enter a valid number!")
                        t = int(input("How many tomatoes?"))
		tmoney = t * 1.25
		totalt += tmoney
		newt += t
		cart = newm + newa + newt + newp
		total = totalp + totalt + totala + totalm
		print("Your cost for", newt, "tomatoes is $", tmoney, ".", "You have", cart, "items in your cart.", "Your total is now $", total)
	elif user == 3: 
		a = int(input("How many apples?"))
		while (a <= 0):
                        print("Please enter a valid number!")
                        a = int(input("How many apples?"))
		amoney = a * 0.75
		totala += amoney
		newa += a
		total = totalp + totalt + totala + totalm
		cart = newm + newa + newt + newp
		print("Your cost for", newa, "apple is $", amoney, "You have", cart, "items in your cart.", "Your total is now $", total)
	elif user == 4:
		m = int(input("How many mangoes?"))
		while (m <= 0):
                        print("Please enter a valid number!")
                        m = int(input("How many mangoes?"))
		mmoney = m * 1.75
		totalm += mmoney
		newm += m
		total = totalp + totalt + totala + totalm
		cart = newm + newa + newt + newp
		print("Your cost for", newm, "mangoes is $", mmoney, "You have", cart, "items in your cart.", "Your total is now $", total)
	elif user == 5:
		again = False
		cart = newm + newa + newt + newp
		total = totalp + totalt + totala + totalm
		print("You have", cart, "items in your cart. Your total would be $", total)
		userpay = float(input("Please enter the amount of money you are paying for:"))
		while (userpay < total):
                        print("Your payment is not enough!")
                        userpay = float(input("Please enter the amount of money you are paying for:"))
	else:
		print("Sorry, that was an invalid choice. Please try again.")
change = userpay - total
five = change / 5
lfive = change % 5
one = lfive / 1
lone = lfive % 1
quarter = lone / 0.25
lquarter = lone % 0.25
dime = lquarter / 0.1
ldime = lquarter % 0.1
nickle = ldime / 0.05
lnickle = ldime % 0.05
penny = lnickle / 0.01
lpenny = lnickle % 0.01
print("Change is $", change, ".", "Give the customer", int(five), "$5 bill", int(one), "$1 bill", int(quarter), "quarter", int(dime), "dime", int(nickle), "nickle", int(lpenny), "penny" )
