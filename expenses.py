from states_tax_rates import all_states
from calculations import *

def asking_pay():
  if(type_of_pay == "hourly"):
    #ask state in order to calculate the state income tax
    state = input("What state do you live in (enter 'dc' if in District of Columbia? ")
    hourly_bef_tax = int(input("What's your hourly wage? "))
    #calculate their wage after income tax
    real_hourly = hourly_bef_tax - (hourly_bef_tax*all_states[state])
    #calculate the real monthly salary after income tax
    global salary
    salary =real_hourly*8*30.417
    print("Monthly pay after tax: " + str(salary))
  elif(type_of_pay == "annually"):
    #ask state to calculate state income tax
    state = input("What state do you live in (enter 'dc' if in District of Columbia? ")
    annually = int(input("What's your annual salary? "))
    #calculate the real monthly salary after income tax
    real_annually = annually - (annually*all_states[state])
    salary = real_annually/12
    #display the monthly salary after income tax
    print("Monthly pay after tax: " + str(salary))

#ask user how often they get paid
type_of_pay = input("Does your job pay you 'hourly' or 'annually'? ")

#list of expenses which we later ask user to rank
expenses = ["food", "entertainment", "education", "health", "leisure", "utilities", "transportation", "savings", "other"]

#the income tax rates of all states in the United States

salary = 0.0
real_annually = 0
hourly_bef_tax = 0
real_hourly = 0
state = ' '
#if statement to ask how much they get paid and how often


asking_pay()
#declaring the variables for which the user will rank
item1 = ""
item2 = ""
item3 = ""
item4 = ""
item5 = ""
item6 = ""
item7 = ""
item8 = ""
item9 = ""

answer = True
#loop to rank the users priorities
while(answer):
  print("\n\n_________________________________________ \n\n")
  print("Rank these categories based on importance: \n" )
  print(expenses)
  #asking user to rank the expenses
  item1 = input()
  item2 = input()
  item3 = input()
  item4 = input()
  item5 = input()
  item6 = input()
  item7 = input()
  item8 = input()
  item9 = input()

  item_list = [item1, item2, item3, item4, item5, item6, item7, item8, item9]
  print("\n")
  for i in range(len(expenses)):
    print(str(i + 1) + ": " + item_list[i])
  yon = input("\nIs this correct? ")
  if(yon == "yes"):
    answer = False



#rerank their priorities based on what we expect to be more costly than the other
priority1 = ""
priority2 = ""
priority3 = ""
priority4 = ""
priority5 = ""
priority6 = ""
priority7 = ""
priority8 = ""
priority9 = ""
#top3: health, savings, education
top_list = [priority1, priority2, priority3]
#middle3: food, utilities, transportation
middle_list = [priority4, priority5, priority6]
#bottom3: entertainment, leisure, other
bottom_list = [priority7, priority8, priority9]





#education: are you in college? how much debt do you have? 
#setting variables for false which we will later use

s_important = False
h_important = False
edu_important = False

f_important = False
u_important = False
t_important = False

e_important = False
l_important = False
o_important = False

#education
edu_debt = 0
in_college = input("\n\n_________________________________________\n\nAre you in college? ")
if(in_college == "yes"):
  edu_debt = int(input("How much debt do you have? "))
  if(edu_debt > (salary*.5)):
    edu_important = True

#savings
savings_amt = float(input("How much do you have in your savings account? "))
time = int(input("How many months you been saving? "))
if(savings_amt<((salary*12)*.25) or time<6):
  s_important = True

#health
health = int(input("How much per month do you pay for health insurance? "))
if(health > (salary*.1)):
  h_important = True

print("\n\n_________________________________________\n\n")

edu=-1
s=-1
h=-1



for i in range(9):
  if(item_list[i] == "education"):
    edu = i
  if(item_list[i] == "savings"):
    s = i
  if(item_list[i] == "health"):
    h = i

