def hello_user():
   while True:
    hello_user = input("Как дела?")
    if hello_user == 'Хорошо':
        break
  except KeyboardInterrupt:
    print("Пока!")
    break
    
if __name__ == "__main__":
    hello_user()