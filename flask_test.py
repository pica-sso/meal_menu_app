from flask import Flask, jsonify
from flask_cors import CORS
from main import LUNCH

app = Flask(__name__)
CORS(app)  # CORS 설정 추가

@app.route('/menu')
def get_menu():
    lu = LUNCH()
    site_url = lu.find_ww(0)
    menu = lu.open_site(url=site_url)
    menu_data = lu.make_menu_dict(menu)
    return jsonify(menu_data)

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, host='10.0.2.2')
