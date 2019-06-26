
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

from read_nba_data import *

output_file('west_top_2_standings_race.html',
            title='Western Conference Top 2 Teams Wins Race')

#rockets_data = west_top_2[west_top_2['teamAbbr'] == 'HOU']
#warriors_data = west_top_2[west_top_2['teamAbbr'] == 'GS']

#rockets_cds = ColumnDataSource(rockets_data)
#warriors_cds = ColumnDataSource(warriors_data)

west_cds = ColumnDataSource(west_top_2)

rockets_view = CDSView(source=west_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=west_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='GS')])

west_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Western Conference Top 2 Teams Wins Race, 2017-2018',
                  x_axis_label='Date', y_axis_label='Wins',
                  toolbar_location=None)

west_fig.step('stDate', 'gameWon',
              source=west_cds, view=rockets_view,
              color='#CE1141', legend='Rockets')
west_fig.step('stDate', 'gameWon',
              source=west_cds, view=warriors_view,
              color='#006BB6', legend='Warriors')

west_fig.legend.location = 'top_left'

show(west_fig)