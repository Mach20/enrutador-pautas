import random
import urllib.parse
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="Enrutador Aleatorio de Pautas")

VENDEDORES = [
    {"nombre": "Juan", "phone": "593992243456"},
    {"nombre": "Pepe", "phone": "593939757804"},
    {"nombre": "Juan", "phone": "593992241556"},
    {"nombre": "Pepe", "phone": "593939753454"},
    {"nombre": "Juan", "phone": "593992241456"},
    {"nombre": "Pepe", "phone": "593939723445"}
]

@app.get("/pauta-lead")
def asignar_vendedor_azar():
    vendedor_elegido = random.choice(VENDEDORES)
    phone = vendedor_elegido['phone']
    
    mensaje = "Hola, busco más información"
    mensaje_codificado = urllib.parse.quote(mensaje)
    
    link_whatsapp = f"https://api.whatsapp.com/send?phone={phone}&text={mensaje_codificado}"
    
    return RedirectResponse(url=link_whatsapp, status_code=302)
