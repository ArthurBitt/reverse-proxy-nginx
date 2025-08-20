FROM nginx:1.29.0-alpine-slim

LABEL maintainer="arthur@forrisk.com.br"

EXPOSE 80

# Instala bash, python3 e jinja2 (via apk, mais leve)
RUN apk add --no-cache python3 py3-jinja2 bash gettext

# Copia o nginx.conf com Jinja2 placeholders
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Copia e da permisão de execução e leitura no entrypoint
COPY --chmod=755 entrypoint.sh /entrypoint.sh

# Script que renderiza com Jinja2 no runtime
COPY nginx_render.py .