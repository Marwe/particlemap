#!/usr/bin/env python

import argparse
from geojson import Polygon
#from numpy import linspace
import numpy as np
from geojson import Feature, FeatureCollection

parser = argparse.ArgumentParser(description='generate a GeoJSON polygon grid between coordinates x,y X,Y with either side length definition or number of rows/cols')
parser.add_argument('-x', '--xmin', type=float, default=9, dest='xmin',
                   help='area definition: xmin')
parser.add_argument('-X', '--xmax', type=float, default=10, dest='xmax',
                   help='area definition: xmax')
parser.add_argument('-y', '--ymin', type=float, default=48, dest='ymin',
                   help='area definition: ymin')
parser.add_argument('-Y', '--Ymax', type=float, default=49, dest='ymax',
                   help='area definition: ymax')
parser.add_argument('-a', '--xlen', type=float, default=0.1, dest='xlen',
                   help='side length: xlen')
parser.add_argument('-b', '--ylen', type=float, default=0.1, dest='ylen',
                   help='side length: ylen')
parser.add_argument('-c', '--ncols', type=int, default=None, dest='ncols',
                   help='number of cols (x,X), overrides xlen')
parser.add_argument('-r', '--nrows', type=int, default=None, dest='nrows',
                   help='number of rows (y,Y), overrides ylen')

args = parser.parse_args()


# generate sequences
xseq,nx=np.linspace(args.xmin,args.xmax,(args.xmax-args.xmin)/args.xlen+1,retstep=True)
#clip: last element = max
xseq[-1]=args.xmax
yseq,ny=np.linspace(args.ymin,args.ymax,(args.ymax-args.ymin)/args.ylen+1,retstep=True)
yseq[-1]=args.ymax


if args.ncols is not None:
    xseq,nx=np.linspace(args.xmin,args.xmax,args.ncols+1,retstep=True)
if args.nrows is not None:
    yseq,ny=np.linspace(args.ymin,args.ymax,args.nrows+1,retstep=True)


farr=[]
for xi in range(len(xseq)-1):
    for yi in range(len(yseq)-1):
        farr.append(
            Feature(geometry=Polygon([[
                (xseq[xi], yseq[yi]),
                (xseq[xi], yseq[yi+1]),
                (xseq[xi+1], yseq[yi+1]),
                (xseq[xi+1], yseq[yi]),
                (xseq[xi], yseq[yi])
            ]]),properties={"xyid":str(xi)+" "+str(yi)})
         )

fc=FeatureCollection(farr)
print(fc)

