from fastapi import FastAPI, HTTPException
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from pydantic import BaseModel

app = FastAPI()

GITHUB_STATUS_URL = "https://www.githubstatus.com/api/v2/status.json"

session = requests.Session()
retries = Retry(
    total=4,                
    backoff_factor=0.1,     
    status_forcelist=[500, 502, 503, 504], 
    allowed_methods=["GET"] 
)

session.mount("https://", HTTPAdapter(max_retries=retries))
session.mount("http://", HTTPAdapter(max_retries=retries))

class StatusInfo(BaseModel):
    indicator: str
    description: str

class StatusResponse(BaseModel):
    status: StatusInfo
    page: dict

@app.get("/github-status", response_model=StatusResponse)
def read_github_status():
    try:
        response = session.get(GITHUB_STATUS_URL, timeout=(0.1)) 
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectTimeout:
        # El servidor no respondió a tiempo para establecer la conexión
        raise HTTPException(status_code=504, detail="No se pudo establecer conexión con GitHub (Timeout)")

    except requests.exceptions.ReadTimeout:
        # Se estableció conexión, pero el servidor tardó demasiado en enviar datos
        raise HTTPException(status_code=504, detail="GitHub tardó demasiado en responder (Read Timeout)")

    except requests.exceptions.HTTPError as e:
        # Errores 4xx o 5xx que NO fueron reintentados o fallaron tras reintentos
        raise HTTPException(status_code=e.response.status_code, detail=f"Error de API: {str(e)}")

    except requests.exceptions.ConnectionError:
        # Problemas de DNS, red caída, o rechazo de conexión
        raise HTTPException(status_code=502, detail="Error de red al intentar conectar con GitHub")

    except requests.exceptions.RequestException as e:
        # Otros
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")