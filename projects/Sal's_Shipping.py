weight = 7.5

# GROUND SHIPPING

if weight <= 2:
  cost = weight * 1.5 + 20
elif weight <= 6:
  cost = weight * 3.0 + 20
elif weight <= 10:
  cost = weight * 4.0 + 20
else:
  cost = weight * 4.75 + 20
g_cost = cost
print('Ground shipping cost: {}'.format(cost))

# GROUND SHIPPING PREMINUM

cost = 125
gp_cost = cost
print('Ground shipping premium cost: {}'.format(cost))

# DRONE SHIPPING

if weight <= 2:
  cost = weight * 4.5
elif weight <= 6:
  cost = weight * 9.0
elif weight <= 10:
  cost = weight * 12.0
else:
  cost = weight * 14.25
d_cost = cost
print('Drone shipping cost: {}\n'.format(cost))

print("The smallest cost is: {}".format(min(g_cost, gp_cost, d_cost)))