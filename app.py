from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emission-estimation')
def emission_estimation():
    return render_template('emission-estimation.html')

@app.route('/carbon-neutrality-pathways')
def carbon_neutrality_pathways():
    return render_template('carbon-neutrality-pathways.html')

@app.route('/data-visualization')
def data_visualization():
    return render_template('data-visualization.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)
