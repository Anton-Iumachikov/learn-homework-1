
def people_age(age):
    if age < 7:
        return 'Детский сад'
    elif age >= 7 and age < 18:
        return 'Школа' 
    elif age >= 18 and age < 22:
        return 'ВУЗ'
    elif age >= 22:
        return 'работа'
def main(): #не до конца понял это
    age = int(input("Введите ваш возраст: "))
    activity  = people_age(age)  
    print(activity )
if __name__ == "__main__": #не до конца понял это
    main() #не до конца понял это