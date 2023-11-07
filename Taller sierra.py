#ejer 1
# Elaborado por:Ivan david galeano, nicole camila hoyos, juan jose guzman camacho, Jerson stiven gonzalez.
import random
first_add = 987
last_add = 5674
number = random.randint(10000, 99999)
firt_three_digits = ""
last_two_digits = ""
def datta():
    global firt_three_digits,last_two_digits, number
    number = random.randint(10000, 99999)
    f_number_str = str(number)
    firt_three_digits = f_number_str[:3]
    last_two_digits = f_number_str[-2:]

#for que añada los tre primeros numeros a la lista
def f_addittion():
    global first_add
    first_add = 0
    for digit in firt_three_digits:
        first_add += int(digit)
        print(first_add)

def l_addittion():
    global last_add
    last_add = 0
    for digit in last_two_digits:
        last_add += int(digit)
        print(last_add)

if __name__=="__main__":
    while last_add != first_add:
        datta()
        f_addittion()
        l_addittion()
        

print(f"El numero: {number} cumple las condiciones"
        f"Los primeros 3 digitos son: {firt_three_digits}"
        f"Sumados serían: {first_add}"
        f"Los ultimos 2 digitos son: {last_two_digits}"
        f"Sumados serían: {last_add}")
   
    
