import yaml

class YamlRepository():
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.source = yaml.safe_load(file)

class ZoneRepository(YamlRepository):
    def __init__(self):
        super().__init__('data/zones.yml')
        self.zones = self.source.get('zones')

class ActionRepository(YamlRepository):
    def __init__(self) -> None:
        super().__init__('data/actions.yml')
        self.actions = self.source.get('actions')