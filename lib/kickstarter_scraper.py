from bs4 import BeautifulSoup
import ipdb
def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()
    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        projects[title] = {
        'image_link': project.select("div.project-thumbnail a img")[0]["src"],
        'description': project.select("p.bbcard_blurb")[0].text,
        'location': project.select("ul.project-meta span.location-name")[0].text,
        'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
        }
    return projects
projects = create_project_dict()
print(projects)
