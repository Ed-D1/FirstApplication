import main.py

bills = []

print("Add in the name of your bill followed by the cost, when done enter Q\n")
endloop = 'H'
name = ""
cost = 0
while(endloop != 'Q'):
    bills.append(main.Bill(name, cost))
