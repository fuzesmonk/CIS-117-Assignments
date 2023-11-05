import datetime
import urllib
import html.parser

class URL(urllib):
    def Fetcher(self, FetchedURL):
        print("Fetched URL:", FetchedURL)

class NASParser(html.parser):
    def handle_starttag(self, tag, attrs):
        print("Start Tag:", tag)
    def handle_endtag(self, tag):
        print("End Tag: ", tag)
    def DataHandler(self, data):
        print("Data", data)

urlToFetch = URL()
urlToFetch.Fetcher("https://www.nasonline.org/")
parser = NASParser()








