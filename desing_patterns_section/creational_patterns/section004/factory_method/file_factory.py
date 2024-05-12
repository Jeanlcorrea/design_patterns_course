from abc import ABC, abstractmethod


# Interface para o leitor de arquivo
class FileReader(ABC):
    @abstractmethod
    def read(self, file_path: str):
        pass


# Implementação concreta para leitura de arquivos CSV
class CsvFileReader(FileReader):
    def read(self, file_path: str):
        print(f"Reading CSV file: {file_path}")


# Implementação concreta para leitura de arquivos JSON
class JsonFileReader(FileReader):
    def read(self, file_path: str):
        print(f"Reading JSON file: {file_path}")


# Factory Method na classe abstrata
class FileReaderFactory(ABC):
    @abstractmethod
    def create_reader(self) -> FileReader:
        pass


# Factory Method concreto para criar leitores de arquivos CSV
class CsvFileReaderFactory(FileReaderFactory):
    def create_reader(self) -> FileReader:
        return CsvFileReader()


# Factory Method concreto para criar leitores de arquivos JSON
class JsonFileReaderFactory(FileReaderFactory):
    def create_reader(self) -> FileReader:
        return JsonFileReader()


# Cliente usando Factory Method
if __name__ == '__main__':
    csv_reader_factory = CsvFileReaderFactory()
    json_reader_factory = JsonFileReaderFactory()

    csv_reader = csv_reader_factory.create_reader()
    json_reader = json_reader_factory.create_reader()

    csv_reader.read('data.csv')
    json_reader.read('data.json')
