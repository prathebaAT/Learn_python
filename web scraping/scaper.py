import requests
from bs4 import BeautifulSoup

html_text_req = requests.get('https://realpython.github.io/fake-jobs/')

print(html_text_req)

# print(r.content)

soup = BeautifulSoup(html_text_req.content, 'html.parser')
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

with open('jobs.txt', 'w') as file:
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
    
        file.write(f"Job Title: {title_element.text.strip()}\n")
        file.write(f"Company: {company_element.text.strip()}\n")
        file.write(f"Location: {location_element.text.strip()}\n")
        file.write("\n")
    

print("Job information has been written to jobs.txt")

# python_jobs = results.find_all("h2", string="Python")
# print(python_jobs)
