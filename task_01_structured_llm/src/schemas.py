from typing import List
from pydantic import BaseModel, Field


class InvoiceItem(BaseModel):
    description: str = Field(
        ..., description="Detailed description of the product or service"
    )
    quantity: int = Field(
        ..., description="Quantity of items, must be greater than 0"
    )
    unit_price: float = Field(..., description="Price per single unit")
    total_price: float = Field(..., description="Total price for this item")


class InvoiceData(BaseModel):
    invoice_number: str = Field(
        ..., description="Unique reference code or identifier of the invoice"
    )
    vendor_name: str = Field(
        ..., description="Full legal name of the seller or vendor"
    )
    customer_name: str = Field(
        ..., description="Full legal name of the customer or buyer"
    )
    issue_date: str = Field(
        ..., description="Date of issue in YYYY-MM-DD format"
    )
    items: List[InvoiceItem] = Field(
        default_factory=list, description="List of itemized goods or services"
    )
    subtotal: float = Field(..., description="Subtotal amount before tax")
    tax_amount: float = Field(0.0, description="Total tax amount applied")
    total_amount: float = Field(..., description="Grand total amount due")
    currency: str = Field("USD", description="Currency code, e.g. USD, VND, EUR")