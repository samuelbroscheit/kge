import yaml

class Config:
    def __init__(self):
        # load default config file
        with open('kge/default.yaml', 'r') as file:
            self.raw = yaml.load(file)

    def load(self, filename):
        # user_config = yaml.load(file)
        raise NotImplementedError

    def folder(self):
        return self.raw['output']['folder']

    def logfile(self):
        return self.folder() + "/" + self.raw['output']['logfile']

    def log(self, msg, echo=True):
        if echo:
            print(msg)
        with open(self.logfile(), 'a') as file:
            file.writelines(msg)

    def dump(self, filename):
        with open(filename, "w+") as file:
            file.write( yaml.dump(self.raw) )
