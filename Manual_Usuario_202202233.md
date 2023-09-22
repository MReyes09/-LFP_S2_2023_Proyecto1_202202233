#####  Universidad de San Carlos de Guatemala
#####  Facultad de Ingeniería
#####  Escuela de Ciencias y Sistemas
#####  Laboratorio de Lenguajes Formales y de Programación
##### **Matthew Emmanuel Reyes Melgar 202202233**

# Manual De Usuario

## Descripción General

El Manual de Usuario proporciona una guía detallada sobre el uso de la Aplicación de Análisis Léxico. Esta aplicación consta de una ventana única que ofrece opciones para cargar, editar, analizar y generar informes sobre el código fuente en un lenguaje específico. A continuación, se describe en detalle cada componente y función de la aplicación.

## Vista de Usuario

La vista de usuario de la aplicación consta de una ventana principal con los siguientes elementos:

### Barra de Navegación

La barra de navegación se encuentra en la parte superior de la ventana y contiene las siguientes opciones:

- **Abrir:** Permite al usuario abrir un archivo en formato JSON para editarlo en la aplicación.
- **Guardar:** Permite al usuario guardar los cambios en el archivo actual.
- **Guardar Como:** Permite al usuario guardar el archivo actual con un nuevo nombre o en una ubicación diferente.
- **Salir:** Cierra la aplicación.

### Área de Edición de Texto (txtArea)

El área de edición de texto es un campo de texto grande donde se muestra y edita el contenido del archivo JSON cargado. El usuario puede modificar el código fuente en este campo.

### Botones de Acción

La ventana también contiene los siguientes botones de acción:

- **Analizar:** Ejecuta el analizador léxico en el código fuente cargado y muestra los resultados de las operaciones contenidas en el archivo JSON.
- **Errores:** Genera un archivo JSON separado que muestra los errores léxicos detectados en el código fuente.
- **Reporte:** Aún no se ha definido su funcionalidad.

### Numeración de Líneas

A la izquierda del área de edición de texto, se encuentra una columna que muestra la numeración de las líneas. Esta numeración se actualiza automáticamente a medida que se edita el código fuente.

## Uso Básico

A continuación, se describen las funciones básicas de la aplicación:

### Abrir

La opción "Abrir" en la barra de navegación permite al usuario seleccionar y cargar un archivo JSON existente en la aplicación. El contenido del archivo se muestra en el área de edición de texto (txtArea) y se puede editar. Si se realiza algún cambio, se puede guardar el archivo con la opción "Guardar" o "Guardar Como".

### Guardar y Guardar Como

- **Guardar:** La opción "Guardar" permite al usuario guardar los cambios realizados en el archivo actual. Si el archivo se abrió previamente, los cambios se guardarán en la misma ubicación y con el mismo nombre.
- **Guardar Como:** La opción "Guardar Como" permite al usuario guardar el archivo actual con un nombre nuevo o en una ubicación diferente. Se abrirá un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo.

### Analizar

El botón "Analizar" ejecuta el analizador léxico en el código fuente cargado en el área de edición de texto. Después de la ejecución, se muestran los resultados de las operaciones contenidas en el archivo JSON en un cuadro de mensaje. Los resultados incluyen la identificación de tokens y operaciones realizadas.

### Errores

El botón "Errores" genera un archivo JSON separado que muestra los errores léxicos detectados en el código fuente. Si no se encuentran errores, el archivo JSON estará vacío. Los errores incluyen detalles como el lexema, el tipo de error, la columna y la fila en la que se produjo el error.

## Funcionalidades Adicionales

### Reporte

La funcionalidad del botón "Reporte" aún no ha sido definida en la aplicación y puede implementarse en futuras versiones.

## Conclusiones

El Manual de Usuario proporciona una guía completa para utilizar la Aplicación de Análisis Léxico. Los usuarios pueden cargar, editar y analizar código fuente, así como generar informes y gestionar errores léxicos. La aplicación ofrece una interfaz sencilla y funcionalidades esenciales para el análisis de código en un lenguaje específico.

