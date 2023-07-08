# run.py

import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    print("MAIN!!!")
    app.run(port=5001, host='0.0.0.0')
