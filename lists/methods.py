# using .append() and .remove() methods
# .remove() starts removing from 0 to higher index

orders = ["periwinkle", "daisies", "periwinkle"]
orders.append('tulips')
orders.append('roses')
print(orders)
orders.remove('periwinkle')
print(orders)

# growing a list/concatenation --> Plus (+)

new_orders = ["lilac", "iris"]
print(new_orders)
combined_orders = orders + new_orders
print(combined_orders)