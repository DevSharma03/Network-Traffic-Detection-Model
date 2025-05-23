from flask import Flask, render_template, send_file
import os

app = Flask(__name__, static_folder='leaflet_map_files')

@app.route('/map')
def serve_map():
    return send_file('leaflet_map.html')

@app.route('/')
def home():
    map_file = "leaflet_map.html"
    if not os.path.exists(map_file):
        return "Map file not found. Please generate it using your R script."
    return render_template("index.html", map_file="/map")

if __name__ == '__main__':
    app.run(debug=True)
