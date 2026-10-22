import random
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
    
    mensaje = "Hola,%20busco%20más%20información%20"
    
    link_whatsapp = f"https://wa.me/{vendedor_elegido['phone']}?text={mensaje}"
    
    return RedirectResponse(url=link_whatsapp, status_code=302)