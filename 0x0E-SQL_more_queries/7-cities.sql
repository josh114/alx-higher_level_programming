-- create database with table cities
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities (PRIMARY KEY(id), id INT UNIQUE NOT NULL AUTO_INCREMENT, state_id INT NOT NULL, name VARCHAR(256), FOREIGN KEY(state_id), REFERENCE hbtn_0d_usa.states(id));
