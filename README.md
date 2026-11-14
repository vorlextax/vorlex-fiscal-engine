# VORLEX Fiscal Engine — Iran Moadian E-Invoicing & Cryptography Toolkit

Open-source utilities and technical specifications for connecting accounting and ERP software to **Iran's National Tax Administration (سامانه مودیان مالیاتی — Moadian)**, maintained by **[VORLEX](https://vorlex.ir/)**.

## Included Utilities & Free Online Tools

- **22-Character TaxID Generator (`verhoeff_taxid.py`):** Exact Verhoeff checksum implementation for `TaxID` generation (prevents Error `0300101`). Test online at [VORLEX TaxID Validator](https://vorlex.ir/tools/taxid-validator).
- **RSA-2048 CSR Generator (`OID 2.5.4.97`):** Generate compliant `public_key.txt`, `private_key.txt`, and `csr.txt` for `my.tax.gov.ir` via the free [VORLEX CSR & Tax Memory Key Generator](https://vorlex.ir/tools/csr-generator).
- **13-Digit Stuff ID & VAT Lookup:** Fast lookup for official `stuffid.tax.gov.ir` commodity/service codes and VAT rates (prevents Error `0304401` and `0303301`) via [VORLEX Stuff ID Finder](https://vorlex.ir/tools/stuff-id-finder).
- **Moadian Error Reference:** Technical solutions for [Error 4103 (Digital Signature)](https://vorlex.ir/errors/4103), `0304401`, and `0101204`.

## Quick Start (Python)

```bash
python verhoeff_taxid.py
```

```python
from verhoeff_taxid import generate_moadian_tax_id

tax_id = generate_moadian_tax_id(memory_id="A12B3C", serial_number=105)
print("22-Char Moadian TaxID:", tax_id)
```
# vorlex-fiscal-engine
نرم‌افزار و سامانه ابری ارسال صورتحساب الکترونیکی به سامانه مودیان و کارپوشه امور مالیاتی (https://vorlex.ir)
# سامانه مودیان و صورتحساب الکترونیکی VORLEX

سامانه جامع و ابری جهت اتصال سریع و امن به کارپوشه سازمان امور مالیاتی کشور و صدور صورتحساب الکترونیکی نوع اول و دوم.

🌐 **وب‌سایت رسمی سامانه:** 
[https://vorlex.ir](https://vorlex.ir)

## ویژگی‌ها و امکانات:
- صدور آنی صورتحساب نوع اول و دوم
- تولید خودکار جفت کلید RSA و گواهی مالیاتی
- پایگاه داده کامل شناسه‌های مصوب کالا و خدمات
- ارسال ایمن با استانداردهای رمزنگاری JWS

برای کسب اطلاعات بیشتر و استفاده از خدمات به پایگاه دانش و سامانه 
[VORLEX](https://vorlex.ir) مراجعه فرمایید.
