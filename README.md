# Python Stock Chart Drawer

This small script calls an API to get live data of current stocks and visualizes their value over time on a graph

## Executing

To run this, just execute stockPlot.py and enter the ticker symbol of a stock you want see. The API will request the data and the script will then generate the plot.

Example:
````
python .\stockPlot.py 
Enter Symbol: AAPL
````
## API

The used API is by yahoo-finance and a guide for it can be found here: https://blog.api.rakuten.net/api-tutorial-yahoo-finance/

### About this project

This was a small private project I was working on in June 2021. It is currently not documented and has no unit test.
I used this project to practice my skills with python and the communication with an API. I also wanted to practice creating plots in python with this project.
I planed to make a GUI for this, but never did, maybe I will in the future...  