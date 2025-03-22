
def to_roman(val : int) -> str:
    #{"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    roman_key_list = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman_value_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    final_list = []
    loop = 0
    while val > 0:
        if val >= roman_value_list[loop]:
            val -= roman_value_list[loop]
            final_list.append(roman_key_list[loop])
        else: loop += 1  
        if loop == 13:
            break
    return "".join(final_list)

def from_roman(roman_num : str) -> int:
    roman_key_list = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman_value_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_double_key_list = ["CM","CD","XC","XL","IX","IV"]
    roman_double_value_list = [900,400,90,40,9,4]
    roman_list = list(roman_num)
    final = 0
    loop = 0
    while len(roman_list) > 0:
        if len(roman_list) >= 2 and "".join([roman_list[loop],roman_list[loop+1]]) in roman_double_key_list:
            temp_str = "".join([roman_list[loop],roman_list[loop+1]])
            final += roman_double_value_list[roman_double_key_list.index(temp_str)]
            roman_list.pop(0)
            roman_list.pop(0)
        else:
            final += roman_value_list[roman_key_list.index(roman_list[loop])]
            roman_list.pop(0)       
    return final

if __name__ == "__main__":
    while True:
        choice = int(input("1 --> integer to roman\n2 --> roman to integer\n3 --> exit\n"))
        if choice == 1:
            x = int(input("integer : \n"))
            print(to_roman(x))
        if choice == 2:
            x = input("roman : \n")
            print(from_roman(x))
        elif choice == 3:
            break
        else:
            print("invalid choice")