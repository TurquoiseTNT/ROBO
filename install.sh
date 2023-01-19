curl "https://github.com/TurquoiseTNT/ROBO"
cd ROBO
mv robo.service /lib/systemd/system/robo.service
sudo chmod 644 /lib/systemd/system/robo.service
sudo systemctl daemon-reload
sudo systemctl enable robo.service