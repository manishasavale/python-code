def string_ip_to_int(ip):
    ip_bin = ['{0:08b}'.format(int(octet)) for octet in ip.split('.')]
    return int(''.join(ip_bin), 2)

def find_min_subnet(ip_addr_set):
    if len(ip_addr_set) < 2:
        return 'Error'

    diff = 0
    for ip, next_ip in zip(ip_addr_set, ip_addr_set[1:]):
        ip1 = string_ip_to_int(ip)
        ip2 = string_ip_to_int(next_ip)
        diff = diff | (ip1 ^ ip2)

    diff = diff.bit_length()

    mask = ((1 << (4 * 8 - diff)) - 1) << diff
    subnet_ip = string_ip_to_int(ip_addr_set[0]) & mask
    
    # Convert the int to ipv4 string
    ip_parts = []
    for _ in range(4):
        ip_part = str(subnet_ip & 255)
        ip_parts.insert(0, ip_part)
        subnet_ip = subnet_ip >> 8
    subnet = '.'.join(ip_parts)

    return subnet

if __name__ == '__main__':
    ip_addr_set = 
    print(find_min_subnet(['172.168.1.1', '172.168.1.0', '172.168.1.1', '172.168.0.0', '172.168.0.1']))
