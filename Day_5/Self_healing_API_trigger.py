ping_responses = [42, 55, 120, 48, 310, 405, 39]
critical_API = 0
for item in ping_responses:
    if item >100:
        critical_API += 1

if critical_API >= 3:
    print("RESTART")
else:
    print("STABLE")