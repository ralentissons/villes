from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
EXCEL_FILE = BASE_DIR / "lovac-open-data-2020-a-2026.xlsx"
JS_FILE = BASE_DIR / "com-data.js"

try:
	data_lovac = pd.read_excel(EXCEL_FILE, sheet_name="COM open data")
except ImportError as error:
	raise SystemExit("Installez la dépendance Excel avec : python -m pip install openpyxl") from error

js_data = data_lovac.to_json(orient="records", force_ascii=False, double_precision=15)
JS_FILE.write_text(f"window.COM_DATA={js_data};\n", encoding="utf-8")

print(f"{len(data_lovac)} lignes et {len(data_lovac.columns)} colonnes exportées dans {JS_FILE}")



