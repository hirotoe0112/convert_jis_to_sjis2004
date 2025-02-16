#起動方法
wsl

docker-compose up -d

docker exec -it CONTAINER_ID /bin/bash

pip install pyinstaller

pyinstaller main.py --onefile

cd dist/

./main