CREATE DATABASE db;

CREATE USER 'webserver'@'%' IDENTIFIED BY 'webserver';
GRANT CREATE ON db.* TO 'webserver'@'%';
GRANT DELETE ON db.* TO 'webserver'@'%';
GRANT INSERT ON db.* TO 'webserver'@'%';
GRANT SELECT ON db.* TO 'webserver'@'%';
GRANT UPDATE ON db.* TO 'webserver'@'%';