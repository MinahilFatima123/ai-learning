#Variables, data types, operators, control structures
students={"Ahmed": 85,"Sara": 92, "Ali": 60,"Fatima": 78, "Umar": 45,}
fail_count=0;
for name, score in students.items():
    if score >= 90:
      print(f"{name}: A grade");
    elif score>= 80:
      print(f"{name}: B grade");
    elif score>= 70:
      print(f"{name}: C grade");
    elif score>= 60:
      print(f"{name}: D grade");
    else:
      print(f"{name}: Failing");
      fail_count+=1
      
      
print(f"Total failing: {fail_count}");

#Functions
def calculate_discount(price,discount_percent):
    return int(price-(price*discount_percent/100));

def print_receipt(name,final_price):
    print(f"{name} your final price is {final_price}")


print_receipt("Minahil",calculate_discount(1000,15))



#Classes and OOP




















































