from model import *
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row
from bokeh.models import HoverTool, NumeralTickFormatter

import csv
import datetime

def line_formatter(input):
    if (len(input) == 3):
        return (input[0], (input[1], float(input[2])))
    else:
        print("Malformed line item passed to line_formatter")

def import_csv(target_file = 'datafiles\LakeO_AmmoniaReports.csv'):
    with open(target_file, newline='') as csvfile:
        active_reader = csv.reader(csvfile, delimiter=',')
        for row in active_reader:
            if (not row[0] == 'Station ID'):
                formatted = line_formatter(row)
                insert_data(formatted[0], formatted[1])

def retrieve_stored_data():
    return dataStorage

def insert_data(key, input):
    # Data should be in a (Key as a string, tuple(datetime, value)) format
    if(isinstance(key, str) == False or isinstance(input, tuple) == False):
        errorMessage = "insertData failed input type verification. Data should be in a (Key as a string, List(datetime, value)) format"
        print(errorMessage)
        return False
    if key in dataStorage:
        data = dataStorage[key]
        data.append(input)
        dataStorage.update({key: data})
    else:
        dataStorage.update({key: [input]})
    return True

def delete_all_stored_data():
    dataStorage.clear()

def delete_key_stored_data(key):
    if key in dataStorage:
        del dataStorage[key]

def convert_to_datetime(input):
    date_and_time = input.split(" ")
    date_isolated = [int(d) for d in date_and_time[0].split("/")]
    time_isolated = [int(t) for t in date_and_time[1].split(":")]
    output = datetime.datetime(date_isolated[2], date_isolated[0], date_isolated[1], time_isolated[0], time_isolated[1])
    return output

def graph_stored_data():   
    today = str(datetime.date.today())
    output_file("output/"+today+".html")

    plot_list = []

    for key in dataStorage:
        x = []
        y = []

        data_chunk = dataStorage.get(key)
        for item in data_chunk:
            x.append(convert_to_datetime(item[0]))
            y.append(item[1])        

        # create a new plot with a title and axis labels
        p = figure(title=key, x_axis_label='', y_axis_label='Ammonia Level', x_axis_type="datetime", plot_height=100, tools='pan,wheel_zoom,save')

        h = HoverTool(tooltips=[('Date:', '@x{%F %H:%M}'), ('Reading:', '@y')], formatters={'@x': 'datetime'})
        p.add_tools(h)

        # add a line renderer with legend and line thickness
        p.line(x, y, legend_label="Ammonia", line_width=2)
        plot_list.append(p)

    # show the results
    show(column(*plot_list, sizing_mode='scale_width')) 
 

def main():
    import_csv()
    graph_stored_data()

if __name__== "__main__":
  main()