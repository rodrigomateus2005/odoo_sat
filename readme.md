# Simple SAT for Odoo

## Descrição

Este projeto usa a api sathub (https://github.com/base4sistemas/sathub) para se comunicar com o equipamento SAT.

## Iniciando

para inicial o ambiente, execute os seguintes comandos:

```Shell
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
pip install <<path do Odoo>>
```

## Debug

Para subir o container docker para uso em debug execute os seguintes comando:

```Shell
docker run -d -e POSTGRES_USER=<<user>> -e POSTGRES_PASSWORD=<<password>> -e POSTGRES_DB=postgres --name db postgres:15

docker run -v /path/to/addons:/mnt/extra-addons -p 8069:8069 --name odoo --link db:db -t odoo:16
```

e coloque os arquivos do modulo na pasta mapeada.

Depois log no container e altere o arquivo /usr/bin/odoo e faça as alterações necessárias para se parecer com o modelo debug/model.odoo.debug.py.

Reinicie o container e utlize o launch.json da pasta debug como exemplo caso use VS Code.