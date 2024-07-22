# -----------------------------------------
# Little project by snkfranco
# Github: https://github.com/snkfranco
# -----------------------------------------

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_info = None
    abilities_str = None
    height_m = None
    weight_kg = None
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name').lower()
        pokemon_info = get_pokemon_info(pokemon_name)
        if pokemon_info:
            abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
            abilities_str = ', '.join(abilities)
            height_m = pokemon_info['height'] / 10
            weight_kg = pokemon_info['weight'] / 10
    return render_template('index.html', 
                           pokemon_info=pokemon_info, 
                           abilities_str=abilities_str, 
                           height_m=height_m, 
                           weight_kg=weight_kg)

if __name__ == '__main__':
    app.run(debug=True)
