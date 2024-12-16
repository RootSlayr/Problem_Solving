# Link to the problem
# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true


def timeConversion(s):
    time_h, time_m, time_s = s.split(':')
    if 'am' in time_s.lower():
        if '12' in time_h:
            time_h = '00'
        time_h_24 = time_h
        time_m_24 = time_m
        time_s_24 = time_s[0:-2]
        return f"{time_h_24}:{time_m_24}:{time_s_24}"
    else:
        if '12' in time_h:
            time_h_24 = time_h
        else:
            time_h_24 = str(int(time_h)+12)
        time_s_24 = time_s[0:-2]
        return f"{time_h_24}:{time_m}:{time_s_24}"
