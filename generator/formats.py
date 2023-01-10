class Header(object):
    def __init__(self, level:int, text:str):
        if level not in (1, 2, 3):
            raise ValueError(f'UInvalid header level: {level}')
        self.level = level
        self.text = text

    @property
    def content(self) -> str:
        """
        The text content of the header.

        Returns:
            str: Formatted header text
        """
        return f'{"#" * self.level} {self.text}'


class Paragraph(object):
    def __init__(self, text:str):
        self.text = text
        
    @property
    def content(self) -> str:
        return f'<p>{self.text}</p>'

    
class Badge(object):
    def __init__(self, label:str, message:str, color:str, logo:str=None):
        self.label = label
        self.message = message
        self.color = color
        
        # Set badge properties
        self.__url = f'https://img.shields.io/badge/{self.label}-{self.message}-{self.color}?style=for-the-badge'
        if logo is not None:
            self.__url += f'&logo={logo.lower()}&logoColor=white'
            
    @property
    def url(self) -> str:
        return self.__url
    