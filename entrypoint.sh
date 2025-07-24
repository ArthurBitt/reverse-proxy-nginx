#!/bin/bash

echo ">> Usando variáveis de ambiente conforme definidas no .env..."

echo ">> Substituindo variáveis no nginx.conf..."

envsubst '
  ${WORKER_PROCESS}
  ${WORKER_CONNECTIONS}
  ${SIZE_LIMIT_PER_REQUEST}
  ${SIMULTANEOUS_CONNECTION_PER_IP}
  ${CONN_LIMIT_ZONE_SIZE}
  ${REQ_LIMIT_ZONE_SIZE}
  ${RATE_LIMIT_PER_IP}
  ${RATE_BURST}
  ${RATE_NODELAY}
  ${READ_TIMEOUT}
  ${CONNECT_TIMEOUT}
  ${SEND_TIMEOUT}
  ${NGINX_LISTEN_PORT}
  ${APPLICATION_PUBLIC_HOST}
  ${APPLICATION_PUBLIC_DOMAIN}
  ${APPLICATION_INTERNAL_HOST}
  ${APPLICATION_PORT}
  ${HSTS_MAX_AGE}
' < /etc/nginx/nginx.conf > /tmp/nginx.conf

mv /tmp/nginx.conf /etc/nginx/nginx.conf

echo ">> Validando configuração do NGINX..."
nginx -t || exit 1

echo ">> Iniciando NGINX..."
nginx -g 'daemon off;'
