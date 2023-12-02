# Projeto de Previsão do Tempo

Este projeto consome a API OpenWeatherMap para fornecer informações meteorológicas para uma cidade específica. O código está dividido em dois arquivos principais: `app.py` e `tempo.py`.

## Estrutura do Projeto

- `app.py`: Contém o aplicativo Flask que disponibiliza uma interface web para consultar a previsão do tempo.
- `tempo.py`: Implementa a classe `OpenWeatherMapAPI` que interage com a API OpenWeatherMap para obter informações meteorológicas.

## Configuração

### Requisitos

Certifique-se de ter Python instalado. Recomenda-se criar um ambiente virtual para isolar as dependências do projeto.

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate


## Instale as dependências do projeto.

Chave de API OpenWeatherMap
Obtenha uma chave de API da OpenWeatherMap `https://openweathermap.org/api` e substitua a variável `api_key` em `app.py` e tempo.py pela sua chave.


## Uso

1. Execute o aplicativo Flask.
- python app.py


2. Abra um navegador e vá para http://localhost:5000/ para acessar a interface web.

3. Digite o nome da cidade e obtenha a previsão do tempo.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests.