# 2daw-m12-p1-solution

Proposta de solució del projecte 1 dins del mòdul de projecte (M12) de 2n de DAW.

## Setup

### Python Virtual Environment

Crea l'entorn:

    python3 -m venv .venv

Activa'l:

    source .venv/bin/activate

Instal·la el requisits:

    pip install -r requirements.txt

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

### Base de dades

L'aplicació suporta tres motors de bases de dades: Postgres, MySQL i SQLite. En tots els casos, hi ha quatre usuaris de prova i tots tenen com a contrasenya `test`:

* `joan@example.com` que té el rol de `admin`.
* `anna@example.com` que té el rol de `moderator`.
* `elia@example.com` que té el rol de `wanner`.
* `kevin@example.com` que té el rol de `wanner`.

#### SQLite

Per a fer servir SQLite cal definir la ruta relativa del fitxer de base de dades amb el paràmetre `SQLITE_FILE_RELATIVE_PATH` del fitxer de configuració. Aquesta base de dades s'ha de crear a partir de l'script [0_tables.sql](./sqlite/0_tables.sql). Tens una d'exemple creada amb les dades del fitxer [1_mock_data.sql](./sqlite/1_mock_data.sql). 

#### Postgres

Per a fer servir Postgres s'ha de definir la cadena de connexió amb el paràmetre `SQLALCHEMY_DATABASE_URI`. A la carpeta [postgres](./postgres/) hi ha els fitxers SQL per crear les taules i afegir-hi dades de prova.

El fitxer [docker-compose-postgres.yml](./docker-compose-postgres.yml) permet iniciar un contenidor amb Postgres. Quan s'inicia per 1a vegada, la base de dades es crea amb els fitxers SQL de la carpeta [postgres](./postgres/)

#### MySQL

Per a fer servir MySQL s'ha de definir la cadena de connexió amb el paràmetre `SQLALCHEMY_DATABASE_URI`. A la carpeta [mysql](./mysql/) hi ha els fitxers SQL per crear les taules i afegir-hi dades de prova.

El fitxer [docker-compose-mysql.yml](./docker-compose-mysql.yml) permet iniciar un contenidor amb MySQL. Quan s'inicia per 1a vegada, la base de dades es crea amb els fitxers SQL de la carpeta [mysql](./mysql/)

### Fitxer de configuració

Crea un fitxer `.env` amb els paràmetres de configuració. Pots fer servir el fitxer [.env.exemple](./.env.exemple).

## Run des de terminal

Executa:

    flask --debug run

I obre un navegador a l'adreça: [http://127.0.0.1:5000](http://127.0.0.1:5000).

Aquesta comanda executa el codi de [wsgi.py](./wsgi.py).

## Docker

Tot l'aplicatiu és pot executar amb el fitxer [docker-compose.yml](./docker-compose.yml). Cal fer servir un fitxer de configuració propi anomenat `env.docker`. En el cas de fer servir postgres, la cadena de connexió ha de fer servir el nom del contenidor com adreça de la base de dades, és a dir, el valor de `SQLALCHEMY_DATABASE_URI` ha de ser `postgresql://user:patata@postgres:5432/userdb`.

## Debug amb Visual Code

Des de l'opció de `Run and Debug`, crea un fitxer anomenat `launch.json` amb el contingut següent:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "WANNAPOP",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "wsgi.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```
