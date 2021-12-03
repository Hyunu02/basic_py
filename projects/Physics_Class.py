train_mass = 22680
train_acceleration = 10
c = 3*10**8
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies {} Newtowns of force.\n".format(train_force))

def get_energy(mass, c):
  return mass * c**2

bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies {} Joules.\n".format(bomb_energy))

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))