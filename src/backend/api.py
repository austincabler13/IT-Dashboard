import system_info
import hardware_info
import performance_info
import storage_info
import network_info
    
class API:
    def get_system_info(self):
        return system_info.get_system_info(self)

    def get_hardware_info(self):
        return hardware_info.get_hardware_info(self)

    def get_performance_info(self):
        return performance_info.get_performance_info(self)

    def get_storage_info(self):
        return storage_info.get_storage_info(self)

def get_network_info(self):
        return network_info.get_network_info(self)