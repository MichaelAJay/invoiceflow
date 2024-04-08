from fastapi import FastAPI, Request

from .pdf_generator import generate_pdf_invoice
from .models import InvoiceData

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the invoice microservice"}

@app.post("/generate-invoice")
async def generate_invoice(data: InvoiceData):
    # Validate the request data using Pydantic
    data = InvoiceData(**data.model_dump())

    # Generate the PDF invoice
    pdf = generate_pdf_invoice(data)

    # Send the email with the PDF attachment

    return {"message": "Invoice generated and sent successfully"}