from config import GOOGLE_SHEET_KEY
from services.google_sheets.api import gc
from services.google_sheets.get_cells_by_keys import get_cells_by_keys


def get_consumables():
    sheet = gc.open_by_key(GOOGLE_SHEET_KEY).sheet1

    cells = ['F3', 'G3', 'H3', 'I3', 'J3']

    data = get_cells_by_keys(sheet, cells)

    return data
