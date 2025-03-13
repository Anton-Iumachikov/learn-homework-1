def strings(one, two):
    if not isinstance(one, str) or not isinstance(two, str):
        return '0'
    elif len(one) == len(two):
        return '1' 
    elif len(one) > len(two):
        return '2'
    elif len(one) != len(two) and two == 'learn':
        return '3'
def main(): #не до конца понял это
    one = input("Введите первую строку:")
    two = input("Введите вторую строку:")
    score = strings(one, two)  
    print(score)
if __name__ == "__main__": #не до конца понял это
    main() #не до конца понял это
