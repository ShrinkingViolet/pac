import os
import re
# main
with open('proxy.pac', 'r') as f:
    proxy = re.findall(r'  "(.*)"',f.read())

with open('index.html', 'w') as f:
    wt = ''
    for i in proxy:
        wt = '''<span class="line">    <span class="attr">&quot;'''+i+'''&quot;:</span> <span class="number">1</span>,</span><br>''' + wt
    with open('index.html.tmp', 'r') as t:
        f.write(t.read().replace('$$--$$', wt))