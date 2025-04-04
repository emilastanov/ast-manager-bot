

def get_cells_by_keys(sheet, keys):
    values = {}

    for cell in keys:
        value = sheet.acell(cell).value
        cleaned = (
            value.replace('р.', '')
                 .replace('₽', '')
                 .replace('р', '')
                 .replace(',', '.')
                 .strip()
        )
        try:
            values[cell] = float(cleaned)
        except ValueError:
            values[cell] = cleaned

    return values

