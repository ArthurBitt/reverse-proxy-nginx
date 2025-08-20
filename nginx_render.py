import os
from jinja2 import Environment, FileSystemLoader


def str_to_bool(val):
    return str(val).lower() in ['1', 'true', 'yes']

env = Environment(loader=FileSystemLoader('/etc/nginx/'))
template = env.get_template('nginx.conf')

context = {
    # gerais
    "WORKER_PROCESS": os.getenv("WORKER_PROCESS", "1"),
    "WORKER_CONNECTIONS": os.getenv("WORKER_CONNECTIONS", "1024"),
    "SIZE_LIMIT_PER_REQUEST": os.getenv("SIZE_LIMIT_PER_REQUEST", "10m"),
    "SIMULTANEOUS_CONNECTION_PER_IP": os.getenv("SIMULTANEOUS_CONNECTION_PER_IP", "10"),
    "CONN_LIMIT_ZONE_SIZE": os.getenv("CONN_LIMIT_ZONE_SIZE", "10m"),
    "REQ_LIMIT_ZONE_SIZE": os.getenv("REQ_LIMIT_ZONE_SIZE", "10m"),
    "RATE_LIMIT_PER_IP": os.getenv("RATE_LIMIT_PER_IP", "10r/s"),
    "RATE_BURST": os.getenv("RATE_BURST", "20"),
    "RATE_NODELAY": os.getenv("RATE_NODELAY", "nodelay"),
    "READ_TIMEOUT": os.getenv("READ_TIMEOUT", "60s"),
    "CONNECT_TIMEOUT": os.getenv("CONNECT_TIMEOUT", "10s"),
    "SEND_TIMEOUT": os.getenv("SEND_TIMEOUT", "30s"),
    "NGINX_LISTEN_PORT": os.getenv("NGINX_LISTEN_PORT", "80"),
    "APPLICATION_INTERNAL_HOST": os.getenv("APPLICATION_INTERNAL_HOST", "localhost"),
    "APPLICATION_PUBLIC_HOST": os.getenv("APPLICATION_PUBLIC_HOST", "localhost"),
    "APPLICATION_PORT": os.getenv("APPLICATION_PORT", "3000"),
    "HSTS_MAX_AGE": os.getenv("HSTS_MAX_AGE", "31536000"),

    # headers unitários
    "enable_http_connection": str_to_bool(os.getenv("ENABLE_HTTP_UPGRADE", "true")),
    "enable_connection_upgrade": str_to_bool(os.getenv("ENABLE_CONNECTION_UPGRADE", "true")),
    "enable_x_frame_options": str_to_bool(os.getenv("ENABLE_X_FRAME_OPTIONS", "true")),
    "enable_x_content_type_options": str_to_bool(os.getenv("ENABLE_X_CONTENT_TYPE_OPTIONS", "true")),
    "enable_referrer_policy": str_to_bool(os.getenv("ENABLE_REFERRER_POLICY", "true")),
    "enable_connection_header": str_to_bool(os.getenv("ENABLE_CONNECTION_HEADER", "true")),
    "enable_csp": str_to_bool(os.getenv("ENABLE_CSP", "true")),
    "enable_permissions_policy": str_to_bool(os.getenv("ENABLE_PERMISSIONS_POLICY", "true")),
    "enable_hsts": str_to_bool(os.getenv("ENABLE_HSTS", "true")),
    "enable_coep": str_to_bool(os.getenv("ENABLE_COEP", "true")),
    "enable_coop": str_to_bool(os.getenv("ENABLE_COOP", "true")),
    "enable_corp": str_to_bool(os.getenv("ENABLE_CORP", "true")),
    "enable_x_permitted_cdp": str_to_bool(os.getenv("ENABLE_X_PERMITTED_CDP", "true")),
    "enable_x_xss_protection": str_to_bool(os.getenv("ENABLE_X_XSS_PROTECTION", "true")),
}

output = template.render(context)

with open('/etc/nginx/nginx.conf', 'w') as f:
    f.write(output)
