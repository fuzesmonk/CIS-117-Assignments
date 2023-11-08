'''
Write a program that takes the NAS website url:  http://www.nasonline.org, downloads the HTML document, and decodes it into a string.
Create a list of the topics under review which include:  research, climate, evolution, cultural and leadership.
To provide additional insight to the bizops team, include an additional topic of your selection to the review list.
Determine the number of occurrences of each topic that appears on the webpage.
Provide a report summary that specifies the topic of interest and the number of times that the subject presents on the NAS website.
Import the datetime module to generate the date of your report run. Print this date in your run output.
'''

#IMPORTANT: Ran in Python 3.8
import datetime
import requests
from html.parser import HTMLParser
'''
#DO NOT TOUCH:
#THIS SECTION FIXES THE UNSAFE LEGACY RENEGOTIATION DISABLED ERROR

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.options |= ssl.OP_NO_SSLv2
ssl_context.options |= ssl.OP_NO_SSLv3
ssl_context.options |= ssl.OP_NO_COMPRESSION
ssl_context.options |= ssl.OP_SINGLE_DH_USE
ssl_context.options |= ssl.OP_SINGLE_ECDH_USE
ssl_context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_COMPRESSION
'''

class URL():
    def Fetcher(self, FetchedURL):
        try:
            response = requests.get(FetchedURL, verify=True, stream=True, timeout=10, allow_redirects=True)
            if response.status_code == 200:
                htmlContent = response.text

                with open('output.html', 'w', encoding='utf-8') as file:
                    file.write(htmlContent)
                    file.close()
#                print(htmlContent)
            else:
                print(f'Failed to retrieve the web page. Status code {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')

#            print(type(URLContent))

class NASParser(HTMLParser):
    def TopicCounter(self, dataFile):
        Words = ['research', 'climate', 'evolution', 'cultural', 'leadership', 'Gene Editing']
        occurrances = 0
        for topic in Words:
            if topic in dataFile:
                occurrances += dataFile.count(topic)
            print(f"The topic {topic} is mentioned {occurrances} times.")

   #Topics of Interest
with open('output.html', 'r', encoding='utf-8') as OutputFile:
    FileContents = OutputFile.read()




#Get Date of Run


def main():
    dateofRun = datetime.datetime.now()
    print(f"Ran on the date: {dateofRun}")
    urlToFetch = URL()
    urlToFetch.Fetcher("http://www.nasonline.org")
    DataContent = NASParser()
    DataContent.TopicCounter(FileContents)


if __name__ == "__main__":
    main()







