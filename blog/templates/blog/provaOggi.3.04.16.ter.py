valore_utente = input("Scrivi qualcosa: ")
tipo_di_valore = ""
 # voglio scoprire il type di quello che ha scritto l'utente
try :
 	valore_utente = int (valore_utente)
 	tipo_di_valore = "intero"
except :
 	try : 
 		valore_utente = float(valore_utente)
 		tipo_di_valore = "virgola mobile"
 	except :
 		#valore utente e una string
 		tipo_di_valore = "string"

if tipo_di_valore == "intero" :
 	print("Hai scritto il numero %d", valore_utente)
elif tipo_di_valore == "float" :
 	print("Hai scritto il numero in virgola mobile %g", valore_utente)
else : #questa e una string
 	print("Hai scritto la parola o la frase %s", valore_utente)
