import pandas as pd
import plotly.express as px
import argparse
import os
import webbrowser

def plot_csv_data(csv_file_path, output_html_path, data_column_numbers):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()

    df = pd.read_csv(csv_file_path, skiprows=1, encoding='utf-8')
    date_column = df.columns[0]
    if data_column_numbers:
        data_columns = [df.columns[i - 1] for i in data_column_numbers if i > 0 and i < len(df.columns)]
    else:
        data_columns = df.columns[1:]

    fig = px.line(df, x=date_column, y=data_columns, title='CSV Data Plot',
                  labels={date_column: 'Date', 'value': 'Data'})

    fig.update_layout(legend_title=first_line)

    if not output_html_path:
        output_html_path = 'output.html'
        print(f"Output HTML file not specified. Using default: {output_html_path}")

    if os.path.exists(output_html_path):
        os.remove(output_html_path)
        print(f"Existing file '{output_html_path}' found and deleted.")

    fig.write_html(output_html_path)
    webbrowser.open('file://' + os.path.realpath(output_html_path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot CSV data to HTML using Plotly.')

    parser.add_argument('csv_file_path', type=str, help='The path to the CSV file')
    parser.add_argument('output_html_path', nargs='?', default=None, help='The path to save the HTML file (optional)')
    parser.add_argument('data_column_numbers', nargs='*', type=int, help='Space-separated numbers of the data columns to plot (optional)', default=None)

    args = parser.parse_args()

    plot_csv_data(args.csv_file_path, args.output_html_path, args.data_column_numbers)
