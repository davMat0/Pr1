import psutil


def listarProcesos(nombre_procesos):

    for nombre in nombre_procesos:
        try:
            encontrado = False
            for proc in psutil.process_iter():
                try:
                    if nombre.lower() in proc.name().lower():
                        print(f"{proc.pid} {proc.name()} {proc.memory_info().rss/(1024 * 2)}")
                        encontrado = True
                except (psutil.NoSuchProcess,psutil.AccessDenied) as e:
                    continue
            if not encontrado:
                print("No se ha encontrado ningun proceso con el nombre de",nombre)
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"Error al acceder al proceso: {nombre}")


def finalizarProceso(nombre_proceso):
    encontrado = False
    try:
        for proc in psutil.process_iter():
            if proc.name() == nombre_proceso:
                proc.kill()
                encontrado = True
        if encontrado:
            print(f"El proceso {nombre_proceso} se ha finalizado")
        else:
            print(f"No se ha encontrado el proceso {nombre_proceso}")
    except (psutil.NoSuchProcess) as e:
        print("El proceso no existe")
    except (psutil.AccessDenied) as e:
        print(f"Acceso denegado. No tienes permiso para finalizar el proceso: {nombre_proceso}")
    except (psutil.ZombieProcess) as e:
        print("El proceso no se puede finalizar")

def main():

    continuar = True

    while continuar:
        print("1-Buscar procesos \n2-Finalizar procesos \n0-Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1": #Buscar procesos
            # Se solicita al usuario la lista de procesos separada por comas
            entrada = input("Introduce los procesos separados por comas: ")

            nombre_procesos = []
            for nombre in entrada.split(','):
                nombre_procesos.append(nombre)
            if len(nombre_procesos) >= 1:
                listarProcesos(nombre_procesos)
            else:
                print("No se ha introducido ningun nombre de proceso")
        elif opcion == "2":#Finalizar procesos
            nombre_proceso = input("Introduce el nombre del proceso que quiere finalizar: ")
            finalizarProceso(nombre_proceso)
        elif opcion == "0":#Salir
            continuar = False
        else:
            print("Opcion incorrecta")

main()