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


# Scenario 2: CloudWatch alarm evaluation bug
# Expected: Alarm should trigger when average exceeds threshold

def evaluate_alarm(metric_values, threshold):
    total = 0
    for v in metric_values:
        total += v
    avg = total / len(metric_values)

    if avg < threshold:
        return "ALARM"
    else:
        return "OK"
