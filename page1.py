#!/usr/bin/python
import cgitb
import cgi
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
form = cgi.FieldStorage()
if form.getvalue("name"):
      name = form.getvalue("name")
      print '<h1> Hello ' + name + '! Thanks </h1><br />'

if form.getvalue("happy"):
      name = form.getvalue("name")
      print '<h1> Hello !happy  Thanks </h1><br />'
print '<form method="post" action="hello.py">'
print '<p>Name: <input type="text" name="name" /></p>'
print '<input type="checkbox" name="happy" /> Happy'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</body>'
print '</html>'
print '<h1>sample</h1>'
