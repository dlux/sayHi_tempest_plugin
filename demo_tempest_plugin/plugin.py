'''
Tempest Plugin implementation

@author:luzC

'''
import os

from tempest import config
from tempest.test_discover import plugins
from demo_tempest_plugin import config as config_share



class sayHiPlugin(plugins.TempestPlugin):
    def get_opt_lists(self):
        return [(
            config_share.say_hi_group.name,
            config_share.SayHiGroup)]

    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "demo_tempest_plugin/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        config.register_opt_group(
            conf,
            config_share.service_available_group,
            config_share.ServiceAvailableGroup)
        config.register_opt_group(
            conf,
            config_share.say_hi_group,
            config_share.SayHiGroup)

