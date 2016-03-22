'''
Tempest plugin configuration for say_hi packages

@author: luzC

'''
from oslo_config import cfg
from tempest import config


service_available_group = cfg.OptGroup(
    name="service_available",
    title="Available OpenStack Services"
)

ServiceAvailableGroup = [
    cfg.BoolOpt("dluxSay", default=True,
                help="Whether or not dluxsay is expected to be available")
]

say_hi_group = cfg.OptGroup(
    name="say_hi",
    title="Say hi test variables"
)

SayHiGroup = [
    cfg.StrOpt("my_custom_variable", default="custom value",
               help="My custom variable.")
]
