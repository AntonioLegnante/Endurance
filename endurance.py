#Determinare la duranta massima di volo conoscendo la quantità di carburante espressa in Galloni e il consumo orario (Galloni/h) 
#Soluzione alternativa che dovrebbe funzionare ma...
print ("Determina la durata massima di volo conoscendo la quantita di carbutante ed il consumo orario.") 
carburante=float (input ("carburante \t"))
consumo_orario= float (input("consumo orario \t"))   
if carburante<=0:
    print ("secondo te un aereo senza carburante può mai partire")
elif consumo_orario<=0:
     print ("arriverai a destinazione nel 20mai!")
else:
    ore = int (carburante / consumo_orario)
    carburante = carburante % consumo_orario           #modifichiamo il valore di carburante 
    minuti = int (carburante / consumo_orario*60)
    carburante= carburante % consumo_orario            #modifichiamo il valore di carburante
    secondi = int (carburante / consumo_orario*60)
    print ("la massima durata del volo possibile e' ", ore , "h" , minuti , "min" , secondi, "sec")
#problema: nonostante ci siano i simboli di assegnazione è come se il programma non tenesse conto della prima modifica e pertanto  esegua 2 volte le stesse istruzioni
#ps: ingrippo