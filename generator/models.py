import os
import yaml
from tkinter import Tk, Entry, Button
from dataclasses import dataclass
from formats import Header, Paragraph, Badge

class MarkdownGenerator(object):
    def __init__(self, title:str="Project Title"):
        self.root = Tk()
        self.root.title("Github README Generator")
        self.entry = Entry(self.root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.project_title = title
    
    def write(self) -> None:
        output_directory = os.path.join(os.path.dirname(__file__), "output") 
        os.makedirs(output_directory, exist_ok=True)
        filepath = os.path.join(output_directory, "README.md")
        print("Writing README file...")
        headings = [
            Header(1, self.project_title).content,
            " ".join([Badge("status", "active", "brightgreen"), Badge("license", "MIT", "blue")]),
            
        ]
        
        with open(filepath, "w") as file:
            for heading in headings:
                file.write(heading)
                
            for 
    
    def run(self) -> None: 
        print("Running generator!")
        