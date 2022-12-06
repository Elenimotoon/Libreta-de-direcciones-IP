import xlsxwriter
from time import sleep
import shutil 

lista1 = [('asda','sxds','dasd','asd',), ('ksa','jfkd','sajfa','dsfk','dsf',)]




def Crear_excel (lista) :
    archivo=xlsxwriter.Workbook('directorio-ip.xlsx')
    hoja=archivo.add_worksheet()
    for i in range(len(lista)):
        fila = list (lista[i])
        for c in range(len(fila)):
            hoja.write(i, c, fila[c])
    archivo.close()
    
    sleep(10)
    shutil.move ('directorio-ip.xlsx', "C:/Users/Public/Documents")
    

Crear_excel(lista1)