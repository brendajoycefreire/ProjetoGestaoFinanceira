from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bem-vindo(a) ao Porkin! O seu melhor aplicativo de gestão financeira e controle de gastos."}