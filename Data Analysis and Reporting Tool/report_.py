import statistics
import sys
import os
import webbrowser
from statistics import mean
def Calculate(lst_float):
    results = []
    print(lst_float)
    maxum = max(lst_float)
    results.append(maxum)
    minum = min(lst_float)
    results.append(minum)
    avg = mean(lst_float)
    results.append(avg)
    median = statistics.median(lst_float)
    results.append(median)
    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        os.chdir(".")
        if os.path.exists(out_file):
            os.remove(out_file)
        html_file = open(out_file, "w")

        with open(in_file, "r") as file:
            str1 = file.readline()

        html_file.write("<h1>Parametrs: </h1>")
        list_1 = str1.split(",")
        lst_float = []
        for i in list_1:
            lst_float.append(float(i))
        Calculate(lst_float)
        html_file.write("<ou>")
        html_file.write("<li><b>Maximum is </b>" + str(Calculate(lst_float)[0]) + "</li>")
        html_file.write("<li><b>Minimum is </b>" + str(Calculate(lst_float)[1]) + "</li>")
        html_file.write("<li><b>Average is </b>" + str(Calculate(lst_float)[2]) + "</li>")
        html_file.write("<li><b> std.dev. </b> " + str(Calculate(lst_float)[3]) + "</li>")
        html_file.write("</ou>")
        html_file.close()
        webbrowser.open("file://" + os.getcwd() + "/" + out_file)