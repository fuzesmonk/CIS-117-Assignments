import datetime
import urllib.request
import html.parser

class URL():
    def Fetcher(self, FetchedURL):
        FetchedURL = urllib.request.urlopen(FetchedURL)
        print("Fetched URL:", FetchedURL)

class NASParser():
    def handle_starttag(self, tag, attrs):
        print("Start Tag:", tag)
    def handle_endtag(self, tag):
        print("End Tag: ", tag)
    def DataHandler(self, data):
        print("Data", data)

urlToFetch = URL()
urlToFetch.Fetcher("https://www.nasonline.org/")
parser = NASParser()








