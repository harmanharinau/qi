echo "Cloning Repo...."
git clone https://github.com/harmanharinau/pirosearcher.git /pirosearcher
cd /pirosearcher
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
