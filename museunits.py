import sys
from baseConverter import numToBase


def calculate_time_units(tick):
    tick = float(tick)

    print(' > Units if X is equal to {} seconds < '.format(tick))
    print('                   {:30} {:30} {:30} {:30} {:30}'.format('secs', 'mins', 'hours', 'days', 'years'))
    print('            {:30} {:30} {:30} {:30} {:30}'.format('--------------------', '--------------------', '--------------------', '--------------------', '--------------------'))

    for i in range(0, 12):
        print('{:8} = '.format('X*6^{}'.format(i)), end=' ')

        secs = tick * (6 ** i)
        mins = secs / 60
        hours = mins / 60
        days = hours / 24
        years = days / 365

        units = [secs, mins, hours, days, years]
        for unit in units:
            rounding = 2  # max is 4, else it will do the 1e-5 thing

            unit = str(round(unit, rounding))
            sexUnit = numToBase(unit, 6, precision=rounding)

            # max is like 15 chars
            if len(str(int(float(unit)))) < 4:
                if unit.endswith('.0'):
                    unit = str(int(float(unit)))
                if sexUnit.endswith('.0'):
                    sexUnit = str(int(float(sexUnit)))
                if float(sexUnit) != 0.0:
                    print('{:15}{:15}'.format(sexUnit, '[{}]'.format(unit)), end=' ')
                    continue
            print('{:30}'.format(''), end=' ')
        print('')


# tick = 0.52154778 # normalized to the year
# tick = 0.52
# tick = 1.85
# tick = 50/27 # equal to 1.851... and is normalized to the day
tick = 175/81  # if the day were 28 hours


if len(sys.argv) > 1:
    tick = sys.argv[1]

calculate_time_units(tick)

# ------------------------------------------
# X*6^-2 ---- instant -------- centasecond
# X*6^-1 ---- snap -------------------------
# X*6^0 ----- tick ----------- second
# X*6^1 ----- moment -----------------------
# X*6^2 ----- lull ----------- minute
# X*6^3 ----- span -------------------------
# X*6^4 ----- short lapse ---- hour
# X*6^5 ----- long lapse -------------------
# X*6^6 ----- solar cycle ---- day
# X*6^7 ----- solar set --------------------
# X*6^8 ----- lunar cycle ---- month
# X*6^9 ----- lunar set --------------------
# X*6^10 ---- stellar cycle -- year
# X*6^11 ---- stellar set ------------------
# X*6^12 ----  ---------------------
# X*6^13 ---- lifetime ---------------------
# ------------------------------------------

