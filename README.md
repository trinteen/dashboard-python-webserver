# dashboard-python-webserver
 Dashboard in python

Autor: Trinteen (c)2024

---

## Python 3.12 and newer
```
Download & Install: https://www.python.org/
```

## Install dependencies
```
pip install -r requirements.txt
```

## Configuration

Webserver configuration - **config.ini**
```
[webserver]
ip = "192.168.0.10" <= Set IP server
port = "8000"       <= Set specific port

[ui]
table_column = 5    <= Set column number for layout
```


Layout store (structure directory and files) in directory **dashboard**
```
\dashboard\
    \1\         <= list/slide
        1.ini   <= Button configuration file
        2.ini   <= Button configuration file
        ...
        ...
```

Structure button file
```
[A]                     <= Specific simulate key for send
name = "Button #1"      <= Name button - first line
info = "Demo button"    <= Info text - second line
font = "#ffffff"        <= Hex code font color
bacg = "#000000"        <= Hex code background color
loop = "0"              <= Number loops for send key (repeat)
```
