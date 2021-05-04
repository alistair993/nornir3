from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nornir = InitNornir('nornir_config.yml')

ntp_config = [
        "ntp server 1.1.1.1"
    ]

result = nornir.run(netmiko_send_config, config_commands=ntp_config)
print_result(result)
