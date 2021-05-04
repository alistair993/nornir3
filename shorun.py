from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nornir = InitNornir('nornir_config.yml')

result = nornir.run(netmiko_send_command, command_string="show run")#
print_result(result)
