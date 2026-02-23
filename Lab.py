phone_book ={
   "0568323222":"Amal",
   "0522222232":"Mohammed",
   "0532335983":"Khadijah",
   "0545341144":"Abdullah",
   "0545534556":"Rawan",
   "0560664566":"Faisal",
   "0567917077":"Layla"
}
def search_phone_number(phone_book:dict)->dict:
    user_input = input("Enter a phone number : ")
    if len(user_input) != 10 or not user_input.isdigit():
        print("This is invalid number.")    
    else:
        if user_input in phone_book:
                print(f'The name of the owner is {phone_book[user_input]}.')
        else: 
            print("Sorry, the number is not found.")
    return phone_book

search_phone_number(phone_book)