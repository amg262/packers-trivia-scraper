from bs4 import BeautifulSoup
import requests

# Replace with the actual URL of the page
url = "https://www.funtrivia.com/en/Sports/Green-Bay-Packers-1407.html"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all question divs
questions = soup.find_all('div', itemtype="http://schema.org/Question")

for question in questions:
	# Extract the question text


	question_text = question.find('span', itemprop="name").text.strip()

	if question.find('div', itemprop="text") is None:
		question_text = "No question provided"
	else:
		question_text = question.find('div', itemprop="text").text.strip()

	# Extract the explanation text
	if question.find('div', itemprop="text") is None:
		explanation = "No explanation provided"
	else:
		explanation = question.find('div', itemprop="text").text.strip()

	print("Question:", question_text)
	print("Explanation:", explanation)
	print("---")
