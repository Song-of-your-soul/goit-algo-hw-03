from datetime import datetime as dtdt
from datetime import timedelta


def get_days_from_today(date):
    try:
        new_date = dtdt.strptime(date, "%Y-%m-%d")
        today = dtdt.today()
        difference = today - new_date # Різниця між вказаною датою і сьогодні
        formatted_difference = difference.days # Відформатована різниця між вказаною датою і сьогодні
        return formatted_difference
    except Exception:
        print("Please enter your date as YYYY-MM-DD")





    



    