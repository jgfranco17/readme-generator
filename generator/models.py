import os
from .formats import Header, Badge, Section

class MarkdownGenerator(object):
    def __init__(self, title:str, style:str):
        self.project_title = title
        self.style = style.lower()
        
        with open(os.path.join(os.path.dirname(__file__), "template.txt"), "r") as template_file:
            self.template_text = template_file.read()
            
        self.content_titles_options = {
            "minimal": ["About", "Setting Up", "Usage", "Authors"],
            "standard": ["About", "Prerequisites", "Usage", "Testing", "Teck Stack", "Authors"]
        }
        self.content_titles = self.content_titles_options.get(self.style)
    
    def write(self) -> str:
        output_directory = os.path.join(os.getcwd(), "output") 
        os.makedirs(output_directory, exist_ok=True)
        filepath = os.path.join(output_directory, "README.md")
        add_newline = lambda t: t + "\n\n"
        headings = [
            Header(1, self.project_title).content,
            " ".join([str(badge) for badge in (Badge("status", "active", "brightgreen"), Badge("license", "MIT", "blue"))]),
            "---"
        ]
        contents = [Section(title, self.template_text).content for title in self.content_titles]
        
        with open(filepath, "w") as file:
            for heading in headings:
                file.write(add_newline(heading))
            for content in contents:
                file.write(add_newline(content))
                
        print(f'Wrote README file to {output_directory}')
    
    def run(self) -> None: 
        print("Running README generator!")
        self.write()
        