import requests
import mechanize
import re

url = "http://gamactf.asgama.web.id:41001/"

br = mechanize.Browser()
br.open(url)

for i in range(10):
    r = br.response().read()
    print r
    r1 = re.findall(r"KERUPUK",r)
    total = len(r1)

    br.select_form(nr=0)
    br.form['jumlah'] = str(total)
    res = br.submit()
