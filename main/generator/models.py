import os
import yaml
from tkinter import Tk, Entry, Button


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
        if not os.path.exists(filename):
            raise ValueError("Config file does not exist!")
        
        if not (filename.endswith(".yml") or filename.endswith(".yaml")):
            raise ValueError("Config file must be a YAML file format!")
        
        # Open the YAML config file
        with open(filename, "r") as file:
            configs = yaml.load(file, Loader=yaml.FullLoader)
        
        print(f'Read config file: {filename}')    
        return configs
    
    def write(self) -> None:
        pass
    
    def run() -> None: 
        print("Running generator!")
    