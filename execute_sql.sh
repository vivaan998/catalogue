#!/bin/bash


for s in $(ls sql/init*.sql); do
	echo $s
	docker exec -it mysql mysql -u root -p123456  -e "$(cat $s)"
done

for s in $(ls sql/create*.sql); do
	echo $s
	docker exec -it mysql mysql -u root -p123456  -e "$(cat $s)"
done

