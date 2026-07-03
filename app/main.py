from fastapi import FastAPI
import logging

app = FastAPI(title="Employee Management API")

os.makedirs('/var/log/employee-api', exist_ok=True)

logging.basicConfig(
    filename='/var/log/employee-api/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.get("/")
def home():
    logging.info("Home endpoint called")
    return {"message": "Welcome to Employee Management API"}

@app.get("/health")
def health():
    logging.info("Health endpoint called")
    return {"status": "healthy"}
