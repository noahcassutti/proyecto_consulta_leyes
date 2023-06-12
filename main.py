import sqlite3
import pandas as pd

#Funcion para insertar las leyes que haga falta
def insertLaw():
    #Nro = 0
    tipoNorma = input("Tipo de Normativa: ")
    numNorma = input("Numero de Normativa: ")
    fecha = input("Fecha: ")
    desc = input("Descripcion: ")
    cat = input("Categoria: ")
    jur = input("Jurisdiccion: ")
    org = input("Organo Legislativo: ")
    keyW = input("Palabra Clave: ")
    cursor.execute("INSERT INTO laws (TipoDeNormativa,NumeroDeNormativa,Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabraClave) Values(?,?,?,?,?,?,?,?)",
                    (tipoNorma, numNorma, fecha, desc, cat, jur, org, keyW))
    P.commit

#Funcion para ver las leyes ya insertadas
def verLaw():
    cursor.execute("SELECT * FROM laws")        
    results = cursor.fetchall()
    results_df = pd.DataFrame(results, columns=["Nro","TipoDeNormativa", "NumeroDeNormativa", "Fecha", "Descripcion", "Categoria", "Jurisdiccion", "OrganoLegislativo", "PalabraClave"])
    print(results_df)

#Funcion a la que le podemos ir añadiendo las opciones    
def menu():
    global opcion
    print("------------------Menu------------------")
    opcion = input("Seleccione 1 para insertar Leyes \nSeleccione 2 para ver las Leyes Existentes\n")

#preguntar si sigue agregando o sale al menu
def preguntarOtra():
    otro = (input("Otra?:(si/no) "))
    if otro == "si":
        insertLaw()
    elif otro == "no":
        print("Todas Agregados Correctamente")
        menu()

#conexion a la base de datos y poniendo de alias la letra P de proyecto
with sqlite3.connect("Proyect") as P:
    
    cursor = P.cursor()
    cursor.execute("Create table if not exists laws (Nro INTEGER PRIMARY KEY AUTOINCREMENT, TipoDeNormativa VARCHAR(50), NumeroDeNormativa VARCHAR(50), Fecha VARCHAR(20), Descripcion VARCHAR(50), Categoria VARCHAR(50), Jurisdiccion VARCHAR(50), OrganoLegislativo VARCHAR(50), PalabraClave VARCHAR(50))")
    
    menu()
    
    if opcion == "1":
        insertLaw()
        preguntarOtra()
        preguntarOtra()
        preguntarOtra()
       
        menu()
        
    elif opcion == "2":
        verLaw()
        menu()
        fin = input("Salir del programa? (si/no)")
        if fin == "no":
            menu()
        elif fin == "si":
            print("Adios...")
            
    else:
        print("Opcion Incorrecta")