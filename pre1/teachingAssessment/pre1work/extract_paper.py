import bs4
from bs4 import BeautifulSoup
import os

file_path = '/Users/kangli/Documents/Course/6020/mccpSpring2026/pre1/teachingAssessment/pre1work/papers/Exploring the Potential of LLMs for Serendipity Evaluation in Recommender Systems _ Proceedings of the Nineteenth ACM Conference on Recommender Systems.html'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    def clean_text(text):
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)

    # RQ1 Findings
    print("=== RQ1 Findings (sec-3) ===")
    elem = soup.find(id='sec-3')
    if elem:
        print(clean_text(elem.get_text(separator=' '))[:10000])
    else:
        print("Not found.")
    print("\n")

except Exception as e:
    print(f"Error: {e}")
