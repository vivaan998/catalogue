#!/bin/bash

sqlacodegen mysql+pymysql://root:123456@localhost:3306/db > model.py 
