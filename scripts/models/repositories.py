import yaml
import os

class YamlRepository():

    def __init__(self, file_name):
        file_path = os.path.join(os.path.dirname(__file__), '../data', file_name)
        with open(file_path, 'r') as file:
            self.source = yaml.safe_load(file)

class ZoneRepository(YamlRepository):
    def __init__(self):
        super().__init__('zones.yml')
        self.zones = self.source.get('zones')

class ActionRepository(YamlRepository):
    def __init__(self) -> None:
        super().__init__('actions.yml')
        self.actions = self.source.get('actions')