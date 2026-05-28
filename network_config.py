from netmiko import ConnectHandler
import datetime

device = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}

print("=" * 50)
print("  AUTOMATED BRANCH NETWORK CONFIGURATION")
print("=" * 50)
print(f"Connecting to {device['host']}...")

connection = ConnectHandler(**device)
connection.enable()
print("Connected Successfully!")

print("\nINTERFACE STATUS:")
output1 = connection.send_command('show ip interface brief')
print(output1)

print("\nDEVICE INFORMATION:")
output2 = connection.send_command('show version | include IOS|uptime')
print(output2)

print("\nROUTING TABLE:")
output3 = connection.send_command('show ip route')
print(output3)

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
report = f"""
NETWORK AUTOMATION REPORT
Generated: {timestamp}
Device: {device['host']}

INTERFACE STATUS:
{output1}

DEVICE INFO:
{output2}

ROUTING TABLE:
{output3}
"""

with open('network_report.txt', 'w') as f:
    f.write(report)

print("\nReport saved to network_report.txt")
connection.disconnect()
print("Automation Complete!")
print("=" * 50)