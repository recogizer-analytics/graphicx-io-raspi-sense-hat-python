from sense_hat import SenseHat

import numpy as np

npcolor2 = np.array([0, 208, 193])
npcolor3 = np.array([130, 141, 152])
npcolor5 = np.array([59, 71, 82])
npcolorred = np.array([130, 41, 52])
npcoloryellow = np.array([130, 141, 52])

nplit = npcolor2
npdimmed = npcolor3
npdark = npcolor5
npred = npcolorred
npyellow = npcoloryellow

lit = nplit.asarray
dimmed = npcolor3.asarray
dark = npdark.asarray
red = npred.asarray
yellow = npyellow.asarray


def the_x_lit(sense):
    internal_draw(sense, dark, lit)


def the_x_dimmed(sense):
    internal_draw(sense, dark, dimmed)


def the_x_in_red(sense):
    internal_draw(sense, dark, red)


def the_x_in_yellow(sense):
    internal_draw(sense, dark, yellow)


def internal_draw(sense, o, X):
    x = [
        o, o, o, o, o, o, o, o,
        o, o, o, o, o, o, X, X,
        o, X, X, o, o, X, X, o,
        o, o, X, X, X, X, o, o,
        o, o, o, X, X, o, o, o,
        o, o, X, X, X, X, o, o,
        o, X, X, o, o, X, X, o,
        X, X, o, o, o, o, o, o
    ]
    sense.set_pixels(x)


def the_x_wiped(sense):
    sense.clear(dark)


def the_x_off(sense):
    sense.clear([0, 0, 0])