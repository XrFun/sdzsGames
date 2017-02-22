import os
import os.path
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import svn_update
import json
import re

FILE_EVENT = r"../../src/global/cevent.js"
EXCEL_PATH = r"../../excel"

FILTER_FILE_LIST = ["base_robot_team.xlsx"]

def svn_checkout():
    print "checkout ..."
    os.system("rm -r " + EXCEL_PATH)
    svn_update.checkout()

def to_res_path(path):
    return re.sub("excel", "res/data", path);

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def FloatToString (aFloat):
    if type(aFloat) != float:
        return ""
    strTemp = str(aFloat)
    strList = strTemp.split(".")
    if len(strList) == 1 :
        return strTemp
    else:
        if strList[1] == "0" :
            return strList[0]
        else:
            return strTemp

def table2jsn(table, jsonfilename):
    nrows = table.nrows
    ncols = table.ncols
    ensure_dir(jsonfilename)
    final_json = u"{\n\t\"list\":[\n"
    write_flag = False
    for r in range(nrows-1):
        if r < 4:
            continue
        final_json += u"\t\t "
        strTmp = u"{"
        for c in range(ncols):
            asterisk = table.cell_value(3, c)
            if asterisk != '*':
                continue
            write_flag = True
            key = table.cell_value(0, c)
            if key != "":
                strCellValue = u""
                CellObj = table.cell_value(r+1, c)
                hasField = False
                if type(CellObj) == unicode:
                    #print("unicode")
                    hasField = True
                    strCellValue = json.dumps(CellObj, ensure_ascii=False)
                elif type(CellObj) == float:
                    #print("float")
                    hasField = True
                    strCellValue = FloatToString(CellObj)
                else:
                    strCellValue = str(CellObj)
                if hasField:
                    strTmp += u"\t\""  + key + u"\":" + strCellValue
                    if c < ncols - 1:
                        strTmp += u","
                    #f.write(strTmp)
                    #f.write(u"\n\t\t")
        if len(strTmp) > 0:
            if strTmp[-1] == ",":
                strTmp = strTmp[:-1]
        strTmp += u" }"
        if len(strTmp) > 3:
            final_json += strTmp
            #f.write(u" }")
            if r < nrows-2:
                final_json += u","
                final_json += u"\n"
    final_json += u"\t]\n}\n"
    if write_flag == True:
        f = codecs.open(jsonfilename, "w", "utf-8")
        f.write(final_json)
        f.close()
        print "Create " + jsonfilename + " OK"
    return

def convertExcel(path, dest_path):
    file_list = os.listdir(path)
    for filename in file_list:
        if filename in FILTER_FILE_LIST or "~$" in filename:
            continue
        name, ext = os.path.splitext(filename)
        if ext == ".xls" or ext == ".xlsx":
            data = xlrd.open_workbook(os.path.join(path, filename))
            desttable = data.sheet_by_index(0)
            table2jsn(desttable, os.path.join(dest_path, name + ".json"))

#os.system("bash ./encryption.sh")

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        print "argv count != 2, program exit"
        print "USAGE: a.py excelfilename"
        exit(0)

    print "excel to json"

    svn_checkout()

    convertExcel(EXCEL_PATH, to_res_path(EXCEL_PATH))

    print "finish..."

