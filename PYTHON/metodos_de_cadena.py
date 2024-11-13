print("estar".capitalize())
print("esTAr".capitalize())

print("["+"Jankito".center(12)+"]")
print("["+"Jankito".center(12,"*")+"]")

t = "zeta"
print(t.endswith("a")) #true
print(t.endswith("A")) #false

print("omega".startswith("meg"))
print("omega".startswith("om"))

print("Eta".find("ta")) #1
print("Eta".find("mma")) #-1 porque no arroja error y no existe la primera letra q es m

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())

print("Moooo".isalpha())
print('Mu40'.isalpha())

print('2018'.isdigit())
print("Year2019".isdigit())

print("Moooo".islower())
print('moooo'.islower())

print(" ".isspace())
print("mooo mooo mooo".isspace())

print('moooo'.isupper())
print('MOOOO'.isupper())

print(",".join(["omicron", "pi", "rho"])) #devuelve una cadena

print("SiGmA=60".lower()) # devuelve una cadena todo en minúcula

print("[" + " tau ".lstrip() + "]") #elimina los espacios en blanco iniciales

print("www.cisco.com".lstrip("w.")) #elimina los caracteres pasados como parámetro que se encuentren al inicio de la cadena 

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) #reemplaza el primer argumento por lo indicado en el segundo argumento
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("This is it!".replace("is", "are", 1)) #el tercer argumento indica la cantidad de veces que se va a reemplazar
print("This is it!".replace("is", "are", 2))

print("phi       chi\npsi".split()) #este método retorna una lista