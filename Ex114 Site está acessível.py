from tabnanny import check
import urllib
import urllib.request


try:
    url = urllib.request.urlopen(str(input("URL: ")))
except urllib.request.URLError:
    print("\033[31mSite não está acessível!!\033[m")
else:
    print("\033[36mSite está acessível!!\033[m")
