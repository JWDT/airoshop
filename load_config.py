import configparser
import warnings


class Config:

    _config: configparser.ConfigParser
    defaults: dict
    section: str

    def __init__(self, config_file_location: str = "config.ini", defaults: dict = None, section = "Config",
                 file_must_exist=False):
        self.section = section
        if defaults is None:
            defaults = dict()
        self.defaults = defaults
        try:
            self._config = configparser.ConfigParser(open(config_file_location))
        except FileNotFoundError as e:
            if file_must_exist:
                raise e
            else:
                warnings.warn("Config file specified but not found. Will still try to run.\n"
                              "Use 'file_must_exist=True' if it should not run without config.", Warning)

    def _get(self, section, option, required = False):
        try:
            value = self._config.get(section, option, fallback=self.defaults.get(option))
        except:
            value = self.defaults.get(option)
        if value or not required:
            return value
        else:
            raise KeyError(f"Config: {section} -> {option} does not exist anywhere and is required.")

    def get(self, option, required = False):
        return self._get(self.section, option, required)