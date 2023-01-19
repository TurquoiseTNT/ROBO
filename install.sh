curl -L -o ROBO-b.tar.gz "https://github.com/TurquoiseTNT/ROBO/archive/refs/tags/d.tar.gz"
mkdir /home/ROBO
tar xf ROBO-b.tar.gz -C /home/ROBO
cd /home/ROBO
mv robo.service /lib/systemd/system/robo.service
sudo chmod 644 /lib/systemd/system/robo.service
sudo systemctl daemon-reload
sudo systemctl enable robo.service