import datetime
import requests
import html.parser

class URL():
    def Fetcher(self, FetchedURL):
        self.FetchedURL = requests.get(FetchedURL)
        print("Fetched URL:", self.FetchedURL)
        return FetchedURL
    class NASParser():
        def __init__(self):
            URLparser = URL()
        def ServerResponse(self):
            response = URL.Fetcher()
        def handle_starttag(self, tag, attrs):
            print("Start Tag:", tag)
        def handle_endtag(self, tag):
            print("End Tag: ", tag)
        def DataHandler(self, data):
            print("Data", data)

urlToFetch = URL()
urlToFetch.Fetcher("https://www.nasonline.org/")
parser = urlToFetch.NASParser()








