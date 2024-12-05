import tabula
import pandas as pd
import json

def tables_extractor(path):
    pdf_con = tabula.read_pdf(path, pages='all', multiple_tables=True)

    df = [pd.DataFrame(table) for table in pdf_con]
    
    return df

def toJson(tables):
    my_dict = {f"Table{i+1}": table.to_dict(orient='list') for i, table in enumerate(tables)}

    with open('table_extraction_assn\\tables.json', 'w') as f:
        json.dump(my_dict, f, indent=4)

    return

tables = tables_extractor(r'table_extraction_assn\sample.pdf')
toJson(tables)
print("Successfully wrote the json file...")