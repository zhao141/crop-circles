#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

A = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
B = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
C = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
D = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
E = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
F = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
G = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
H = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
I = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
J = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 1, 0, 0 ], [ 0, 0, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 0, 1, 1, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
K = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 1, 0, 0, 0 ], [ 0, 1, 1, 0, 0, 0, 0 ], [ 0, 1, 0, 1, 0, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
L = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
M = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 0, 1, 1, 0 ], [ 0, 1, 0, 1, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
N = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 0, 0, 1, 0 ], [ 0, 1, 0, 1, 0, 1, 0 ], [ 0, 1, 0, 0, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
O = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
P = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
Q = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 1, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 1 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
R = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
S = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
T = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
U = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
V = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 0, 1, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
W = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 1, 0, 1, 0, 1, 0 ], [ 0, 1, 0, 1, 0, 1, 0 ], [ 0, 1, 0, 1, 0, 1, 0 ], [ 0, 0, 1, 0, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
X = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 0, 1, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 1, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
Y = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 0, 1, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
Z = [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 1, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 1, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
zero =          [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 1, 0 ], [ 0, 1, 0, 1, 0, 1, 0 ], [ 0, 1, 1, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
one =           [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 1, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
two =           [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 0, 1, 1, 0, 0 ], [ 0, 0, 1, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
three =         [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
four =          [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
five =          [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 1, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
six =           [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
seven =         [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 1, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 1, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
eight =         [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
night =         [ [ 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 1, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 1, 0 ], [ 0, 0, 0, 0, 0, 1, 0 ], [ 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0 ]  ]
space =         [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
point =         [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 1, 1, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
period =        [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 1, 1, 0 ], [ 0, 0, 0 ]  ]
comma =         [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ], [ 1, 0, 0 ]  ]
semicolon =     [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ], [ 1, 0, 0 ]  ]
colon =         [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 0, 0 ]  ]
question =      [ [ 0, 1, 0 ], [ 0, 0, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ]  ]
exclamation =   [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ]  ]
doller =        [ [ 0, 1, 0 ], [ 0, 1, 1 ], [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ], [ 1, 1, 0 ], [ 0, 1, 0 ]  ]
power =         [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 1, 0, 1 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
star =          [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 1, 1, 1 ], [ 0, 1, 0 ], [ 1, 0, 1 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
equal =         [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
plus =          [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 1, 0 ], [ 1, 1, 1 ], [ 0, 1, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
minus =         [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
underline =     [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]  ]
apos =          [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]  ]
vertical =      [ [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ]  ]
backslash =     [ [ 0, 0, 0 ], [ 1, 0, 0 ], [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ], [ 0, 0, 1 ], [ 0, 0, 0 ]  ]
slash =         [ [ 0, 0, 0 ], [ 0, 0, 1 ], [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ], [ 1, 0, 0 ], [ 0, 0, 0 ]  ]
l_parentheses = [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 0 ]  ]
r_parentheses = [ [ 0, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 1, 0 ], [ 0, 0, 0 ]  ]
l_brackets =    [ [ 0, 0, 0 ], [ 1, 1, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ], [ 1, 0, 0 ], [ 1, 1, 0 ], [ 0, 0, 0 ]  ]
r_brackets =    [ [ 0, 0, 0 ], [ 0, 1, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 1, 1 ], [ 0, 0, 0 ]  ]
l_braces =      [ [ 0, 0, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ]  ]
r_braces =      [ [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 0, 0 ]  ]
l_title =       [ [ 0, 0, 0 ], [ 0, 0, 1 ], [ 0, 1, 0 ], [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ], [ 0, 0, 0 ]  ]
r_title =       [ [ 0, 0, 0 ], [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ], [ 0, 1, 0 ], [ 1, 0, 0 ], [ 0, 0, 0 ]  ]


DOT_MATRIX = collections.OrderedDict([ 
    ('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F), ('G', G), ('H', H), ('I', I), 
    ('J', J), ('K', K), ('L', L), ('M', M), ('N', N), ('O', O), ('P', P), ('Q', Q), ('R', R), 
    ('S', S), ('T', T),  ('U', U), ('V', V), ('W', W), ('X', X), ('Y', Y), ('Z', Z),  
    ('0', zero), ('1', one), ('2', two), ('3', three), ('4', four), ('5', five),  
    ('6', six), ('7', seven), ('8', eight), ('9', night),  
    (' ', space), ('·', point), ('.', period), (',', comma), (';', semicolon), (':', colon),  
    ('?', question), ('!', exclamation), ('$', doller), ('^', power), ('*', star),  
    ('=', equal), ('+', plus), ('-', minus), ('_', underline), 
    ('\'', apos),  ('|', vertical), ('/', slash), ('\\', backslash),  
    ('(', l_parentheses), (')', r_parentheses),  ('[', l_brackets), (']', r_brackets),  
    ('{', l_braces), ('}', r_braces), ('<', l_title), ('>', r_title)
])
