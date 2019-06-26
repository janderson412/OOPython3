
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

from read_nba_data import *

output_file('east_top_2_standings_race.html',
            title='Eastern Conference Top 2 Teams Wins Race')

standings_cds = ColumnDataSource(standings)

celtics_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='BOS')])
raptors_view = CDSView(source=standings_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='TOR')])

east_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Eastern Conference Top 2 Teams Wins Race, 2017-2018',
                  x_axis_label='Date', y_axis_label='Wins',
                  toolbar_location=None)

east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=celtics_view,
              color='#007A33', legend='Celtics')
east_fig.step('stDate', 'gameWon',
              source=standings_cds, view=raptors_view,
              color='#CE1141', legend='Raptors')

east_fig.legend.location = 'top_left'

show(east_fig)