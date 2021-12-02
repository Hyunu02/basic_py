hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# calculate total price
for i in prices:
  total_price += i

average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

# discount all hairstyles prices by R$ 5 
new_prices = [num - 5 for num in prices]
print(new_prices)

# calculate total and average revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(total_revenue)
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# create a list where there is just hairstyles which each price of them is under R$30!
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)