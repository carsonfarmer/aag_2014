import pandas as pd
per = pd.read_csv('UN_Global_By_Year.csv', index_col=0, parse_dates=True)

# Get `rstyle` function from here:
# http://messymind.net/2012/07/making-matplotlib-look-like-ggplot/
# Or use mpltools:
from mpltools import style
from mpltools import layout

style.use('ggplot')

# Plot
sub = per[["World","More developed", "Less developed", "Least developed"]]

fig, ax = plt.subplots(figsize=(10,6))
sub.plot(ax=ax, legend='left', linewidth=2)
ax.set_ylabel('Percentage Urban')
#rstyle(ax)
fig.savefig('un_global_percent.png')

# A few more numbers to play around with
tot = pd.read_csv('global_pop.csv', index_col=0, parse_dates=True)
tot1 = tot[["Total Population", "Urban Population", "Rural Population"]]/1000
tot2 = tot[["Percentage Rural", "Percentage Urban"]]

fig, ax = plt.subplots(figsize=(6,6))
tot1.plot(ax=ax, linewidth=2)
ax.set_ylabel('Population (millions)')
#rstyle(ax)
fig.savefig('unknown1.png')

fig, ax = plt.subplots(figsize=(6,6))
tot2.plot(ax=ax, linewidth=2)
ax.set_ylabel('Percentage')
#rstyle(ax)
fig.savefig('unknown2.png')


import pandas as pd
from ggplot import *
df = pd.read_csv('urban_by_lat.csv')
pop = pd.melt(df, id_vars=("Latitude"), var_name="Year", value_name="Population")
ggplot(aes(x="Population", y="Latitude", color="Year"), data=pop) + geom_line()


