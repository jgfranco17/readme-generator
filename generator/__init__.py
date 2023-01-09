import os
from .models import MarkdownGenerator


def create_generator():
    app = MarkdownGenerator(config="config.yaml")
    print("Created Markdown generator...")
    return app
