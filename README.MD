# MLH/mlh-flyer-generator

This is a system to automatically generate flyers for [Local Hack Day](http://localhackday.mlh.io) when given a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) with event names and venue addresses.

## Installation

You will need to have the Python Imaging Libary (PIL) installed. See https://python-pillow.github.io for information about installing PIL.

## Usage

To run this project from the root directory type the following into your command line: 

```
$ python main.py
```

## Customization

If you want to change the background image replace `base.jpg` with a desired background. To change the data modify the `data.csv` file. 

Output samples can be viewed in https://github.com/MLH/mlh-flyer-generator/tree/master/output. 
