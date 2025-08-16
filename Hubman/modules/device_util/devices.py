import random
import string


def random_mac_address(os):
    def byte():
        return random.randint(0x00, 0xFF)

    if os == 'win':
        # Use valid OUI ranges for common Windows network adapters
        # Intel, Realtek, Broadcom ranges (first 3 bytes)
        oui_ranges = [
            (0x00, 0x1B, random.randint(0x20, 0x2F)),  # Intel range
            (0x00, 0xE0, random.randint(0x4C, 0x4F)),  # Realtek range
            (0x00, 0x10, random.randint(0x18, 0x1F)),  # Broadcom range
            (0x08, 0x00, random.randint(0x27, 0x2F)),  # Intel range
        ]
        first_three = random.choice(oui_ranges)
        mac = list(first_three) + [byte(), byte(), byte()]

    elif os == 'linux':
        # Similar hardware vendors as Windows, but include some embedded/server vendors
        oui_ranges = [
            (0x00, 0x1B, random.randint(0x20, 0x2F)),  # Intel
            (0x00, 0xE0, random.randint(0x4C, 0x4F)),  # Realtek
            (0x00, 0x15, random.randint(0x5D, 0x5F)),  # Microsoft (for some Linux VMs)
            (0x52, 0x54, 0x00),  # QEMU/KVM virtual machines
        ]
        first_three = random.choice(oui_ranges)
        mac = list(first_three) + [byte(), byte(), byte()]

    elif os == 'mac':
        # Apple OUI ranges
        apple_ouis = [
            (0x00, 0x16, 0xCB),
            (0x00, 0x1F, 0xF3),
            (0x00, 0x23, 0xDF),
            (0x00, 0x25, 0x00),
            (0x28, 0xCF, 0xDA),
            (0x3C, 0x15, 0xC2),
        ]
        first_three = random.choice(apple_ouis)
        mac = list(first_three) + [byte(), byte(), byte()]

    else:
        # Completely random for unknown OS
        mac = [byte() for _ in range(6)]

    return ':'.join(f'{b:02x}' for b in mac)


def random_device_name(os):
    if os == 'win':
        # Windows computer names: DESKTOP/LAPTOP/PC-XXXXXXX
        prefixes = ['DESKTOP', 'LAPTOP', 'PC', 'WORKSTATION']
        suffix_length = random.randint(6, 8)
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=suffix_length))
        return f'{random.choice(prefixes)}-{suffix}'

    elif os == 'linux':
        # Linux hostnames are more varied
        patterns = [
            # username-device pattern
            lambda: f"{''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))}-{''.join(random.choices(['desktop', 'laptop', 'server', 'workstation']))}",
            # distro-inspired names
            lambda: f"{''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))}-{''.join(random.choices(string.digits, k=random.randint(2, 4)))}",
            # simple hostname
            lambda: ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 12))),
        ]
        return random.choice(patterns)()

    elif os == 'mac':
        # Mac names: often "Name's Device" or just device type
        patterns = [
            # User's Device format
            lambda: f"{''.join(random.choices(string.ascii_letters, k=random.randint(4, 8)))}{'s ' if random.choice([True, False]) else ' '}{''.join(random.choices(['MacBook Pro', 'MacBook Air', 'iMac', 'Mac Studio', 'Mac mini']))}",
            # Just device name
            lambda: random.choice(['MacBook Pro', 'MacBook Air', 'iMac', 'Mac Studio', 'Mac mini']),
            # Device with number
            lambda: f"{''.join(random.choices(['MacBook Pro', 'MacBook Air', 'iMac']))} {''.join(random.choices(string.digits, k=random.randint(1, 2)))}",
        ]
        name = random.choice(patterns)()
        # Clean up any double spaces
        return ' '.join(name.split())

    else:
        # Generic device name
        return f"device-{''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))}"
