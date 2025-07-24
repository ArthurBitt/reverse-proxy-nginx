# Run Command

```docker
docker run -d \
  --name proxy \
  --env-file .env \
  -p 80:80 \
  ghcr.io/ArthurBitt/reverse-proxy-nginx:version
```


# Expected Vars

```sh
### NGINX CORE ###
WORKER_PROCESS=1                     #Número de processos worker do Nginx (geralmente igual ao número de CPUs)
WORKER_CONNECTIONS=2048              #Máximo de conexões simultâneas por worker

### REQUEST LIMITS ###
SIZE_LIMIT_PER_REQUEST=20MB         #Tamanho máximo do corpo da requisição (ex: uploads) em megabytes
SIMULTANEOUS_CONNECTION_PER_IP=10   #Limite de conexões simultâneas permitidas por IP
CONN_LIMIT_ZONE_SIZE=10M            #Memória compartilhada para controle de conexões simultâneas (ex: 10 megas)
REQ_LIMIT_ZONE_SIZE=10              #Memória compartilhada para controle do limite de requisições por segundo
RATE_LIMIT_PER_IP=10r/s             #Taxa máxima de requisições permitidas por IP (ex: 10 requisições por segundo)
RATE_BURST=20                       #Número de requisições extras permitidas em rajadas além do limite normal
RATE_NODELAY=nodelay                 #Comportamento para requisições excedentes (usar "nodelay" para rejeitar imediatamente)

### TIMEOUTS ###
READ_TIMEOUT=60s                    #Tempo máximo para Nginx esperar resposta completa do backend
CONNECT_TIMEOUT=60s                 #Tempo máximo para Nginx estabelecer conexão TCP com backend
SEND_TIMEOUT=60s                    #Tempo máximo para Nginx enviar dados para o backend (ex: uploads)

### NGINX PORT ###
NGINX_LISTEN_PORT=80                #Porta em que Nginx vai escutar as requisições HTTP

### APPLICATION CONFIG ###
APPLICATION_INTERNAL_HOST=internal  #Host interno do backend (Docker service name, IP, etc)
APPLICATION_PORT=app.port           #Porta do backend para proxy_pass
APPLICATION_PUBLIC_HOST=domain      #Host público configurado no Nginx para servir a aplicação

### HSTS CONFIG ###
HSTS_MAX_AGE=31536000               #Tempo em segundos para duração da política HSTS (ex: 1 ano)
```
