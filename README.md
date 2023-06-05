BGRemover
==
Alternativa de Código Abierto a Remove.bg 


BGRemover es un servicio basado en Docker que proporciona una alternativa de código abierto al popular servicio de pago remove.bg. Este proyecto utiliza la biblioteca backgroundremover de Python para eliminar automáticamente el fondo de las imágenes, similar a cómo funciona remove.bg, pero de manera completamente gratuita y con la flexibilidad y el control que proporciona el código abierto.

Este proyecto puede funcionar como un servicio HTTP independiente que acepta URLs de imágenes codificadas en base64 a través de una ruta de acceso específica. Después de recibir una solicitud, descarga la imagen, procesa la imagen para eliminar el fondo y luego devuelve la imagen procesada.

Además de la funcionalidad básica de eliminación de fondo, este proyecto también implementa un sistema de caché para mejorar el rendimiento al manejar múltiples solicitudes.

Este proyecto está diseñado para ser fácil de desplegar y escalar, lo que lo hace ideal tanto para uso personal como empresarial. Puede ser una excelente opción para cualquiera que necesite un servicio de eliminación de fondo recurrente y esté buscando una solución de código abierto flexible y eficiente.

Recuerda que esta es solo una sugerencia. Puedes personalizarla aún más para adaptarla a las características y objetivos específicos de tu proyecto. Además, es posible que quieras añadir más información sobre cómo utilizar y desplegar tu servicio, así como cualquier limitación o consideraciones importantes que los usuarios deberían tener en cuenta.

## Correr en Docker
 
Clonar el repositorio:
--
Primero, necesitarás clonar el repositorio de GitHub en tu máquina local. Puedes hacer esto con el siguiente comando:

```bash
 
git clone https://github.com/rrortega/BGRemover.git
```

Recuerda reemplazar your_username con tu nombre de usuario de GitHub.

Construir la imagen Docker:
--
Después de clonar el repositorio, cambia al directorio que contiene el Dockerfile:

```bash 
cd bgremover

## Construir la imagen Docker con el siguiente comando:

docker build -t bgremover:latest . -t rro/bgrmover

```

Esto creará una nueva imagen Docker llamada rro/bgrmover con la etiqueta latest.

Ejecutar el contenedor Docker:
---
Una vez que la imagen Docker esté construida, puedes ejecutar el contenedor con el siguiente comando:
```bash 
docker run -p 80:80 bgremover:latest
```
Esto iniciará el contenedor y mapeará el puerto 80 del contenedor al puerto 80 de tu máquina local. Ahora deberías poder acceder al servicio en http://localhost/$BASE64, donde $BASE64 es tu URL de imagen codificada en base64.

## Desplegar con Docker Compose
  

Ejecuta el archivo docker-compose.yml:
--
```yml
version: '3.8'

services:
  bgremover:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "80:80"
```

```bash
## Ejecuta en tu consola:

docker-compose up -d
```

## Desplegar como un Stack en Docker Swarm

Docker Swarm es una herramienta nativa de orquestación para Docker que permite administrar y escalar aplicaciones multi-contenedor en múltiples hosts. Si estás utilizando Docker Swarm, puedes seguir los siguientes pasos para desplegar bgremover como un Stack:

Iniciar un Docker Swarm:
--
```bash
docker swarm init
```
Este comando configurará tu Docker para utilizar la funcionalidad de Swarm.

Desplegar el Stack:
--
```bash
docker stack deploy -c docker-compose.yml bgremover
```

Una vez que el Stack esté en marcha, deberías poder acceder a tu servicio en http://localhost/bgrmv/$BASE64, donde $BASE64 es tu URL de imagen codificada en base64.

-------
Al igual que en las secciones anteriores, esta sección asume ya tienes Docker y Docker Swarm instalados en su máquina.

 
## Hacer Uso del Servicio

Una vez que el servicio esté en marcha, puedes acceder a él a través de la ruta raiz HTTP `/` seguida de la URL de tu imagen codificada en base64. 

Para codificar tu URL en base64, puedes usar varias herramientas en línea o incluso una función de codificación en base64 en tu lenguaje de programación preferido. Para este ejemplo, usaremos una herramienta en línea.

1. **Codificación en base64:**

   Supongamos que la URL de tu imagen es `https://ruta-real.com/imagen.jpg`. Necesitas codificar esta URL en base64. Puedes usar un codificador en línea como [www.base64encode.net](https://www.base64encode.net/base64-url-encoder).

   Al ingresar tu URL en el campo de texto y hacer clic en "Encode", obtendrás una cadena codificada en base64 que se parece a esto: `aHR0cHM6Ly9ydXRhLXJlYWwuY29tL2ltYWdlbi5qcGc=`.

2. **Construir la URL del servicio:**

   Ahora que tienes tu URL codificada en base64, puedes usarla para acceder al servicio. Supongamos que estás ejecutando el servicio en `localhost` en el puerto 80. La URL de acceso al servicio se verá así:

   `http://localhost/aHR0cHM6Ly9ydXRhLXJlYWwuY29tL2ltYWdlbi5qcGc=`

   Aquí, `aHR0cHM6Ly9ydXRhLXJlYWwuY29tL2ltYWdlbi5qcGc=` es la versión codificada en base64 de tu URL de imagen.

Al acceder a esta URL a través de tu navegador o un cliente HTTP, el servicio descargará la imagen desde la URL original, procesará la imagen para eliminar el fondo y luego devolverá la imagen procesada.

Por ejemplo, si usas un cliente HTTP como `curl`, puedes descargar la imagen resultante con el siguiente comando:

```bash
curl -O http://localhost/aHR0cHM6Ly9ydXRhLXJlYWwuY29tL2ltYWdlbi5qcGc=
```

Este comando descargará la imagen resultante y la guardará en el directorio actual con un nombre de archivo basado en la ruta de acceso. Puedes cambiar el nombre del archivo de salida utilizando la opción `-o` con `curl`. 

Por favor, ten en cuenta que estos son solo ejemplos y puedes modificarlos según tus necesidades o cómo hayas configurado tu servicio.



