from flask import Flask
from waitress import serve
import configparser
import os
import math
import pyautogui

def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    ip = eval(config.get("webserver", "ip"))
    port = eval(config.get("webserver", "port"))
    table_column = config.get("ui", "table_column")
    config_values = {
        "ip" : ip,
        "port" : port,
        "table_column" : table_column
    }
    return config_values

app = Flask(__name__, static_folder="appdata")

@app.route("/")
def dashboard():
    HTML = "<html><head><meta charset=\"UTF-8\"><meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><link rel=\"stylesheet\" href=\"/appdata/dash.css\">"
    HTML+= "<title>DASHBOARD PYTHON</title>"
    HTML+= "</head><body>"

    dashboard = os.scandir("./dashboard/")
    for pages in dashboard:
        if pages.name == "1":
            disp = "block"
        else:
            disp = "none"
        HTML+= "<div id=\"pages" + pages.name + "\" style=\"display:" + disp + ";\">"
        btn_ind = 0
        btn_data = len(os.listdir("./dashboard/" + pages.name))
        table_col = int(config["table_column"])
        table_ceil_w = math.ceil(100/table_col)
        table_row = math.ceil(btn_data/table_col)
        HTML+= "<table>"
        if btn_data > 0:
            buttons = os.listdir("./dashboard/" + pages.name)
            for tab_row in range(table_row):
                HTML+= "<tr>"
                for tab_col in range(table_col):
                    HTML+= "<td width=\"" + str(table_ceil_w) + "%\">"
                    if btn_ind <= (btn_data - 1):
                        ini = configparser.ConfigParser()
                        ini.read("./dashboard/" + pages.name + "/" + buttons[btn_ind])
                        key = ini.sections()[0]
                        name = eval(ini.get(key, "name"))
                        info = eval(ini.get(key, "info"))
                        font = eval(ini.get(key, "font"))
                        bacg = eval(ini.get(key, "bacg"))
                        loop = eval(ini.get(key, "loop"))
                        HTML+= "<div id=\"button\" class=\"on\" style=\"color:" + str(font) + ";background:" + str(bacg) + ";\">"
                        HTML+= "<a href=\"#\" onClick=\"sendkey('" + str(key) + "', '" + str(loop) + "');\" style=\"color:" + str(font) + ";\">"
                        HTML+= "<h2>" + str(name) + "</h2><h4>" + str(info) + "</h4>"
                        HTML+= "</a></div>"
                        btn_ind += 1
                    else:
                        HTML+= "<div id=\"button\" class=\"off\">"
                    HTML+= "</td>"
                HTML+= "</tr>"
        else:
            HTML+= "<tr></tr>"

        HTML+= "<tr><td class=\"table_menu\" colspan=\"" + str(table_col) + "\"><table><tr>"
        menu = os.scandir("./dashboard/")
        for menu_item in menu:
            if menu_item.is_dir:
                HTML+= "<td>"
                if menu_item.name == "1":
                    HTML+= "<div id=\"menu" + menu_item.name + "\" class=\"on\">"
                else:
                    HTML+= "<div id=\"menu" + menu_item.name + "\" class=\"off\">"
                HTML+= "<a href=\"#\" onClick=\"show('" + menu_item.name + "');\">" + menu_item.name + "</a></div></td>"
        HTML+= "</tr></table></td></tr></table></div>"
    HTML+= "<script src=\"/appdata/dash.js\"></script>"
    HTML+= "<audio id=\"audio_click\" src=\"/appdata/audio/click.mp3\"></audio>"
    HTML+= "<audio id=\"audio_switch\" src=\"/appdata/audio/switch.mp3\"></audio>"
    HTML+= "</body></html>"
    return HTML

@app.route("/command/<key>/<loop>")
def send_command(key, loop):
    if int(loop) > 0:
        for loops in loop:
            pyautogui.press(key)
    else:
        pyautogui.press(key)
    print("key=" + key + " loop=" + loop)
    return ""

if __name__ == '__main__':
    config = read_config()
    print("Server started on: http://" + str(config["ip"]) + ":" + str(config["port"]) + "/")
    serve(app, host=config["ip"], port=config["port"])