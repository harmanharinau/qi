echo "Cloning Repo...."
git clone https://github.com/harmanharinau/qi.git /qi
cd /qi
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
