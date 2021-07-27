
def get_my_list(lista_compleja):
    
  if type(lista_compleja) != list:
    print("El parámetro requerido es una lista o arreglo de datos")
  else:
    for index in range(0, len(lista_compleja)-1):
     if type(lista_compleja[index]) == list:
      output_list = lista_compleja[index]
      
  return output_list
  
