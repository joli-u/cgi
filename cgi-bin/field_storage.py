#!/usr/bin/env python
import cgi

print("Content-Type: text/plain")
print("")

# values that field storage retrieves from query always a STRING
form = cgi.FieldStorage()
stringval = form.getvalue('a', None)
listval = form.getlist('b')

print("a: {}, b: {}".format(str(stringval), str(listval)))