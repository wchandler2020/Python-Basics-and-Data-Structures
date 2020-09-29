try: 
    with open("exceptions.py") as file:
        print("file opened")  
         
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age. ")


print("program continues. ")
