from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/previsao')
def previsao():
    cidade = request.args.get('cidade')
    if cidade:
        api_key = 'coloque_sua_Chave_Api_Aqui'
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': cidade, 'appid': api_key, 'units': 'metric'}
        
        response = requests.get(base_url, params=params)
        data = response.json()
        
        return jsonify(data)
    else:
        return jsonify({'error': 'Parâmetro "cidade" ausente na solicitação'})

if __name__ == '__main__':
    app.run(debug=True)
