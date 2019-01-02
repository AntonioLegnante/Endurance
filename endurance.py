#Determinare la duranta massima di volo conoscendo la quantità di carburante espressa in Galloni e il consumo orario (Galloni/h) 
print ("Determina la durata massima di volo conoscendo la quantita di carbutante ed il consumo orario.") 
carburante=float (input ("carburante \t"))
consumo_orario= float (input("consumo orario \t"))   
if carburante<=0:
    print ("secondo te un aereo senza carburante può mai partire")
elif consumo_orario<=0:
     print ("arriverai a destinazione nel 20mai!")
else:
    temporanea = carburante / consumo_orario
    ore = int (temporanea)
    temporanea-= ore     
    temporanea*=60 
    minuti = int (temporanea)
    temporanea-=minuti
    temporanea*=60           
    secondi = int (temporanea)
    print ("la massima durata del volo possibile e' ", ore , "h" , minuti , "min" , secondi, "sec")


