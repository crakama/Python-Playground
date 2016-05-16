"""
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
Print , where  totalCost is the rounded integer result of the entire bill ( with added tax and tip).

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
mealcost_ = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

def mealCost(mealcost_, tipPercent,taxPercent):
    tip = mealcost_ * (tipPercent)/100
    tax = mealcost_ * (taxPercent)/100
    totalCost = int(round(mealcost_ + tax + tip))
    print "The total meal cost is {} dollars.".format(totalCost)

mealCost(mealcost_,tipPercent,taxPercent)
