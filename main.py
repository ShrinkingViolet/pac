import os
import re
# main
with open('database.qaq','r') as f:
    database = re.findall(r'  "(.*)"',f.read())
database.sort(reverse = True)
with open('proxy.pac','w') as f:
    wt = ''
    for i in database:
        wt = '''    "''' + i + '''": 1,\n''' + wt
    with open('proxy.pac.tmp', 'r') as t:
        f.write(t.read().replace('$$--$$', wt))
    with open('database.qaq','w') as t:
        t.write(wt)

with open('index.html', 'w') as f:
    wt = ''
    for i in database:
        wt = '''<span class="line">    <span class="attr">&quot;'''+i+'''&quot;:</span> <span class="number">1</span>,</span><br>''' + wt
    with open('index.html.tmp', 'r') as t:
        f.write(t.read().replace('$$--$$', wt))
