import time

min_epoch=60
hr_epoch=60*60
day_epoch=60*60*24
year_epoch=60*60*24*365

cur_epoch=time.time()

yrs_elapsed=cur_epoch//year_epoch
cur_year=1970+yrs_elapsed

sec_remaining_this_year = cur_epoch%year_epoch
days_in_this_year = sec_remaining_this_year // day_epoch

sec_remaining_today = sec_in_this_year % day_epoch
hrs_in_today =  sec_remaining_today // hr_epoch

sec_remaining_this_hr = sec_remaining_today % hr_epoch
mins_in_this_hr = sec_in_this_hr//min_epoch

sec_in_this_min = sec_in_this_hr%min_epoch

#print hrs_in_today, mins_in_this_hr, sec_in_this_min
#print int(cur_year)
print "Current year is: ", int(cur_year)
print "Days in this year: ", days_in_this_year
print "hrs: ", hrs_in_today
print "minutes: ", mins_in_this_hr
print "seconds: ", sec_in_this_min



