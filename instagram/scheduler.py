from datetime import datetime, timedelta

def generate_schedule(days=7):
    today = datetime.now()
    schedule = []

    for i in range(days):
        post_day = today + timedelta(days=i)
        schedule.append({
            "date": post_day.strftime("%Y-%m-%d"),
            "platform": "Instagram",
            "status": "Scheduled"
        })

    return schedule