#if only one of the categories in the top 3 is important, then make the priority list based off that
if(s_important and not h_important and not edu_important):
  priority1 = "savings"
  if(h<edu):
    priority2 = "health"
    priority3 = "education"
  elif(edu<h):
    priority2 = "education"
    priority3 = "health"
if(h_important and not s_important and not edu_important):
  priority1 = "health"
  if(s<edu):
    priority2 = "savings"
    priority3 = "education"
  else:
    priority2 = "education"
    priority3 = "savings"

if(edu_important and not h_important and not s_important):
  priority1 = "education"
  if(h<s):
    priority2 = "health"
    priority3 = "savings"
  else:
    priority2 = "savings"
    priority3 = "health"

#if all of them are true, look off their original rankings and make priority ranking based off that

if(s_important and h_important and edu_important):
  if(s<h and s<edu):
    priority1 = "savings"
    if(h<edu):
      priority2 = "health"
      priority3 = "education"
    else:
      priority2 = "education" 
      priority3 = "health"
  elif(h<s and h<edu):
    priority1 = "health"
    if(s<edu):
      priority2 = "savings"
      priority3 = "education"
    else:
      priority2 = "education"
      priority3 = "savings"
  elif(edu<s and edu<h):
    priority1 = "education"
    if(s<h):
      priority2 = "savings"
      priority3 = "health"
    else:
      priority2 = "health"
      priority3 = "savings"

if(not s_important and not h_important and not edu_important):
  if(s<h and s<edu):
    priority1 = "savings"
    if(h<edu):
      priority2 = "health"
      priority3 = "education"
    else:
      priority2 = "education" 
      priority3 = "health"
  elif(h<s and h<edu):
    priority1 = "health"
    if(s<edu):
      priority2 = "savings"
      priority3 = "education"
    else:
      priority2 = "education"
      priority3 = "savings"
  elif(edu<s and edu<h):
    priority1 = "education"
    if(s<h):
      priority2 = "savings"
      priority3 = "health"
    else:
      priority2 = "health"
      priority3 = "savings"

#if two of the categories are important, look off their original rankings and make priority ranking based off that
if(s_important and h_important and not edu_important):
  if(s<h):
    priority1 = "savings"
    priority2 = "health"
    priority3 = "education"
  elif(h<s):
    priority1 = "health"
    priority2 = "savings"
    priority3 = "education"

if(s_important and edu_important and not h_important):
  if(s<edu):
    priority1 = "savings"
    priority2 = "education"
    priority3 = "health"
  if(edu<s):
    priority1 = "education"
    priority2 = "savings"
    priority3 = "health"


if(not s_important and edu_important and h_important):
  if(edu<h):
    priority1 = "education"
    priority2 = "health"
    priority3 = "savings"
  elif(h<edu):
    priority1 = "health"
    priority2 = "education"
    priority3 = "savings"

top_list = [priority1, priority2, priority3]




#starting the middle list (food, transportation, utilities)
eat_out = int(input("On average many times do you eat out per week? "))
if(eat_out*4.345 > 6):
  f_important = True

drive = input("Do you drive a vehicle? ")
if(drive == "yes"):
  gas = int(input("Approximately how much does it cost to fill up a full gas tank? "))
  if(gas > 60):
    t_important = True
elif(drive == "no"):
  public = int(input("Approximately how much per week do you spend on transportation? "))
  if(public > 30):
    t_important = True

utility_cost = int(input("How much do your utilities total out to per month? "))
if(utility_cost > .3*salary):
  u_important = True




f=-1
u=-1
t=-1

for i in range(9):
  if(item_list[i] == "food"):
    f = i
  if(item_list[i] == "utilities"):
    u = i
  if(item_list[i] == "transportation"):
    t = i



if(f_important and not u_important and not t_important):
  priority4 = "food"
  if(u<t):
    priority5 = "utilities"
    priority6 = "transportation"
  elif(t<u):
    priority5 = "transportation"
    priority6 = "utilities"
