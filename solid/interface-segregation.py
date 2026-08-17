from abc import ABC, abstractmethod

# Bad example
class PrinterMachine(ABC):
    @abstractmethod
    def print_document(self, document):
        pass
    @abstractmethod
    def scan_document(self, document):
        pass
    @abstractmethod
    def fax(self, document):
        pass

class Printer(PrinterMachine):
    def print_document(self, document):
        print("Printer printing the document")

    def scan_document(self, document):
        raise RuntimeError('Printer does not support scanning')

    def fax(self, document):
        raise RuntimeError('Printer does not support faxing')

# Good example
class Printable(ABC):
    def print_document(self, document):
        pass

class Scannable(ABC):
    def scan_document(self, document):
        pass

class Faxable(ABC):
    def fax(self, document):
        pass

class LowEndPrinter(Printable):
    def print_document(self, document):
        print("Printer printing the document")

class HighEndPrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        print("Printer printing the document")
    def scan_document(self, document):
        print("Printer scanning the document")
    def fax(self, document):
        print("Printer faxing the document")