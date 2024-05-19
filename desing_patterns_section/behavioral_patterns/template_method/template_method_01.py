from abc import ABC, abstractmethod


# Template Method class
class Compiler(ABC):
    def compile(self):
        self.collect_sources()
        self.compile_to_bytecode()
        self.package()

    @abstractmethod
    def collect_sources(self):
        pass

    @abstractmethod
    def compile_to_bytecode(self):
        pass

    @abstractmethod
    def package(self):
        pass


class IOSCompiler(Compiler):
    def collect_sources(self):
        print("Collecting Swift source files for iOS...")

    def compile_to_bytecode(self):
        print("Compiling Swift code to bytecode for iOS...")

    def package(self):
        print("Packaging the compiled code into an iOS app bundle...")


class AndroidCompiler(Compiler):
    def collect_sources(self):
        print("Collecting Java/Kotlin source files for Android...")

    def compile_to_bytecode(self):
        print("Compiling Java/Kotlin code to bytecode for Android...")

    def package(self):
        print("Packaging the compiled code into an APK...")


# Client code
if __name__ == "__main__":
    ios_compiler = IOSCompiler()
    android_compiler = AndroidCompiler()

    print("Compiling for iOS:")
    ios_compiler.compile()

    print("\nCompiling for Android:")
    android_compiler.compile()
