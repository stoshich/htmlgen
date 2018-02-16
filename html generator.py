# write-html.py

a = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Привет, Мир!</p></body>
</html>"""

a.write(message)
a.close()
