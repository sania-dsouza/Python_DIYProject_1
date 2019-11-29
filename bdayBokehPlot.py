from bokeh.plotting import figure, show, output_file
import calendar
import bdayMonths

# initialise the html that will have the plot displayed in
output_file("plot.html")

# load the x and y axis values
x_categories = [k for v,k in enumerate(calendar.month_name)][1:]   # remove the first entry which is blank
x = list(bdayMonths.getMonthsCount().keys())
y = list(bdayMonths.getMonthsCount().values())

# create figure
p = figure(x_range = x_categories)

p.vbar(x=x, top=y, width=0.5)

show(p)



