# Copyright 2020 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""
    Pipeline            : data_engineer
    Autor               : Daniel Rojos R.
    Fecha               : 2021-12-29
    Objetivo:
        1)  Generar una función para la limpieza de datos del catalogo "result" en el campo "console", 
            ya que tiene espacios en blanco para las consolas PC y VITA, y generar el catálogo "result_refined"

        2)  Generar una función para unir los catálogos result y consoles usando el campo console, y crear el catalogo "result_consoles"

        3)  Generar una función que reciba como input el catalogo "result_refined" 
            y genere un catalogo con los 10 mejores juegos por cada consola/compañia.

        4)  Generar una función que reciba como input el catalogo "result_refined" 
            y genere un catalogo con los 10 peores juegos por cada consola/compañia.

        5)  Generar una función que reciba como input el catalogo "result_consoles" 
            y genere un catalogo con  Los 10 mejores juegos por todas las consolas.

        6)  Generar una función que reciba como input el catalogo "result_consoles" 
            y genere un catalogo con  Los 10 peores juegos por todas las consolas.

    Requisitos:
        1)  El reporte debe ser versionado diariamente por cada ejecución
"""
import pandas as pd

def cleaningResult(df):
    """
        1)  Generar una función para la limpieza de datos del catalogo "result" en el campo "console", 
                ya que tiene espacios en blanco para las consolas PC y VITA, lo que podría
                generar falsos resultados en los análisis.
    """    
    df['console']=df['console'].str.strip()
    return df

def joinData(refinedResults,consoles):
    """
    2)  Generar una función para unir los catálogos result y consoles usando el campo console, y crear el catalogo "resultConsoles"
    """    
    df = refinedResults.merge(consoles,how='inner')
    return df

def top10BestGames(refinedResults): 
    """
    3)  Generar una función que reciba como input el catalogo "resultConsoles" 
        y genere un catalogo con los 10 mejores juegos por cada consola/compañia.
    """    
    df = refinedResults.sort_values(by=['metascore','userscore'],ascending= False).head(10).drop_duplicates(subset=['name'])
    return df

def top10WorstGames(refinedResults): 
    """
    4)  Generar una función que reciba como input el catalogo "resultConsoles" 
    y genere un catalogo con los 10 peores juegos por cada consola/compañia.
    """    
    df = refinedResults.sort_values(by=['metascore','userscore'],ascending= True).head(10).drop_duplicates(subset=['name'])
    return df

def top10BestGamesCompany(resultConsoles):
    """
        5)  Generar una función que reciba como input el catalogo "resultConsoles" 
        y genere un catalogo con los 10 mejores juegos por todas las consolas.
    """ 
    grouped =resultConsoles.groupby(['company','console'])
    df=grouped.apply(lambda g: g.sort_values(by="metascore",ascending=False).head(10))
    df2=df[['metascore','name']].reset_index()
    df2=df2[['company','console','metascore','name']]
    df2=pd.DataFrame(df2)
    return df2

def top10WorstGamesCompany(resultConsoles):
    """
        6)  Generar una función que reciba como input el catalogo "resultConsoles" 
        y genere un catalogo con los 10 peores juegos por todas las consolas.
    """    
    grouped =resultConsoles.groupby(['company','console'])
    df=grouped.apply(lambda g: g.sort_values(by="metascore",ascending=True).head(10))
    df2=df[['metascore','name']].reset_index()
    df2=df2[['company','console','metascore','name']]
    df2=pd.DataFrame(df2)
    return df2