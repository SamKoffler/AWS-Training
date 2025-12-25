# ============================================
# DEBUGGING SECTION – AWS CLOUDOPS PRACTICE
# ============================================

# Scenario 1: EC2 health check failure (logic bug)
# Expected: Instance should be considered healthy if CPU < 80 and status checks pass

def is_instance_healthy(cpu_utilization, system_status, instance_status):
    if cpu_utilization > 80:
        return True
    if system_status == "ok" or instance_status == "ok":
        return False
    return True
