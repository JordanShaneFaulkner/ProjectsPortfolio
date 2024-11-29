#By Jordan Faulkner 
#5/1/2024

#Make a list of hairstyles, prices for those hairstyles, and how many times each of those hairstyles were given last week, all in seperate lists 
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
#Get the avaerage price for haircuts 
for price in prices:
  total_price+=price
average_price = round(total_price/len(prices),2)
print(average_price)
#decrease the original cost of haircuts by 5 and make a new price list 
new_prices = [price-5 for price in prices]
print(new_prices)

#find the total revenue
total_revenue = 0
for i in range(0,len(hairstyles)):
  total_revenue += prices[i]
  total_revenue += last_week[i]
print(total_revenue)
#Find the average daily rev
average_daily_revenue = round(total_revenue/7,2)
print(average_daily_revenue)
#Find the haircuts that cost under 30
cuts_under_30 = [hairstyles[i] for i in range(0,len(new_prices)-1) if new_prices[i]<30]
print(cuts_under_30)