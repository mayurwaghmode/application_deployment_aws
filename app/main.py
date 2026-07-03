from fastapi import FastAPI

app = FastAPI(title="Employee Management API")

@app.get("/")
def home():
  return { "message": "Welcome to Employee Management API" }
  
@app.get("/health")
  def health():
    return { "status": "healthy" }
