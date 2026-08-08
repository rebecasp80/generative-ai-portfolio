from app import create_app
from app.config import get_config

cfg = get_config()
app = create_app()

if __name__ == "__main__":
    app.run(host=cfg.HOST, port=cfg.PORT, debug=cfg.DEBUG)
