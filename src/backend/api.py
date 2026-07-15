import platform


class API:
    def say_hello(self):
        return "Hello from Python! - Test"

    def get_os_info(self):
        return platform.system()

    def get_computer_name_info(self):
        return platform.node

    def get_architecture_info(self):
        return platform.architecture()[0]

    def get_python_info(self):
        return platform.python_version()