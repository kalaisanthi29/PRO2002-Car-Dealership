
from flask import Flask
from car_dealership_api.routes.car_routes import car_bp

app = Flask(__name__)
app.register_blueprint(car_bp)


if __name__ == "__main__":
    app.run(debug=True)
