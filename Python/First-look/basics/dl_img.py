import urllib.request

def dl_jpg(url,file_path,file_name):
    full_path = file_path + file_name + ".jpg"
    urllib.request.urlretrieve(url,full_path)

url = input("Skriv inn bilde URL: ")
file_name = input("Skriv inn filnavn: ")

dl_jpg(url,'../images/',file_name)