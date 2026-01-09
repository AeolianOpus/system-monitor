import psutil

import GPUtil

# Shows the CPU usage percentage
def get_cpu_usage() -> int:

    return int(psutil.cpu_percent(interval=1))

# Shows the RAM usage percentage
def get_memory_usage() -> int:

    return int(psutil.virtual_memory().percent)

# Shows the DISK usage percentage
def get_disk_usage() -> int:

    return int(psutil.disk_usage('/').percent)

# Shows the GPU usage percentage
def get_gpu_usage():

    try:
        # List of GPUs detected
        gpus = GPUtil.getGPUs()

        # Return none if no gpus are found
        if not gpus:
            return None

        # Returns usage of the first GPU it finds
        return int(gpus[0].load * 100)

    except Exception:
        # Error handling
        return None