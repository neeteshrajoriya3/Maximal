import yaml


class configuration:
    @staticmethod
    def load_config_read():
        """Force reload the latest config.yaml every time it's called."""
        with open("config.yaml", "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def load_config_write():
        """function for saving data in config.yaml"""
        pass
