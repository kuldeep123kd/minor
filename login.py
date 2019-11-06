#!/usr/bin/python2

#  from  httpd  to python  data pipeline and vise versa 
import  cgi
import  commands
print "Content-type:text/html"
print ""

#  browsing complete HTML page 
web_data=cgi.FieldStorage()
# extracting  only user and password from  above data
user=web_data.getvalue('u')
password=web_data.getvalue('p')
'''
print  commands.getoutput(user)
print  commands.getoutput('sudo mkdir  /var/www/html/'+password)

'''
if  user == 'jack' and  password  == 'xyz123' :
	print  "<a href='http://192.168.10.216/services.html'>"
	print  "Click here to go"
	print   "</a>"

else :
	print  "bad authentication.."


