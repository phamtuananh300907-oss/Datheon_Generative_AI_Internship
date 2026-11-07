import json
from pathlib import Path
from task_01_structured_llm.src.schemas import InvoiceData


def print_invoice_summary(data: InvoiceData) -> None:
    print("\n" + "=" * 50)
    print("INVOICE SUMMARY")
    print("=" * 50)
    print(f"Invoice No   : {data.invoice_number}")
    print(f"Vendor Name  : {data.vendor_name}")
    print(f"Customer Name: {data.customer_name}")
    print(f"Issue Date   : {data.issue_date}")
    print("-" * 50)
    print("Line Items:")
    for idx, item in enumerate(data.items, 1):
        print(
            f"  {idx}. {item.description} | Qty: {item.quantity} | "
            f"Unit Price: {item.unit_price} {data.currency} | "
            f"Total: {item.total_price} {data.currency}"
        )
    print("-" * 50)
    print(f"Subtotal    : {data.subtotal} {data.currency}")
    print(f"Tax Amount  : {data.tax_amount} {data.currency}")
    print(f"Grand Total : {data.total_amount} {data.currency}")
    print("=" * 50 + "\n")


def save_invoice_to_json(data: InvoiceData, output_file_path: str) -> None:
    file_path = Path(output_file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data.model_dump(), f, ensure_ascii=False, indent=2)

    print(f"Saved JSON output successfully to: {file_path}")