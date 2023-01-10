import os
import argparse
from .models import MarkdownGenerator


def config():    
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", "-t",
                        type=str,  
                        default="Project Title", 
                        help="Title of project")
    parser.add_argument("--style", "-s",
                        type=str,
                        required=True,
                        help="Choose from \'standard\' or \'minimal\'")
    args = parser.parse_args()
    return args
    

def create_generator() -> MarkdownGenerator:
    """
    Creates an instance of the generator app.

    Returns:
        MarkdownGenerator: Markdown generator app
    """
    app_config = config()
    app = MarkdownGenerator(title=app_config.title, style=app_config.style)
    print("Created Markdown generator...")
    return app
