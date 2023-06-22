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

#--------------------------------------------------