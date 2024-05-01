#By Jordan Faulkner, 5-1-2024
#Practicing coding functions to solve math and physics problems involving mass,acceleration,and distance

#Define the variables 
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
#function to turn fahrenheit in to celsius 
def f_to_c(f_temp):
  c_temp = round((f_temp-32)*(5/9),1)
  return c_temp
#Testing that function 
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
#Function to turn celcius into fahrenheit 
def c_to_f(c_temp):
  f_temp = c_temp*(9/5)+32
  return f_temp
#testing that function 
c0_in_fahrenheit=c_to_f(0)
print(c0_in_fahrenheit)
#write a function to get the force of mass and acceleration measurements 
def get_force(mass,acceleration):
  return mass*acceleration
print(f'The GE train supplies {get_force(train_mass,train_acceleration)} Newtons of force.')
#write a function to get the energy 
def get_energy(mass,c=3*10**8):
  return (mass*c)**2
bomb_energy = get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules')
#write a function to get the work of 3 measurements 
def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration)
  return force*distance 
train_work = get_work(train_mass,train_acceleration,train_distance)
print(f'The GE train does {train_work} Joules of work over {train_distance} meters')

