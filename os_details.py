import os
import platform


def fetch_current_user() -> str:
    return os.getlogin()


def fetch_device_platform() -> str:
    return platform.system()
