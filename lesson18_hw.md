#### 1. Установить PostgreSQL\
```
apt-get update
apt-get install postgresql
```
или
```
apt update
apt install postgresql postgresql-client
```

#### 2. Зайти с пользователя postgresql:
```
sudo -u postgres psql
```

#### 3. Создать базу данных, пользователя, выдать права:
```
CREATE DATABASE database_name;
CREATE USER test_user WITH PASSWORD 'qwerty123!@#';
grant all privileges on DATABASE database_name TO test_user;
```

#### 4. Поправить конфиг:
в файле postgresql.conf поменять:
```
listen_addresses = '*'
```
в файле pg_hba.conf внизу:
``` 
# Database administrative login by Unix domain socket
local   all             postgres                                peer
host    all             all             0.0.0.0/0               scram-sha-256

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            scram-sha-256
host    replication     all             ::1/128                 scram-sha-256
host    all             all             0.0.0.0/0               scram-sha-256 
```
#### 5. Перезапустить PostgreSQL:
```
systemctl restart postgresql
```

#### 6. Подключиться к базе на сервере со своего компьютера, через dBeaver
