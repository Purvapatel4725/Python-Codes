import requests
from bs4 import BeautifulSoup

def search_website(query, url):
    search_url = f"https://www.google.com/search?q=site%3A{url}+{query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    return results

query = input("Enter the data you want: ")
url = 'wikipedia.org'
results = search_website(query, url)

for result in results:
    print(result.get_text())


'''import requests - imports the Python requests module, which is used to send HTTP requests to a website and receive responses.
from bs4 import BeautifulSoup - imports the BeautifulSoup class from the Python bs4 module, which is used to parse HTML and XML documents.
def search_website(query, url): - defines a function named search_website that takes two parameters, query and url.
search_url = f"https://www.google.com/search?q=site%3A{url}+{query}" - creates a search URL by formatting the url and query parameters into a Google search query string.
response = requests.get(search_url) - sends a GET request to the search URL and saves the response in the response variable.
soup = BeautifulSoup(response.content, 'html.parser') - creates a BeautifulSoup object from the response content, which is the HTML of the search results page.
results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd') - finds all the HTML div elements that have both the BNeawe, s3v9rd, and AP7Wnd classes and saves them in the results variable.
return results - returns the results variable from the search_website function.
query = 'chat gpt' - sets the query variable to the string 'chat gpt'.
url = 'wikipedia.org' - sets the url variable to the string 'wikipedia.org'.
results = search_website(query, url) - calls the search_website function with the query and url parameters and saves the results in the results variable.
for result in results: - loops through each result in the results list.
print(result.get_text()) - prints the text content of each result by calling the get_text() method on the result object.'''





