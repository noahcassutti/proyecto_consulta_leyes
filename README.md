

# Proyecto de Consulta de Leyes (INTEGRADOR)

Este proyecto se desarrolló para el instituto superior politecnico de cordoba. El enunciado se basa con  el Poder Judicial de la Provincia de Córdoba y permite a los usuarios realizar consultas sobre leyes vigentes. Los usuarios pueden buscar leyes por número o palabras clave y obtener una breve descripción de sus contenidos.

## Contenido del Proyecto

El proyecto se compone de los siguientes elementos:

1. **Base de Datos**: Se utiliza una base de datos SQLite para almacenar la información de las leyes. La base de datos contiene tres tablas: `Leyes`, `Jurisdiccion`, e `Identificadores`, que almacenan información sobre las leyes, sus jurisdicciones y palabras clave.

2. **Diagrama Entidad-Relación (DER)**: El proyecto incluye un diseño de DER en formato PDF que muestra la estructura de la base de datos y las relaciones entre las tablas.

3. **Código Python**: El código Python se encarga de la interacción con la base de datos y permite a los usuarios realizar consultas y operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en los registros de leyes. El código se organiza en dos clases principales: `Leyes` y `Mods`, y se ejecuta permanentemente para brindar opciones a los usuarios.

## Uso del Proyecto

Para utilizar el proyecto, sigue estos pasos:

1. **Clonar el Repositorio**: Clona este repositorio en tu máquina local.

2. **Requisitos Previos**: Asegúrate de tener Python instalado en tu sistema.

3. **Ejecutar el Proyecto**: Ejecuta el archivo Python `main.py` para iniciar el programa. El programa se ejecutará permanentemente y ofrecerá un menú de opciones.

4. **Menú de Opciones**: El programa ofrece un menú con las siguientes opciones:
   - **1. Insertar Leyes**: Permite ingresar información sobre leyes.
   - **2. Ver Leyes Existentes**: Muestra las leyes almacenadas en la base de datos.
   - **3. Salir del Programa**: Cierra el programa.
   - **4. Actualizar un Registro**: Permite actualizar la fecha de un registro existente.
   - **5. Eliminar un Registro**: Permite eliminar registros por palabra clave.
   - **6. Buscar Registro por Palabra Clave**: Permite buscar leyes por palabra clave.

5. **Colaboración en GitHub**: El proyecto está alojado en GitHub y se utiliza un flujo de trabajo de Git para colaborar en el desarrollo. Cada miembro del equipo debe colaborar mediante confirmaciones (commits) al proyecto.

## Integrantes del Grupo:
-LEO PLAZA -DENISSE SABEFF -NOAH CASSUTTI -SANTIAGO TULIAN -MARCOS PORTELA -MATEO OTERO

## Nota:
Las leyes cargadas con sus respectivas descripciones se pueden ver en la base de datos.

## Tests de pruebas:
Realizados localmente, en Visual Studio Code, además en el IDE Pycharm, con la libreria Pandas descargada. Se procedió a descargar en un directorio local el archivo "main.py", ubicarlo en el mismo junto con el archivo de base de datos "proyect.db", el cual contiene las tres leyes solicitadas en la tabla. Luego se probaron las funciones: INSERT, SELECT, UPDATE, DELETE, pudiendo el usuario realizar las correspondientes consultas y actualizaciones, como asi tambien eliminar registros.
Todas las modificaciones impactaron en el archivo .db al momento de salir del menú (opción 3) del CRUD, conforme a los requerimientos de su Proyecto Integrador.



## Información Adicional

El proyecto tiene como objetivo contribuir a la modernización de la gestión judicial y mejorar la experiencia de los usuarios que buscan respuestas a problemas jurídicos en el sistema judicial es un trabajo integrador de la tecnicatura

---

