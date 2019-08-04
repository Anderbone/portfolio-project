from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse


# Create your views here.
import sys
sys.path.append('../')

from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from bokehApp.models import Products
# from .models import Products
from numpy import pi
import numpy as np
import pandas as pd
from bokeh.resources import CDN

from bokeh.layouts import gridplot
from bokeh.palettes import Viridis3
from bokeh.embed import json_item
from bokeh.sampledata.iris import flowers

from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.sampledata.stocks import AAPL

from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
from scipy import interpolate, optimize


def f_2(x, A, B, C):
    return A * x * x + B * x + C

def graph(request):

    year = [1991,1993,1997,2000,2004,2006,2009,2011,2015]
    abortion = [22.7,15.2,11.6,13.5,12.2,6.2,10.8,13.1,1.9]

    p9 = figure()
    p9.square(year, abortion, size=5, color='olive', alpha=0.5)
    p8 = figure()
    p8.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="red")


    # show(column(p, select))


    # p0 = figure(title="abortion ratio", plot_width=450, plot_height=450)
    # p0.line(x = [1991,1993,1997,2000,2004,2006,2009,2011,2015], y= [22.7,15.2,11.6,13.5,12.2,6.2,10.8,13.1,1.9], line_join='round')

    p0 = figure(title='Abortion ratio in different years')
    xvals = np.linspace(year[0], year[-1], 100000)
    spl = CubicSpline(year, abortion)  # First generate spline function
    y_smooth = spl(xvals)  # then evalute for your interpolated points
    p0.line(xvals, y_smooth)


    A2, B2, C2 = optimize.curve_fit(f_2, year, abortion)[0]
    x2 = np.arange(1980, 2020, 0.01)
    y2 = A2 * x2 * x2 + B2 * x2 + C2
    p0.line(x2, y2, color='red')

    # grid = gridplot([plot, p2], p3)
    # grid = gridplot([[plot, p2], [None, p3]])
    # Store components
    # script, div = components(plot)
    # script, (p1div, p2div, p3div) = components((plot, column(p,select), p0))
    script, (p1div, p2div, p3div) = components((p0, p8, p9))
    # script, (p1div, p2div, p3div) = components((plot, p, select))
    # script, (p1div, p2div, p3div) = components((plot, p, p3))
    # script, div = components(p3)
    # return render(request, 'graph.html', {'script': script, 'div': div})
    return render(request, 'graph.html', {'script': script, 'div1': p1div, 'div2':p2div, 'div3':p3div})


def background(request):
    year = [1991, 1993, 1997, 2000, 2004, 2006, 2009, 2011, 2015]

    abortion = [22.7, 15.2, 11.6, 13.5, 12.2, 6.2, 10.8, 13.1, 1.9]

    total_birth = [19.68,18.09,16.57,14.03,12.29,12.09,11.95,11.93,12.07]
    natural_growth = [12.98,
11.45,
10.06,
7.58,
5.87,
5.28,
4.87,
4.79,
4.96,
]
    p0 = figure(title='Total birth rate and natural growth rate in China')
    xvals = np.linspace(year[0], year[-1], 100000)
    spl = CubicSpline(year, total_birth)  # First generate spline function
    y_smooth = spl(xvals)  # then evalute for your interpolated points
    p0.line(xvals, y_smooth, color='red', legend='total birth rate')

    spl = CubicSpline(year, natural_growth)  # First generate spline function
    y_smooth = spl(xvals)  # then evalute for your interpolated points
    p0.line(xvals, y_smooth, legend='natural growth rate')

    script, div = components(p0)

    return render(request, 'background.html', {'script': script, 'div': div})


def years(request):

    year = [1991,1993,1997,2000,2004,2006,2009,2011,2015]
    abortion = [22.7,15.2,11.6,13.5,12.2,6.2,10.8,13.1,1.9]

    p9 = figure()
    p9.square(year, abortion, size=5, color='olive', alpha=0.5)

    p8 = figure(title='Abortion ratio in rural/urban sites')
    p8.vbar(x=['rural', 'urban'], width=0.5, bottom=0,
           top=[7.6, 15.7], color="firebrick")

    p0 = figure(title='Abortion ratio in different years')
    xvals = np.linspace(year[0], year[-1], 100000)
    spl = CubicSpline(year, abortion)  # First generate spline function
    y_smooth = spl(xvals)  # then evalute for your interpolated points
    p0.line(xvals, y_smooth)


    A2, B2, C2 = optimize.curve_fit(f_2, year, abortion)[0]
    x2 = np.arange(1980, 2020, 0.01)
    y2 = A2 * x2 * x2 + B2 * x2 + C2
    p0.line(x2, y2, color='red')


    script, (p1div, p2div, p3div) = components((p0, p8, p9))

    return render(request, 'years.html', {'script': script, 'div1': p1div, 'div2':p2div, 'div3':p3div})


def education(request):
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")

    script, div = components(plot)

    return render(request, 'education.html', {'script': script, 'div': div})


def others(request):
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")

    script, div = components(plot)

    return render(request, 'others.html', {'script': script, 'div': div})


def conclusion(request):
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")

    script, div = components(plot)

    return render(request, 'conclusion.html', {'script': script, 'div': div})