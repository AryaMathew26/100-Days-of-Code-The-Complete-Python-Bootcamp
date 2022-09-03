#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill=float(input("What was the total bill?\n"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people=int(input("How many people to split the bill?\n"))
share=(bill/people)*(1+tip/100)
#1
rounded_share=round(share,2)
#2
rounded_share="{:.2f}".format(share)
print(f"Each person should pay {rounded_share}")
