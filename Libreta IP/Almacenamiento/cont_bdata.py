import sqlite3 as sq


def crearBD():
    conec = sq.connect('pcbd.db')
    print ('se entro a la base de datos')
    conec.commit()
    conec.close()
    

def crear_tabla():
    conec = sq.connect ('pcbd.db')
    cursor = conec.cursor ()
    cursor.execute("""CREATE TABLE pcbd (
                    equipos text,
                    ipv4 text,
                    ipv6 text,
                    macc text,
                    usuario text,
                    tipo text
                    )""")
    print ('se crearon las colimnas')
    conec.commit()
    conec.close()


def ins_datos(equipos, ipv4, ipv6, macc, usuario, tipo,):
    conec = sq.connect ('pcbd.db')
    cursor = conec.cursor ()
    instr = f"INSERT INTO pcbd VALUES ('{equipos}', '{ipv4}', '{ipv6}', '{macc}', '{usuario}', '{tipo}')"
    cursor.execute(instr)
    print ('se agregaron datos las colimnas')
    conec.commit()
    conec.close()

def leer_datos():
    conec = sq.connect ('pcbd.db')
    cursor = conec.cursor ()
    instr = f"SELECT * FROM pcbd"
    cursor.execute(instr)
    datos = cursor.fetchall()
    print ('se agregaron datos las colimnas')
    conec.commit()
    conec.close()
    print (datos)
    return datos

    
def eliminar_filas (equipo):
    conec = sq.connect('pcbd.db')
    cursor = conec.cursor()
    instruc = f"DELETE FROM pcbd WHERE equipos= '{equipo}'"
    print ('se a borrado estos datos')
    cursor.execute(instruc)
    conec.commit()
    conec.close()

def editar_datos (equipos, ipv4, ipv6, macc, usuario, tipo):
    conec = sq.connect('pcbd.db')
    cursor = conec.cursor()
    instruc = f"INSERT INTO pcbd VALUES ('{equipos}', '{ipv4}', '{ipv6}', '{macc}', '{usuario}', '{tipo}')"
    cursor.execute(instruc)
    conec.commit()
    conec.close()

    
if __name__ == '__main__':
    leer_datos()
