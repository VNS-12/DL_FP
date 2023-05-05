
import validators
import re
import socket
class URLCheck:
    def validation(self,urlvar):
        res=validators.url(urlvar)
        return res

    @staticmethod
    def ipaddress(url):
        url = url.replace("http://", "")
        url = url.replace("https://", "")

        try:
            print(socket.gethostbyname(url))

            return True
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def favicon(url):
        import socket
        try:
            import urllib.request
            from bs4 import BeautifulSoup
            f = urllib.request.urlopen(url)
            soup = BeautifulSoup(f.read())
            icon_link = soup.find("link", rel="shortcut icon")
            icon = urllib.request.urlopen(icon_link['href'])
            print(icon)

            return False
        except:
            return True


    @staticmethod
    def extractPort(input):
        numbers = re.findall('\\d+',input)
        numbers = map(int,numbers)
        print(numbers)

        try:
            print (max(numbers))
            return True
        except:
            return False


if __name__=="__main__":
    print("main")
    u=URLCheck()
    print(URLCheck.ipaddress("https://stackoverflow.com"))

