# coding=utf-8
def getPath(path):
    dirs = "D:/pyCharmProgram/pyAppium/config"
    dirs_result="D:/pyCharmProgram/pyAppium/result"
    ini_path = dirs + "/" + "properties.ini"
    excel_path = dirs + "/" + "TestData.xlsx"
    email_path = dirs_result + "/" + "Report.html"
    log_path=dirs_result

    if path == "ini_path":
        return ini_path
    elif path == "excel_path":
        return excel_path
    elif path == "email_path":
        return email_path
    elif path=="log_path":
        return log_path
    else:

        raise u"参数错误"
