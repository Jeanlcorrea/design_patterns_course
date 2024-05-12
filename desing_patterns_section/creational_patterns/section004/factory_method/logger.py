from abc import ABC, abstractmethod


# Interface para o Logger
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


# Implementação concreta do Logger para arquivos
class FileLogger(Logger):
    def log(self, message: str):
        with open('logfile.txt', 'a') as file:
            file.write(f'{message}\n')


# Implementação concreta do Logger para console
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(message)


# Factory Method na classe abstrata
class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass


# Factory Method concreto para criar FileLogger
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


# Factory Method concreto para criar ConsoleLogger
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


# Cliente usando Factory Method
if __name__ == '__main__':
    file_logger_factory = FileLoggerFactory()
    console_logger_factory = ConsoleLoggerFactory()

    file_logger = file_logger_factory.create_logger()
    console_logger = console_logger_factory.create_logger()

    file_logger.log('Log message to file')
    console_logger.log('Log message to console')
