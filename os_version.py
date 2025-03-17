import os
import sys
import platform
from typing import Union, Dict, Any

try:
    import distro
except ImportError:
    distro = None  # The 'distro' module may not be installed

def get_os_name() -> str:
    """Returns the generic OS name."""
    return os.name  # 'posix' for Linux/macOS, 'nt' for Windows

def get_sys_platform() -> str:
    """Returns the system platform."""
    return sys.platform  # 'linux', 'darwin', 'win32'

def get_platform_system() -> str:
    """Returns the detailed OS name."""
    return platform.system()  # 'Windows', 'Linux', or 'Darwin'

def get_platform_release() -> str:
    """Returns the OS version."""
    return platform.release()

def get_platform_info() -> str:
    """Returns detailed platform information."""
    return platform.platform()

def get_linux_distribution() -> Union[Dict[str, str], str]:
    """Returns Linux distribution name and version if applicable."""
    if distro:
        return {
            "name": distro.name(),
            "version": distro.version(),
            "id": distro.id()
        }
    return "Module 'distro' not installed. Use 'pip install distro' for more details."

def get_full_system_info() -> Dict[str, Any]:
    """Returns a dictionary with all available system information."""
    return {
        "os_name": get_os_name(),
        "sys_platform": get_sys_platform(),
        "platform_system": get_platform_system(),
        "platform_release": get_platform_release(),
        "platform_info": get_platform_info(),
        "linux_distribution": get_linux_distribution() if get_sys_platform() == 'linux' else "N/A"
    }

# Test the module
if __name__ == "__main__":
    info = get_full_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")