if(u_important and not f_important and not t_important):
  priority4 = "utilities"
  if(f<t):
    priority5 = "food"
    priority6 = "transportation"
  else:
    priority5 = "transportation"
    priority6 = "food"

if(t_important and not u_important and not f_important):
  priority4 = "transportation"
  if(u<f):
    priority5 = "utilities"
    priority6 = "food"
  else:
    priority5 = "food"
    priority6 = "utilities"



#copy pasted from top list (change to match middle list)
if(f_important and u_important and t_important):
  if(f<u and f<t):
    priority4 = "food"
    if(u<t):
      priority5 = "utilities"
      priority6 = "transportation"
    else:
      priority5 = "transportation" 
      priority6 = "utilities"
  elif(u<f and u<t):
    priority4 = "utilities"
    if(s<edu):
      priority5 = "food"
      priority6 = "transportation"
    else:
      priority5 = "transportation"
      priority6 = "food"
  elif(t<f and t<u):
    priority4 = "transportation"
    if(f<u):
      priority5 = "food"
      priority6 = "utilities"
    else:
      priority5 = "utilities"
      priority6 = "food"

#if all of them are false, look off their original rankings and make priority ranking based off that
if(not f_important and not u_important and not t_important):
  if(f<u and f<t):
    priority4 = "food"
    if(u<t):
      priority5 = "utilities"
      priority6 = "transportation"
    else:
      priority5 = "transportation" 
      priority6 = "utilities"
  elif(u<f and u<t):
    priority4 = "utilities"
    if(s<edu):
      priority5 = "food"
      priority6 = "transportation"
    else:
      priority5 = "transportation"
      priority6 = "food"
  elif(t<f and t<u):
    priority4 = "transportation"
    if(f<u):
      priority5 = "food"
      priority6 = "utilities"
    else:
      priority5 = "utilities"
      priority6 = "food"

#if two of the categories are important, look off their original middle 3 rankings and make priority ranking based off that
if(f_important and u_important and not t_important):
  if(f<u):
    priority4 = "food"
    priority5 = "utilities"
    priority6 = "transportation"
  elif(u<f):
    priority4 = "utilities"
    priority5 = "food"
    priority6 = "transportation"

if(f_important and t_important and not u_important):
  if(f<t):
    priority4 = "food"
    priority5 = "transportation"
    priority6 = "utilities"
  if(t<f):
    priority4 = "transportation"
    priority5 = "food"
    priority6 = "utilities"

if(not f_important and t_important and u_important):
  if(t<u):
    priority4 = "transportation"
    priority5 = "utilities"
    priority6 = "food"
  elif(u<t):
    priority4 = "utilities"
    priority5 = "transportation"
    priority6 = "food"

middle_list = [priority4, priority5, priority6]


e=-1
l=-1
o=-1

for i in range(9):
  if(item_list[i] == "entertainment"):
    e = i
  if(item_list[i] == "leisure"):
    l = i
  if(item_list[i] == "other"):
    o = i

#if only one of the categories in the top 3 is important, then make the priority list based off that
if(l_important and not o_important and not e_important):
  priority7 = "leisure"
  if(o<e):
    priority8 = "other"
    priority9 = "entertainment"
  else:
    priority8 = "entertainment"
    priority9 = "other"
if(o_important and not l_important and not e_important):
  priority7 = "other"
  if(l<e):
    priority8 = "leisure"
    priority9 = "entertainment"
  else:
    priority8 = "entertainment"
    priority9 = "leisure"

if(e_important and not o_important and not l_important):
  priority7 = "entertainment"
  if(o<l):
    priority8 = "other"
    priority9 = "leisure"
  else:
    priority8 = "leisure"
    priority9 = "other"

#if all of them are true, look off their original rankings and make priority ranking based off that

