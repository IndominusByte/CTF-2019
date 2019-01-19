from re import findall
import mechanize,requests,qrtools,time

start_time = time.time()
url = "http://chall.ctfs.me:8002/qrweb/"
br = mechanize.Browser()
br.open(url)

print br.response().read()
result = findall('<img src="(.*?)" />', br.response().read())[0]
name_file = result[4:]

img = "http://chall.ctfs.me:8002/qrweb/"+result
r = requests.get(img, allow_redirects=True)
open(name_file, 'wb').write(r.content)

qr = qrtools.QR()

qr.decode(name_file)
br.select_form(nr=0)
br.form['qr'] = qr.data
br.submit()

print br.response().read()
print "--- {} seconds ---".format((time.time() - start_time)*30)
