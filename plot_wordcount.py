import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime

print('plotting wordcount from log_wordcount.txt...')

now = datetime.datetime.now()

goal = 15000
start = '2018-04-19'
#today = now.strftime('%Y-%m-%d')
#today = '2019-05-31'
deadline = '2019-05-24'

data = pd.read_csv('log_wordcount.txt',delim_whitespace=True,header=None, usecols=[0,1,3],
    names=['date','time','words'],parse_dates=[['date','time']],index_col=[0])

estimate = pd.DataFrame(data=[0,goal],index=[pd.Timestamp('2018-04-19'),pd.Timestamp(deadline)])

plt.close('all')
fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(8,5))

data.plot(ax=ax,marker='+',ms=3,mec='k',title='Words in committed thesis files',legend=False)
estimate.plot(ax=ax,legend=False,color='r')

# ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%d'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

ax.set_xlim(pd.Timestamp(start), pd.Timestamp(deadline))
# xmax = data.max()[0]*1.05
xmax = goal*1.05
ax.set_ylim(0, xmax)

# deadlines
#ax.vlines(pd.Timestamp(today),ymin=0, ymax=xmax, color='0.6')
#ax.text(pd.Timestamp(today),data.max()[0]*0.05, 'today',
#    color='0.6',rotation=90,va='bottom',ha='right')

ax.vlines(pd.Timestamp(deadline),ymin=0, ymax=xmax, color='0.6')
ax.text(pd.Timestamp(deadline),data.max()[0]*0.05, 'deadline',
    color='0.6',rotation=90,va='bottom',ha='right')

plt.xticks(ax.get_xticks(), rotation=0,ha='center')
plt.xlabel('')
plt.tight_layout()
plt.savefig('plot_wordcount.png',dpi=300)

print('done')
