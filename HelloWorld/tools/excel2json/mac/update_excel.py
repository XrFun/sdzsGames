from excel2json import convertExcel

SRC_EXCEL_PATH = r"../../../resource/excel"
DEST_JSON_PATH = r"../../../resource/config"

if __name__ == '__main__':
    convertExcel(SRC_EXCEL_PATH, DEST_JSON_PATH)