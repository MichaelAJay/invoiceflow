from app.models import InvoiceData
from app.pdf_generator import generate_pdf_invoice
from fastapi import FastAPI, Request, HTTPException
from pydantic import ValidationError

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the invoice microservice"}

@app.post("/generate-invoice")
async def generate_invoice(request: Request):
    # Get the request data
    request_data = await request.json()

    try:
        # Validate the request data using Pydantic
        invoice_data = InvoiceData(**request_data)

        # Generate the PDF invoice
        pdf = generate_pdf_invoice(invoice_data.model_dump())

        # Send the email with the PDF attachment
        # ...

        return {"message": "Invoice generated and sent successfully"}
    except ValidationError as e:
        # Handle validation errors
        error_message = "Invalid request data: " + str(e)
        raise HTTPException(400, detail=error_message)