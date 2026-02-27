import socket

ip = '127.0.0.1'
puerto_inicio = 1
puerto_fin = 200

print(f'La IP objetivo a escanear es {ip} del puerto {puerto_inicio} al {puerto_fin}...')
print('*' * 80)

# Se realiza un recorrido para escanear el rango de puertos de inicio a fin de la IP objetivo
for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
	    # Se crea conexión
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Se intenta conectar al puerto actual en el bucle
        resultado_conexion = socket_conexion.connect_ex((ip, puerto))
		
        # Se verifica resultado de conexión
        if resultado_conexion == 0:
            print(f'Puerto {puerto}: ABIERTO')

            # Se Trata de obtener el banner del puerto actual en el bucle
            try:
                # Esperar máximo 3 segundos
                socket_conexion.settimeout(3)
                
                # Se reciben datos (banner) del socket
                banner = socket_conexion.recv(1024)
                
                # Se decodifica el banner de bytes a texto
                banner_texto = banner.decode('utf-8', errors='ignore')
                
                # Se imprime el contenido del banner limpiando la cadena 
                print(f'  - Banner: {banner_texto.strip()}')
            
            except:
                # Si el banner no se encuentra disponible
                print(f'  - Banner: No disponible')
		
        # Se cierra la conexión		
        socket_conexion.close()
		
    except:
        pass
print('*' * 80)
    
print(f'Escaneo de {ip} del puerto {puerto_inicio} al {puerto_fin} completado')
