<p align="center">
  <img src="images/qonvert_banner.png">
</p>

##### Universal Converter Program - Originally written for the Curtin Hackathon Case Study.
---


This program converts:
#### Mass
- Kilograms (kg)
- Pounds (lb)
- Stone (st)
#### Length
- Inches (in)
- Centimetres (cm)
- Yards (yd)
- Metres (m)
- Miles (mi)
- Kilometres (km)
#### Speed
- Miles per hour (mph)
- Kilometres per hour (kph)
- Knots (kn)
#### Currency
- United Arab Emirates Dirham (AED)
- United States Dollar (USD)
- Pound Sterling (GBP)
#### Temperature
- Fahrenheit (˚F)
- Celsius (˚C)
- Kelvin (K)
#### Date
- Gregorian Calendar
- Julian Calendar
- Julian Day Number

## Getting Started

### Prerequisites

The things needed to be installed are:
* [Python](https://www.python.org/)
* [ttkthemes](https://github.com/TkinterEP/ttkthemes), which has been used to stylize the GUI

```
pip install ttkthemes
```
* [tkcalendar](https://pypi.org/project/tkcalendar/), which has been used for the graphical date picker

```
pip install tkcalendar
```

### Usage

This program all runs from the main python file.

```
main_gui.pyw
```

Double click and a window will pop up.

![Mass](/Screenshots/1.png)

Values are calculated upon update of either values, or through the click of the main button.

![Currrency](/Screenshots/2.png)

The same user experience is shared for all tabs except the latter, the date tab.

![Date](/Screenshots/3.png)

Calculation on update is only currently working for the Julian Day Number (JDN) field. To convert from a Gregorian or Julian Calendar input, upon choosing a value for the field, click on the 'Enter' for the corresponding field.

## Built With

* [Python](https://www.python.org/) - The language used
* [tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI toolkit.
* [ttkthemes](https://github.com/TkinterEP/ttkthemes) - Used to stylize the GUI.
* [tkcalendar](https://pypi.org/project/tkcalendar/) -Used for the graphical date picker


## Authors

**Anthony Bon Louis Uy Cubillas** - [louisuy](https://github.com/louisuy)

## References

Most of these relate to Julian to Gregorian conversion, the main struggle of this project.
* [UTexas] (http://quasar.as.utexas.edu/BillInfo/JulianDatesG.html)
* [Stephen P. Morse] (https://stevemorse.org/jcal/julian.html)
* [Fourmilab] (https://www.fourmilab.ch/documents/calendar/)
* [Metric-Conversions.org] (https://www.metric-conversions.org/)

## Notes for judges. (Hello, there!)

All my work-in-progress and raw drafts and steps available for you judges to see on the Drafts/ directory, to show my thought process and ideas.

It can also be noted that the initial approach to this problem was a CLI based operation, however, as a project that can benefit the masses, the ease of a clean and simple GUI was the right approach.
