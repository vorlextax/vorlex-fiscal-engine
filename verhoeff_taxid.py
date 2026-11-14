"""
VORLEX Fiscal Engine - Moadian 22-Char TaxID & Verhoeff Checksum Utility
Online Validator & CSR Tools: https://vorlex.ir/tools/taxid-validator
"""

import datetime

VERHOEFF_D = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
    [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
    [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
    [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]

VERHOEFF_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
]

VERHOEFF_INV = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]


def to_verhoeff_digits(text: str) -> str:
    return "".join(str(ord(ch)) if not ch.isdigit() else ch for ch in text.upper())


def compute_verhoeff_check_digit(numeric_str: str) -> int:
    c = 0
    for i, item in enumerate(reversed(numeric_str)):
        c = VERHOEFF_D[c][VERHOEFF_P[(i + 1) % 8][int(item)]]
    return VERHOEFF_INV[c]


def generate_moadian_tax_id(memory_id: str, serial_number: int, invoice_date: datetime.date = None) -> str:
    if invoice_date is None:
        invoice_date = datetime.date.today()
    days_since_epoch = (invoice_date - datetime.date(1970, 1, 1)).days
    date_hex = format(days_since_epoch, "05X")[-5:]
    serial_hex = format(serial_number, "010X")[-10:]
    raw_21 = f"{memory_id.upper()[:6]}{date_hex}{serial_hex}"
    check_digit = compute_verhoeff_check_digit(to_verhoeff_digits(raw_21))
    return f"{raw_21}{check_digit}"


if __name__ == "__main__":
    print("Sample TaxID:", generate_moadian_tax_id("A12B3C", 1))