if(l_important and o_important and e_important):
  if(l<h and l<edu):
    priority7 = "leisure"
    if(o<e):
      priority8 = "other"
      priority9 = "entertainment"
    else:
      priority8 = "entertainment" 
      priority9 = "other"
  elif(o<l and o<e):
    priority7 = "other"
    if(l<e):
      priority8 = "leisure"
      priority9 = "entertainment"
    else:
      priority8 = "entertainment"
      priority9 = "leisure"
  elif(e<l and e<h):
    priority7 = "entertainment"
    if(l<o):
      priority8 = "leisure"
      priority9 = "other"
    else:
      priority8 = "other"
      priority9 = "leisure"

#if all of them are false, look off their original rankings and make priority ranking based off that
if(not l_important and not o_important and not e_important):
  if(l<h and l<edu):
    priority7 = "leisure"
    if(o<e):
      priority8 = "other"
      priority9 = "entertainment"
    else:
      priority8 = "entertainment" 
      priority9 = "other"
  elif(o<l and o<e):
    priority7 = "other"
    if(l<e):
      priority8 = "leisure"
      priority9 = "entertainment"
    else:
      priority8 = "entertainment"
      priority9 = "leisure"
  elif(e<l and e<h):
    priority7 = "entertainment"
    if(l<o):
      priority8 = "leisure"
      priority9 = "other"
    else:
      priority8 = "other"
      priority9 = "leisure"

#if two of the categories are important, look off their original rankings and make priority ranking based off that
if(l_important and o_important and not e_important):
  if(l<o):
    priority7 = "leisure"
    priority8 = "other"
    priority9 = "entertainment"
  elif(o<s):
    priority7 = "other"
    priority8 = "leisure"
    priority9 = "entertainment"

if(l_important and e_important and not o_important):
  if(l<e):
    priority7 = "leisure"
    priority8 = "entertainment"
    priority9 = "other"
  if(e<l):
    priority7 = "entertainment"
    priority8 = "leisure"
    priority9 = "other"

if(not l_important and e_important and o_important):
  if(e<o):
    priority7 = "entertainment"
    priority8 = "other"
    priority9 = "leisure"
  elif(o<e):
    priority7 = "other"
    priority8 = "entertainment"
    priority9 = "leisure"

bottom_list = [priority7, priority8, priority9]

#base proportions of each expense
money = salary-utility_cost

print("\n\n_____________________\n\n We are going to divide your monthly salary both based off of your priorities and based off what requires more financial attention.\n\n_____________________\n\n")
print("Based off your priorities and responses here is your recommended spending plan for each category:\n\n{}: ${}".format(priority1, round(prop_item1*money, 2)))

invis_num = 0
print("\n{}: ${}".format(priority2, round(prop_item2*money, 2)))
print("\n{}: ${}".format(priority3, round(prop_item3*money, 2)))
if(priority4 != "utilities"):
  print("\n{}: ${}".format(priority4, round(prop_item4*money, 2)))
else:
  print("\n{}: ${}".format(priority4, utility_cost))
  invis_num = prop_item4*money
if(priority5 != "utilities"):
  print("\n{}: ${}".format(priority5, round(prop_item5*money, 2)))
else:
  print("\n{}: ${}".format(priority5, utility_cost))
  invis_num = prop_item5*money
if(priority6 != "utilities"):
  print("\n{}: ${}".format(priority6, round(prop_item6*money, 2)))
else:
  print("\n{}: ${}".format(priority6, utility_cost))
  invis_num = prop_item6*money
print("\n{}: ${}".format(priority7, round(prop_item7*money, 2)))
print("\n{}: ${}".format(priority8, round(prop_item8*money, 2)))
print("\n{}: ${}".format(priority9, round(prop_item9*money, 2)))
print("\n\n_____________________\n\nYou have a total of: ${} left over. {}".format(round(invis_num, 2), "You should take your wife out to a nice steak dinner!"))


