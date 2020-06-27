#!/bin/bash

js60 ./aula.js > nmude
SEGUNDA=$(cat nmude)

js60 ./aula.js

for (( ; ; ))
do	
	js60 ./aula.js > naomecher
	PRIMEIRA=$(cat naomecher)
	if [ "$PRIMEIRA" != "$SEGUNDA" ];
	then
		clear
		js60 ./aula.js 
		js60 ./aula.js > nmude
		SEGUNDA=$(cat nmude)	
	fi
done 
