import requests, re, sys

if sys.version_info[0] == 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve
links = sys.argv[1:]
downloadlink = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=47.0&x=id%3D{}%26installsource%3Dondemand%26uc"
extensionids = []
regexx = re.compile("http[s]?.+\/(?P<lastpart>.+)")
requests.packages.urllib3.disable_warnings()
for link in links:
    extensionids.append(regexx.search(link).group("lastpart"))
for extensionid in extensionids:
    link = downloadlink.format(extensionid)
    extensiondownload = requests.get(link,verify=False,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"}).url
    urlretrieve(extensiondownload,"{}.crx".format(extensionid))