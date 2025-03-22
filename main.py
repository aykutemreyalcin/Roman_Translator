
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

