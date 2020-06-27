#!/bin/bash

echo "Digite o diretorio do arquivo js"
read arquivo;
PRIMEIRA=$(js60 $arquivo)
SEGUNDA=$PRIMEIRA

js60 $arquivo

for (( ; ; ))
do
	SEGUNDA=$(js60 $arquivo)
	if [ "$PRIMEIRA" != "$SEGUNDA" ];
	then
		clear
		js60 $arquivo 
		PRIMEIRA=$SEGUNDA
	fi
done

