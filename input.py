from bs4 import BeautifulSoup
import requests

# mod_url = 'https://csmoodle.clevelandhighschool.org/'
# html_text = requests.get(mod_url).text
# soup = BeautifulSoup(html_text, 'html.parser')

def main():
  mod_url = 'https://csmoodle.clevelandhighschool.org/'
  html_text = requests.get(mod_url).text
  soup = BeautifulSoup(html_text, 'html.parser')
  newtext = soup.find(id='docs-internal-guid-5e158316-7fff-c059-bc16-d8a4bdf53c81').text

  return(newtext)

if __name__ == "__main__": 
  main();
