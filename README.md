# sparse_cpu
sparse_cpu conteiner

sparse_cpu/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── app/
    └── main.py
# 1. проверка доступности:
    запрос
docker compose exec -it app python -c "
import httpx
r = httpx.get('http://sparse-embedder:8002/health', timeout=10)
print('status:', r.status_code)
print('body  :', r.text)
"
ответ:
status: 200
body  : {"status":"ok"}

# 2. 