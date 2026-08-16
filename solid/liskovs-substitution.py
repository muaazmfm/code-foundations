from abc import abstractmethod, ABC

# Violation Example 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = self.height = width # set_width method changes the height

    def set_height(self, height):
        self.height = self.width = height # set_height method changes the width
# Fix
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class RectangleShape(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class SquareShape(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size * self.size

# Violation Example 2
class Document:
    def __init__(self, content):
        self.content = content

    def read_content(self):
        return self.content

class EncryptedDocument(Document):
    def __init__(self, content):
        super().__init__(content)

    def read_content(self):
        raise PermissionError("EncryptedDocument")

if __name__ == "__main__":
    document = Document("Unencrypted Document")
    print(document.read_content())
    encrypted_document = EncryptedDocument("Encrypted Document")
    print(encrypted_document.read_content())