import psutil

def collect_heartbeat():
    status = {}

    status["cpuIdlePct"] = 100 - psutil.cpu_percent()

    memAvail = psutil.virtual_memory().available
    memTotal = psutil.virtual_memory().total
    status["memFreePct"] = 100 * float(memAvail)/float(memTotal)
    status["memFreeBytes"] = memAvail

    return status
