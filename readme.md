# Docker Image Size

```sh
size 62.9MB
``` 

# Expected Vars

```sh
WORKER_PROCESS=                   # Número inteiro: número de processos worker do Nginx (geralmente igual ao número de CPUs)
WORKER_CONNECTIONS=               # Número inteiro: máximo de conexões simultâneas por worker

SIZE_LIMIT_PER_REQUEST=           # Tamanho máximo da requisição, ex: 20m, 50m (em megabytes, com sufixo 'm' ou 'M')
SIMULTANEOUS_CONNECTION_PER_IP=  # Número inteiro: limite de conexões simultâneas permitidas por IP
CONN_LIMIT_ZONE_SIZE=             # Tamanho de memória compartilhada para controle de conexões, ex: 10m, 20m
REQ_LIMIT_ZONE_SIZE=              # Tamanho de memória compartilhada para controle do limite de requisições, ex: 10m, 20m
RATE_LIMIT_PER_IP=                # Taxa de requisições por IP, ex: 10r/s (requests per second)
RATE_BURST=                      # Número inteiro: requisições extras permitidas em rajadas
RATE_NODELAY=                    # String: comportamento para requisições excedentes, ex: "nodelay" para rejeitar imediatamente

READ_TIMEOUT=                    # Tempo (com sufixo s para segundos), ex: 60s — tempo para resposta completa do backend
CONNECT_TIMEOUT=                 # Tempo para estabelecer conexão TCP com backend, ex: 10s
SEND_TIMEOUT=                    # Tempo para enviar dados para backend, ex: 30s

NGINX_LISTEN_PORT=               # Porta TCP que o Nginx vai escutar (ex: 80, 443)

APPLICATION_INTERNAL_HOST=       # Host interno do backend (nome do serviço Docker, IP, etc)
APPLICATION_PORT=                # Porta TCP do backend para proxy_pass
APPLICATION_PUBLIC_HOST=         # Host público configurado no Nginx para servir a aplicação

HSTS_MAX_AGE=                   # Número inteiro: duração da política HSTS em segundos (ex: 31536000 para 1 ano)

ENABLE_HTTP_UPGRADE=            # usado para alterar o protocolo para websocket
ENABLE_CONNECTION_UPGRADE=      # usado para para manter ou fechar a conexão com base na anterior# usado para para manter ou fechar a conexão com base na anterior
ENABLE_X_FRAME_OPTIONS=          # true ou false — controla cabeçalho X-Frame-Options
ENABLE_X_CONTENT_TYPE_OPTIONS=   # true ou false — controla cabeçalho X-Content-Type-Options
ENABLE_REFERRER_POLICY=          # true ou false — controla cabeçalho Referrer-Policy
ENABLE_CONNECTION_HEADER=        # true ou false — controla cabeçalho Connection
ENABLE_CSP=                     # true ou false — controla Content-Security-Policy
ENABLE_PERMISSIONS_POLICY=       # true ou false — controla Permissions-Policy
ENABLE_HSTS=                    # true ou false — habilita Strict-Transport-Security
ENABLE_COEP=                    # true ou false — habilita Cross-Origin Embedder Policy
ENABLE_COOP=                    # true ou false — habilita Cross-Origin Opener Policy
ENABLE_CORP=                    # true ou false — habilita Cross-Origin Resource Policy
ENABLE_X_PERMITTED_CDP=          # true ou false — habilita X-Permitted-Cross-Domain-Policies
ENABLE_X_XSS_PROTECTION=         # true ou false — habilita X-XSS-Protection.
```
