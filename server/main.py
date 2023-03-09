from flask import Flask
from dotenv import load_dotenv
from datetime import datetime
import os
import flask_cors

if os.getenv("FLASK_ENV") == "development":
    load_dotenv("./config/.env.development")


def create_app() -> Flask:
    app = Flask(__name__, static_folder="../client/build", static_url_path="/")
    app.url_map.strict_slashes = False
    return app


app = create_app()
if os.getenv("FLASK_ENV") == "development":
    flask_cors.CORS(app, supports_credentials=True)


@app.route("/api/v1/health", methods=["GET"])
def get_health():
    return {
        "uptime": f"{os.times()[4]}s",
        "code": 200,
        "success": True,
        "date": datetime.utcnow(),
    }


@app.errorhandler(404)
def other_routes(error):
    return app.send_static_file("index.html")
