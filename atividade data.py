atividade data

# etl.py

import requests
import pandas as pd

def etlBcB(data: str) -> pd.DataFrame:
    """
    Função para extrair os dados da API do Banco Central com base no trimestre fornecido.
    
    Parâmetros:
    data (str): O trimestre no formato 'YYYYQx' (ex: '20191' para o primeiro trimestre de 2019)
    
    Retorno:
    pd.DataFrame: DataFrame com os dados extraídos da API do Banco Central
    """
    
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json" 
    
    try:
        req = requests.get(url)
        req.raise_for_status()  # Lança um erro se o status code não for 200
        print(f"Status Code: {req.status_code}")
        dados = req.json() 
        
        df = pd.json_normalize(dados["value"])
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao realizar a requisição: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

if __name__ == "__main__":
    # Exemplo de uso da função
    dadosBcB = etlBcB("20191")
    print(dadosBcB.info())
