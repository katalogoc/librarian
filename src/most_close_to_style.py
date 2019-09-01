from text_processing import most_close_to_style

weekdays = [
    'Monday',
    'Friday'
]

most_romantic = most_close_to_style('romance')

most_newsworthy = most_close_to_style('news')

weekdays = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

print('Most romantic weekday is', most_romantic(weekdays))

print('Most newsworthy weekday is', most_newsworthy(weekdays))
