#!/bin/bash

echo ">> Usando variáveis de ambiente conforme definidas no .env..."
echo ">> Renderizando NGINX com Jinja2..."

python3 /nginx_render.py

echo ">> Validando configuração do NGINX..."
nginx -t || exit 1

echo ">> Iniciando NGINX..."
nginx -g 'daemon off;'
