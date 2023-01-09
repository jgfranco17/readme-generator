import os
from .models import MarkdownGenerator


def create_generator() -> MarkdownGenerator:
    """
    Creates an instance of the generator app.

    Returns:
        MarkdownGenerator: Markdown generator app
    """
    app = MarkdownGenerator(config="config.yaml")
    print("Created Markdown generator...")
    return app
