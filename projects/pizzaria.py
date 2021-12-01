# set toppings
topping = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# set prices
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(topping)
print("We sell {} different kinds of pizza!\n".format(num_pizzas))

# make 2d list with prices and toppings
pizza_and_prices = [[prices[0], topping[0]], [prices[1], topping[1]], 
[prices[2], topping[2]], [prices[3], topping[3]], 
[prices[4], topping[4]], [prices[5], topping[5]], 
[prices[6], topping[6]]]

print(pizza_and_prices, "\n")
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# remove the priciest
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices, "\n")

# derive three_cheapest from integral catalog
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)