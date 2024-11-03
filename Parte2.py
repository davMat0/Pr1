import os

def mensajeEntreProcesos():
    fd = os.pipe()
    # mensaje del padre
    mensajePadre = "saludo mi hijo"
    # se crea un nuevo proceso
    pid = os.fork()
    # se verifica en que proceso se esta
    if pid == 0:  # proceso hijo
        # se lee el mensaje del padre
        buffer = os.read(fd[0], 80).decode("utf-8")
        # se imprime el mensaje recibido
        print(f"El hijo recibe del padre: {buffer}")
        os.close(fd[0])

        mensajeHijo = buffer.upper() #convierte el mensaje en mayusculas
        os.write(fd[1], mensajeHijo.encode("utf-8"))
        os.close(fd[1])
        os._exit(0)

    else:  # proceso padre

        # se escribe el mensaje en el pipe
        os.write(fd[1], mensajePadre.encode("utf-8"))
        # se lee el mensaje del hijo
        os.close(fd[1])

        os.wait()
        buffer = os.read(fd[0], 80).decode("utf-8")

        # se imprime el mensaje recibido
        print(f"El padre recibe del hijo: {buffer}")
        os.close(fd[0])


def intercambioArchivos():
    #ruta del archivo
    ruta_archivo = "archivo.txt"
    fd = os.pipe()
    # se crea un nuevo proceso
    pid = os.fork()

    # se verifica en que proceso se esta
    if pid == 0:  # proceso hijo
        #se lee el contenido de la pipe
        contenido = os.read(fd[0],1024).decode("utf-8")
        os.close(fd[0])

        lineas = contenido.splitlines() #divide el contenido en líneas
        numLineas = len(lineas) #cuenta el numero de lineas
        numPalabras = 0 #contador de palabras

        #se cuenta las palabras que hay por linea y las suma al total
        for linea in lineas:
            numPalabras += len(linea.split())

        resultado = f"Numero de lineas {numLineas}, numero de palabras {numPalabras}"

        os.write(fd[1],resultado.encode("utf-8"))
        os.close(fd[1])
        os._exit(0)
    else: #proceso padre
        try:
            archivo = open(ruta_archivo) # se abre el archivo
            contenido = archivo.read() # se lee todo el contenido del archivo
            #se verifica si el contenido no está vacio
            if contenido:
                #escribe el contenido en la pipe
                os.write(fd[1],contenido.encode("utf-8"))
                os.close(fd[1])

                os.wait() #se espera que el proceso hijo termine

                resultado = os.read(fd[0], 1024).decode("utf-8")
                os.close(fd[0])
                print(resultado)
            else:
                print("El archivo esta vacio")
        #se captura la excepción si el archivo no se encuentra
        except FileNotFoundError:
            print("El archivo no se encontro")

if __name__ == '__main__':
    print("Mensaje entre procesos")
    mensajeEntreProcesos()
    print("Intercambio de archivos")
    intercambioArchivos()