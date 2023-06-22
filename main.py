import sqlite3
import pandas as pd

# Clase Leyes para insertar y ver leyes
class Leyes:
    def __init__(self):
        self.tipoNorma = None
        self.numNorma = None
        self.fecha = None
        self.desc = None
        self.cat = None
        self.jur = None
        self.org = None
        self.keyW = None

    def ingresar_datos(self):
        self.tipoNorma = input("Tipo de Normativa: ")
        self.numNorma = input("Numero de Normativa (Solo Numeros): ")
        self.fecha = input("Fecha Formato dd/mm/aaaa: ")
        self.desc = input("Descripcion: ")
        self.cat = input("Categoria: ")
        self.jur = input("Jurisdiccion: ")
        self.org = input("Organo Legislativo: ")
        self.keyW = input("Palabra Clave: ")

    def insertar_ley_Leyes(self, P):
        cursor = P.cursor()
        cursor.execute("INSERT INTO Leyes (TipoDeNormativa, NumeroDeNormativa, Fecha, Descripcion) VALUES (?,?,?,?)",
                       (self.tipoNorma, self.numNorma, self.fecha, self.desc))

    def insertar_ley_Jurisdiccion(self, P):
        cursor = P.cursor()
        cursor.execute("INSERT INTO Jurisdiccion (Nro, Categoria, Jurisdiccion) VALUES (?,?,?)",
                       (self.numNorma, self.cat, self.jur))

    def insertar_ley_Identificadores(self, P):
        cursor = P.cursor()
        cursor.execute("INSERT INTO Identificadores (Nro, OrganoLegislativo, PalabraClave) VALUES (?,?,?)",
                       (self.numNorma, self.org, self.keyW))

    def ver_laws_unificadas(self, P):
        cursor = P.cursor()
        cursor.execute("SELECT t1.Nro, t1.TipoDeNormativa, t1.NumeroDeNormativa, t1.Fecha, t1.Descripcion, t2.Categoria, t2.Jurisdiccion, t3.OrganoLegislativo, t3.PalabraClave "
                       "FROM Leyes AS t1 "
                       "JOIN Jurisdiccion AS t2 ON t1.NumeroDeNormativa = t2.Nro "
                       "JOIN Identificadores AS t3 ON t1.NumeroDeNormativa = t3.Nro")
        results = cursor.fetchall()
        results_df = pd.DataFrame(results, columns=["Nro", "TipoDeNormativa", "NumeroDeNormativa", "Fecha",
                                                    "Descripcion", "Categoria", "Jurisdiccion",
                                                    "OrganoLegislativo", "PalabraClave"])
        print(results_df)
    def buscar_por_palabra_clave(self, P):
        palabra_clave = input("Ingrese la palabra clave a buscar: ")
        cursor = P.cursor()
        cursor.execute("SELECT t1.Nro, t1.TipoDeNormativa, t1.NumeroDeNormativa, t1.Fecha, t1.Descripcion, t2.Categoria, t2.Jurisdiccion, t3.OrganoLegislativo, t3.PalabraClave "
                   "FROM Leyes AS t1 "
                   "JOIN Jurisdiccion AS t2 ON t1.NumeroDeNormativa = t2.Nro "
                   "JOIN Identificadores AS t3 ON t1.NumeroDeNormativa = t3.Nro "
                   "WHERE t3.PalabraClave=?", (palabra_clave,))
        results = cursor.fetchall()
        if not results:
            print("Palabra no encontrada.")
        else:
            results_df = pd.DataFrame(results, columns=["Nro", "TipoDeNormativa", "NumeroDeNormativa", "Fecha",
                                                    "Descripcion", "Categoria", "Jurisdiccion",
                                                    "OrganoLegislativo", "PalabraClave"])
            print(results_df)

# Clase Mods para actualizar y eliminar registros
class Mods:
    @staticmethod
    def actualizar_por_nro(P, nro):
        cursor = P.cursor()
        cursor.execute("SELECT * FROM Leyes WHERE Nro=?", (nro,))
        registro_Leyes = cursor.fetchone()

        if registro_Leyes is None:
            print("No se encontró ningún registro con el número especificado.")
            return

        #tipoNorma = input("Tipo de Normativa: ")
        #numNorma = input("Numero de Normativa: ")
        fecha = input("Fecha: ")
        #desc = input("Descripcion: ")

        cursor.execute("UPDATE Leyes SET Fecha=? WHERE Nro=?",
                       (fecha, nro))

        cursor.execute("SELECT * FROM Jurisdiccion WHERE Nro=?", (nro,))
        registro_Jurisdiccion = cursor.fetchone()

        if registro_Jurisdiccion is not None:
            cat = input("Categoria: ")
            jur = input("Jurisdiccion: ")

            cursor.execute("UPDATE Jurisdiccion SET Categoria=?, Jurisdiccion=? WHERE Nro=?",
                           (cat, jur, nro))
        cursor.execute("SELECT * FROM Identificadores WHERE Nro=?", (nro,))
        registro_Identificadores = cursor.fetchone()

        if registro_Identificadores is not None:
            org = input("Organo Legislativo: ")
            keyW = input("Palabra Clave: ")

            cursor.execute("UPDATE Identificadores SET OrganoLegislativo=?, PalabraClave=? WHERE Nro=?",
                           (org, keyW, nro))

        P.commit()
        print("Registro actualizado con éxito.")

    @staticmethod
    def eliminar_por_keyw(P, keyw):
        cursor = P.cursor()

        cursor.execute("DELETE FROM Identificadores WHERE PalabraClave=?", (keyw,))
        cursor.execute("DELETE FROM Jurisdiccion WHERE Nro IN (SELECT Nro FROM Identificadores WHERE PalabraClave=?)", (keyw,))
        cursor.execute("DELETE FROM Leyes WHERE Nro IN (SELECT Nro FROM Identificadores WHERE PalabraClave=?)", (keyw,))

        P.commit()
        print("Registro eliminado con éxito.")    

# Función para mostrar el menú
def menu():
    print("------------------Menu------------------")
    print("Seleccione 1 para insertar Leyes")
    print("Seleccione 2 para ver las Leyes Existentes")
    print("Seleccione 3 para salir del programa")
    print("Seleccione 4 para actualizar un registro")
    print("Seleccione 5 para eliminar un registro")
    print("Seleccione 6 para buscar un registro por palabra clave")


# Función para preguntar si se agregan más leyes
def preguntarOtra(objeto_leyes):
    otro = input("¿Agregar otra ley? (si/no): ")
    if otro == "si":
        objeto_leyes.ingresar_datos()
        objeto_leyes.insertar_ley_Leyes(P)
        objeto_leyes.insertar_ley_Jurisdiccion(P)
        objeto_leyes.insertar_ley_Identificadores(P)
        preguntarOtra(objeto_leyes)
    elif otro == "no":
        print("Todas las leyes han sido agregadas correctamente.")
        