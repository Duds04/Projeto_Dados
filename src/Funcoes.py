import unidecode

# Existem diversas funções que são usadas em diversos locais nos códigos. Portanto foi decidido colocar todas as funções em um único file, facilitando assim se uso e funcionamento

def teste():
    print("Teste Funcionando")

def removeAcentos(texto):
    return unidecode.unidecode(texto)

# Remove acentos de uma coluna especifica, coloca-a em maiusculas e retira espaços inuteis (strip)
def removerAcentos_PorMaiusculas(df, coluna):
    df[coluna] = df[coluna].apply(removeAcentos)
    df[coluna] = df[coluna].str.upper().str.strip()


# Funcao usada para trocar o nome da cidade que está errada
def ConsertaMunicipios(dfEntrada, cidadeErrada, cidadeCerta):
    dfEntrada['Municipio_Nascimento'] = dfEntrada['Municipio_Nascimento'].apply(lambda x: str(x).replace(cidadeErrada, cidadeCerta))
    return dfEntrada

# Recebe uma coluna de value_counts, uma coluna base, e filtra a coluna base substituindo os valores por 'OUTROS' dada uma porcentagem. E outras palavras, substitui os valores de columnValue por 'Outros' se o valor representar abaixo de uma determinada porcentagem
def GroupSmallDataIntoOthers(df, columnValue,valueCounts, value=0.005):
    df = df.copy()
    total = df[valueCounts].sum()
    df['CountOthers'] = (df[valueCounts]/total > value)
    df[columnValue] = df[columnValue].where(df['CountOthers'], 'OUTROS')
    df = df.drop(columns=['CountOthers'])
    df = df.groupby(columnValue).sum().sort_values(by=valueCounts, ascending=False).reset_index()
    return df

# Filtra ano da coluna 'Admissao' e 'Saida'
def filtraAno(df, coluna):
    df[coluna] = df[coluna].apply(lambda x : str(x)[:4])
    return df