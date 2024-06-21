from abc import ABC, abstractmethod
class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        print("Підготовка документа до друку...")
        self.print()
        print("Документ відправлено на друк.")

class PDFDocument(Document):
    def print(self):
        print("Друк PDF документа...")

class WordDocument(Document):
    def print(self):
        print("Друк Word документа...")

class ExcelDocument(Document):
    def print(self):
        print("Друк Excel документа...")

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == 'pdf':
            return PDFDocument()
        elif doc_type == 'word':
            return WordDocument()
        elif doc_type == 'excel':
            return ExcelDocument()
        else:
            raise ValueError("Невідомий тип документа.")

if __name__ == "__main__":
    pdf_doc = DocumentFactory.create_document('pdf')
    pdf_doc.prepare_for_printing()

    word_doc = DocumentFactory.create_document('word')
    word_doc.prepare_for_printing()