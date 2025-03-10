import pandas as pd

df = pd.read_csv("Amsterdam1.csv")


#Función_1
def carga_de_archivo(df):
    if df.endswith('.csv'):
        return pd.read_csv(df)
    elif df.endswith('.xlsx'):
        return pd.read_excel(df)
    else:
        raise ValueError("Este formato no está soportado para esta función")

#Función_2
def sustituye_valores_nulos(df):
    for col in df.columns:  #Buscamos por las columnas
        if df[col].dtype in ['float64', 'int64']:  # seleccionamos las numéricas 
            if list(df.columns).index(col) % 2 == 0:  # Si la posición es par se sustituye con mean
                df[col] = df[col].fillna(round(df[col].mean(), 1))  
            else:  # Si la posición es impar se sustituye con 99
                df[col] = df[col].fillna(99)  
        else:  # Si no es numérica se sustituye con string
            df[col] = df[col].fillna("Este_es_un_valor_nulo")  
    return ("Valores nulos sustituidos en DataFrame", df)


#Función_3
def cuenta_valores_nulos(df):
    #Valores nulos por columna 
    valores_nulos_cols = df.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = df.isnull().sum().sum()
    
    return ("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)
    
#Función_4
def sustituye_valores_atipicos(df):
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            y = df[col]  # Obtener la columna numérica

            percentile25 = y.quantile(0.25)
            percentile75 = y.quantile(0.75)
            iqr = percentile75 - percentile25
            limite_superior_iqr = percentile75 + 1.5 * iqr
            limite_inferior_iqr = percentile25 - 1.5 * iqr

            # Sustituir valores atípicos
            df.loc[df[col] > limite_superior_iqr, col] = limite_superior_iqr
            df.loc[df[col] < limite_inferior_iqr, col] = limite_inferior_iqr

    return df 