def discounted(price, discount, max_discount=20):
    try:   
        price, discount, max_discount= float(price), float(discount), int(max_discount) 
        return price - (price * discount / 100)
    except (ValueError, TypeError):
        print("Ошибка")
        
   
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))