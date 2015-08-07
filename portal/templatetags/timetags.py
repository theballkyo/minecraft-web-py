from django import template
import datetime
register = template.Library()

def print_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime("%d %b %Y %I:%M %p")

register.filter(print_timestamp)

@register.simple_tag
def last_login(acc_obj, name):
    try:
        tm = str(acc_obj.get(username=name).lastlogin)[:10]
    except:
        return 1
    return tm

register.filter(last_login)