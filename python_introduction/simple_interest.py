def simple_interest(principal, rate_percent, time_years):
   rate = rate_percent/100.0
   interest = principal * rate * time_years
   total = principal + interest
   return interest, total 
if __name__ == "__main__":   
   p = float(input("principal: "))
   r = float(input("Annual rate (%): "))
   t = float(input("Time (years): "))
   i, total = simple_interest(p, r, t)
   print(f"Interest: {i : . 2f}")
   print(f"Total amount : {total:.2f}")
