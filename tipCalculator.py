def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    friends = int(input("How many friends were at the restaurant together :"))
    eachPersonPay = (dollars + tip)/friends
    print(f"Each Friend Must Pay : ${eachPersonPay:.2f}")


def dollars_to_float(d):
    # TODO
    d = float(d.replace("$", "")) // 1
    return d
  
    


def percent_to_float(p):
    # TODO
    p = (float(p.replace("%", ""))/1)/100
    return p
    


main() 
