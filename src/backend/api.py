import platform


class API:
    def say_hello(self):
        return "Hello from Python! - Test"

    def get_os_info(self):
        return

    def get_computer_name_info(self):
        return

    def get_architecture_info(self):
        return

    def get_python_info(self):
        version = platform.python_version()
        print(f"Python version: {version}")
        return version


if __name__ == "__main__":
    api = API()
    api.get_python_info()