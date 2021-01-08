## Structure

```
├── install.sh              # Install the python env.
├── app.py                  # Application entry point
├── api                     # REST api definition using swagger spec.
├── sql                     # SQL statements to init the database, user and create the relative tables
├── src                      
│   ├── services
│   │   ├── session
│   │   │   ├── session.py       # python entry point 
│   │   │   ├── api.py           # REST entry point and ble print definition, it is the only place where flask is used
│   │   │   ├── core  # logic / controller
│   │   │   └── test  # unit test
│   │   ├── image
│   │   │   ├── core
│   │   │   └── test
│   │   ├── live
│   │   │   ├── core
│   │   │   └── test
│   │   ├── reader
│   │   │   ├── core
│   │   │   └── test
│   │   └── availability
│   │       ├── core
│   │       └── test
│   └── dal                # SQLAlchemy model generated automatically from the SQL statements
├── test
│   └── postman            # postmand tests
```

## How to dev in local
### Prerequisite
- Python 3.X
- Docker

## Steps
### Setup environment
#### Python and app
```
source install.sh
```  
#### Mysql via Docker
The first time in order to setup
```
 docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.0.16
```  
To stop
```
docker stop mysql
```  
To start
```
docker start mysql
```  
The connection string is:
```
mysql+pymysql://root:123456@localhost:3306/db
```
Run the sql script present under ```sql``` folder to create a database and the expected Tables.
### Start app
```
python app.py
```

## How to test in local
```
sh run_codequality.sh
```




