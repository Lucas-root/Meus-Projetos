#!/bin/bash

echo "Digite o diretorio do arquivo js"
read arquivo;
echo $arquivo 

js60 $arquivo > nmude
SEGUNDA=$(cat nmude)

js60 $arquivo

for (( ; ; ))
do
	js60 $arquivo > naomecher
	PRIMEIRA=$(cat naomecher)
	if [ "$PRIMEIRA" != "$SEGUNDA" ];
	then
		clear
		js60 $arquivo 
		js60 $arquivo > nmude
		SEGUNDA=$(cat nmude)
	fi
done

