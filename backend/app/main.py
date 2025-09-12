from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar rotas
from app.routes import auth_routes, agenda_routes

# Criando a aplicação FastAPI
app = FastAPI(
    title="Meu Dashboard de Vendas",
    description="API para gerenciar vendas, financeiro e automações",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois você pode restringir para o domínio do front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota inicial (teste rápido)
@app.get("/")
def home():
    return {"mensagem": "🚀 API do Dashboard funcionando!"}

# Incluir rotas
app.include_router(auth_routes.router)     # já tem prefixo no próprio arquivo
app.include_router(agenda_routes.router)   # idem

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Liberar acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "pong"}
