from flask import Flask, render_template
import requests

app = Flask(__name__)

DOG_API_BASE = "https://dogapi.dog/api/v2"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    response = requests.get(f"{DOG_API_BASE}/breeds")  # gets different breeds
    if response.status_code == 200:
        breeds = response.json()["data"]
        print("Breeds data", breeds)  # This will print the list of breeds to the terminal (for debugging)
        return render_template('breeds.html', breeds=breeds)
    else:
        return render_template('error.html', message="Could not load breeds")

@app.route('/breeds/<breed_id>')

def breed_detail(breed_id):
    response = requests.get(f"{DOG_API_BASE}/breeds/{breed_id}")
    if response.status_code == 200:
        breed = response.json()["data"]
        print(breed)  
        return render_template('breedDetails.html', breed=breed)
    else:
        return render_template('error.html', message="Could not load breed details")

@app.route('/facts')
def facts():
    response = requests.get(f"{DOG_API_BASE}/facts?limit=5") #get the facts
    if response.status_code == 200:
        facts = response.json()["data"]
        print(facts)  
        return render_template('facts.html', facts=facts)
    else:
        return render_template('error.html', message="Could not load dog facts")

if __name__ == '__main__':
    app.run(debug=True)

