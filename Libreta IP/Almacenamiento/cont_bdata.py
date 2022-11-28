import sqlite3 as sq

# Prueben como les funcione. Yo es que tengo un problema con las direcciones relativas 😅
ruta = '.\\Libreta IP\\Almacenamiento\\pcbd.db'

def crearBD():
    conec = sq.connect(ruta)
    print('se entro a la base de datos')
    conec.commit()
    conec.close()

def crear_tabla():
    conec = sq.connect(ruta)
    cursor = conec.cursor()
    cursor.execute("""CREATE TABLE pcbd (
                    equipos text,
                    ipv4 text,
                    ipv6 text,
                    macc text,
                    usuario text,
                    tipo text
                    )""")
    print('se crearon las colimnas')
    conec.commit()
    conec.close()


def ins_datos(equipos, ipv4, ipv6, macc, usuario, tipo,):
    conec = sq.connect(ruta)
    cursor = conec.cursor()
    instr = f"INSERT INTO pcbd VALUES ('{equipos}', '{ipv4}', '{ipv6}', '{macc}', '{usuario}', '{tipo}')"
    cursor.execute(instr)
    conec.commit()
    conec.close()

def leer_datos():
    conec = sq.connect(ruta)
    cursor = conec.cursor()
    instr = f"SELECT * FROM pcbd"
    cursor.execute(instr)
    datos = cursor.fetchall()
    conec.commit()
    conec.close()
    return datos

def eliminar_filas (equipo):
    conec = sq.connect(ruta)
    cursor = conec.cursor()
    instruc = f"DELETE FROM pcbd WHERE equipos='{equipo}'"
    cursor.execute(instruc)
    conec.commit()
    conec.close()

def editar_datos (equipos, ipv4, ipv6, macc, usuario, tipo, identificador):
    conec = sq.connect(ruta)
    cursor = conec.cursor()
    instruc = f"UPDATE pcbd SET equipos=?, ipv4=?, ipv6=?, macc=?, usuario=?, tipo=? WHERE equipos=?"
    cursor.execute(instruc, (equipos, ipv4, ipv6, macc, usuario, tipo, identificador))
    conec.commit()
    conec.close()

if __name__ == '__main__':
    leer_datos()
