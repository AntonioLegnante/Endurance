#Determinare la duranta massima di volo conoscendo la quantità di carburante espressa in Galloni e il consumo orario (Galloni/h)
print ("Determina la durata massima di volo conoscendo la quantita di carbutante ed il consumo orario.")
carburante=int (input ("carburante \t"))
if carburante<=0:
    print ("secondo te un aereo senza carburante può mai partire")
consumo_orario= int (input("consumo orario \t"))
if consumo_orario<=0:
    print ("secondo te gli aerei come volano?")
variabile_temporanea= carburante/consumo_orario
ore = int (variabile_temporanea)
variabile_temporanea=variabile_temporanea - ore
variabile_temporanea=variabile_temporanea*60
minuti = int (variabile_temporanea)
variabile_temporanea=variabile_temporanea - ore
variabile_temporanea=variabile_temporanea*60
secondi= int (variabile_temporanea)
print ("la massima durata del volo possibile e' ", ore , "h" , minuti , "min" , secondi, "sec")