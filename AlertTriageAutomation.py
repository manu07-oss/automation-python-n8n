def triage(alert):
    
    if alert["severity"] == "critical":
        team = "CSOC-P1"

    elif alert["severity"] == "high":
        team = "Security-Team"

    else:
        team = "Operations"

    return team


alert = {
 "event":"failed_logins",
 "severity":"critical"
}

print(triage(alert))
