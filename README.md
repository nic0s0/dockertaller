# dockertaller
Dockers FTP: lftp (cliente) y proftpd (servidor)

Pre-requisito: docker


- Cliente:
En carpeta "client" se encuentra el dockerfile para crear la imagen ubuntu de lftp.
Corre con:
```
docker run -it CONTAINER_ID lftp user:pass@ip
```
Con parametros default:
```
docker run -it CONTAINER_ID
```
En este caso se usarán user=userftp, pass=passftp e ip=172.17.0.2 como default.


- Servidor:
En carpeta "server" se encuentra el dockerfile para crear la imagen ubuntu de proftpd.
Corre con:
```
docker run -it CONTAINER_ID
```
Como daemon:
```
docker run -dit CONTAINER_ID
```
