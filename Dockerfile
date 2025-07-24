FROM nginx:1.29.0-alpine-slim

LABEL manteiner="ArthurBitt"

EXPOSE 80

RUN apk add --no-cache bash gettext

COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]