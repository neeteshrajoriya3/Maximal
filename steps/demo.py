import importlib
import steps.  # Your config module

importlib.reload(config)  # Reloads the module and forces fresh values
self.config = config.load_config()  # Reload config from the module