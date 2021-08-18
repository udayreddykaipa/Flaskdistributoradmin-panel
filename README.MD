# Create venv
python3 -m venv dis_admin_panel

# depency installation( activate venv)
python3 -m pip install -r requirements.txt

# Usage, to start server
source dis_admin_panel/bin/activate
python3 src/server.py