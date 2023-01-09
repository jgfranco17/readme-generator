import os
import yaml
from tkinter import Tk, Entry, Button
from dataclasses import dataclass

class MarkdownGenerator(object):
    def __init__(self, config:str="config.yaml"):
        self.__filename = "README.md"
        self.__config = self.__read_config_file(config)
        self.root = Tk()
        self.root.title("Github README Generator")
        
    @property
    def filename(self) -> str:
        return self.__filename
    
    @staticmethod
    def __read_config_file(filename:str) -> dict:
        """
        Read a YAML configuration file and convert to Python dictionary.

        Args:
            filename (str): File path of YAML configuration file

        Returns:
            dict: Parsed YAML configuration dictionary
        """
        filename = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(filename):
            raise ValueError(f'Config file does not exist: {filename}')
        
        if not (filename.endswith(".yml") or filename.endswith(".yaml")):
            raise ValueError("Config file must be a YAML file format!")
        
        # Open the YAML config file
        with open(filename, "r") as file:
            configs = yaml.load(file, Loader=yaml.FullLoader)
        
        print(f'Read config file: {filename}')    
        return configs
    
    def write(self) -> None:
        pass
    
    def run(self) -> None: 
        print("Running generator!")
        
        
class Header(object):
    def __init__(self, level:int, text:str):
        if level not in (1, 2, 3):
            raise ValueError(f'UInvalid header level: {level}')
        self.__level = level
        self.__text = text

    @property
    def content(self):
        return f'{"#" * self.__level} {self.__text}'
    