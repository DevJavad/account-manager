import random


DEVICES: list[tuple[str, str]] = [
    ("SM-S908B", "Android 13"),      # Galaxy S22 Ultra
    ("SM-S918B", "Android 13"),      # Galaxy S23 Ultra
    ("SM-F946B", "Android 13"),      # Galaxy Z Fold5
    ("SM-F731B", "Android 13"),      # Galaxy Z Flip5

    ("SM-A546E", "Android 13"),      # Galaxy A54
    ("SM-A346E", "Android 13"),      # Galaxy A34
    ("SM-A145F", "Android 13"),      # Galaxy A14

    ("Pixel 7 Pro", "Android 13"),
    ("Pixel 8 Pro", "Android 14"),
    ("Pixel 7a", "Android 13"),
    ("Pixel Fold", "Android 13"),

    ("Mi 13 Pro", "Android 13"),
    ("Xiaomi 13 Ultra", "Android 13"),
    ("POCO F5 Pro", "Android 13"),
    ("Redmi Note 12 Pro", "Android 13"),

    ("CPH2447", "Android 13"),       # OnePlus 11
    ("BE2025", "Android 13"),        # OnePlus 9 Pro
    ("LE2121", "Android 12"),        # OnePlus 10 Pro

    ("RMX3701", "Android 13"),       # Realme GT Neo 5
    ("RMX3687", "Android 13"),       # Realme 11 Pro+

    ("CPH2451", "Android 13"),       # OPPO Find X6
    ("CPH2305", "Android 12"),       # OPPO Reno 8

    ("iPhone16,1", "iOS 17.2"),      # iPhone 15 Pro Max
    ("iPhone16,2", "iOS 17.2"),      # iPhone 15 Pro
    ("iPhone15,4", "iOS 17.2"),      # iPhone 15 Plus
    ("iPhone15,5", "iOS 17.2"),      # iPhone 15

    ("iPhone15,2", "iOS 17.0"),      # iPhone 14 Pro Max
    ("iPhone15,3", "iOS 17.0"),      # iPhone 14 Pro
    ("iPhone14,7", "iOS 16.6"),      # iPhone 14
    ("iPhone14,8", "iOS 16.6"),      # iPhone 14 Plus

    ("iPhone14,2", "iOS 16.5"),      # iPhone 13 Pro Max
    ("iPhone14,3", "iOS 16.5"),      # iPhone 13 Pro
    ("iPhone13,2", "iOS 16.0"),      # iPhone 12

    ("Windows PC", "Windows 11"),
    ("Windows Laptop", "Windows 11"),
    ("Gaming PC", "Windows 10"),
    ("Office Desktop", "Windows 10"),
    ("Surface Pro", "Windows 11"),
    ("Dell XPS", "Windows 11"),
    ("HP Spectre", "Windows 10"),
    ("Lenovo ThinkPad", "Windows 11"),

    ("MacBook Pro", "macOS 14.2"),
    ("MacBook Air", "macOS 14.2"),
    ("iMac", "macOS 14.1"),
    ("Mac Studio", "macOS 14.0"),
    ("Mac Mini", "macOS 13.6"),
    ("MacBook Pro", "macOS 13.5"),

    ("Linux PC", "Ubuntu 22.04"),
    ("Linux Desktop", "Ubuntu 23.10"),
    ("Gaming Linux", "Pop!_OS 22.04"),
    ("Dev Machine", "Arch Linux"),
    ("Server", "Debian 12"),
    ("Workstation", "Fedora 39"),
    ("Linux Laptop", "Linux Mint 21"),
    ("Terminal", "Kali Linux 2023.4"),

    ("Chrome Browser", "Windows 11"),
    ("Firefox Browser", "macOS 14.2"),
    ("Safari Browser", "iOS 17.2"),
    ("Edge Browser", "Windows 11"),
    ("Opera Browser", "Ubuntu 22.04"),
    ("Brave Browser", "Android 13"),
    ("Web Client", "Chrome OS"),
]


def get_device() -> tuple[str, str]:
    return random.choice(DEVICES)