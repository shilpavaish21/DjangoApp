import sqlite3
  from bottle import route, run, template



 host = '169.254.173.16'
 db = sqlite3.connect('C:\Users\SIDDHESH VAISH\AppData\Local\Programs\Python\Python37\Scripts\mysite\db.sqlite3')
 c = db.cursor()

 @route('/')
 def index():


    response = "<head><meta http-equiv='refresh' content='5'></head>"

    c.execute("SELECT * FROM "Sample Data - 20190907" ORDER BY tdate, ttime DESC LIMIT 12")
    data = c.fetchall()
    response += template('/home/pi/Desktop/DB/blind_logs.tpl', rows=data)

    return response
    run(host=host, port=86)
