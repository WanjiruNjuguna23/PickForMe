from flask import Flask
from flask_cors import CORS
from route import decision_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
# CORS(app)

app.register_blueprint(decision_bp)

if __name__ == '__main__':
    app.run(debug=True)