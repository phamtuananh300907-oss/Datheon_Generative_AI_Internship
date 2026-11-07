import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from task_01_structured_llm.src.extractor import InvoiceExtractor
from task_01_structured_llm.src.output_handler import (
    print_invoice_summary,
    save_invoice_to_json,
)


def run_task_01():
    sample_text = """
    INVOICE STATEMENT
    Invoice No: INV-2026-8899
    Date of Issue: 2026-11-05

    Seller Details:
    TechCorp Global Solutions Ltd.

    Customer Details:
    Datheon Enterprise AI Systems

    Itemized Description:
    1. Cloud Server Instance Setup - Quantity: 2 - Unit Price: $450.00 - Line Total: $900.00
    2. Enterprise AI API Gateway Subscription - Quantity: 1 - Unit Price: $350.00 - Line Total: $350.00

    Financial Summary:
    Subtotal Amount: $1250.00
    Applied Tax (VAT 10%): $125.00
    Grand Total Balance Due: $1375.00
    Payment Currency: USD
    """

    print("Running Task 01: Structured LLM Extractor...")

    extractor = InvoiceExtractor()
    extracted_data = extractor.extract(sample_text)

    print_invoice_summary(extracted_data)

    output_path = ROOT_DIR / "task_01_structured_llm" / "samples" / "extracted_invoice.json"

    save_invoice_to_json(
        extracted_data,
        str(output_path),
    )
    print("Task 01 completed successfully!")

if __name__ == "__main__":
    run_task_01()