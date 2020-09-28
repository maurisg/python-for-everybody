import urllib.request
import urllib.parse
import urllib.error
# http://data.pr4e.org/romeo.txt

try:
    url = input('Enter URL: ')
    html_content = urllib.request.urlopen(url).read()
    html_content = html_content.decode()

    print(html_content[:3000])
    print(len(html_content))

except:
    print("ERROR: The URL is improperly formatted or non-existent.")
