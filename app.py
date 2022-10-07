import ramdon
import time
def lucky_color():
    options = [ "azul","amarillo","rojo","lila","rosa","morado"]
    print("tu color de la suerte es :"options)
    time.eleep(3)
    


print("bienvenido a tu horoscopo")
def menu():

    print("##########")
    print("selecciona el numero correspondiente")
    print("1","aquarius")
    print("2","aries")
    print("3","cancer")
    print("4","capricornus")
    print("5","gemini")
    print("6","leo")
    print("7","libra")
    print("8","pisces")
    print("9","sagittarius")
    print("10","scorpio")
    print("11","taurus")
    print("12","virgo")
    print("color de la suerte")
    print("0","salir")
    print("#############")

def read_file(app):

    file = open("signs/"+ app,"r",encoding="UTF-8")
    for line in file:
        print(line)

user_input = ""

while user_input != "exit":
    menu()

    user_input = input()
    if user_input == "1":
       read_file("aquarius.txt")
    elif user_input == "2":
        read_file("aries txt")   
    elif user_input == "3":
        read_file("cancer.txt")
    elif user_input == "4":
        read_file("capricornus.txt")
    elif user_input == "5":
        read_file("geminis.txt")
    elif user_input == "6":
        read_file("leo.txt")
    elif user_input == "7":
        read_file("libra.txt")
    elif user_input == "8":
        read_file("pices.txt")
    elif user_input == "9":
        read_file("sagitario.txt")
    elif user_input == "10":
        read_file("scorpio.txt")
    elif user_input == "11":
        read_file("taurus.txt")      
    elif user_input == "12":
        read_file("virgo.txt")
    elif user_input == "13":

    elif user_input == "exit":
        print("hasta luego")
        exit()
    else: 
        print("opcion incorrecta")

    
        


    
    
         
