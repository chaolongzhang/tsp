# -*- encoding: utf-8 -*-

import random
import math
import sys

if sys.version_info.major < 3:
      import Tkinter
else:
      import tkinter as Tkinter
      
from GA import GA


class TSP_WIN(object):
      def __init__(self, aRoot, aLifeCount = 100, aWidth = 560, aHeight = 330):
            self.root = aRoot
            self.lifeCount = aLifeCount
            self.width = aWidth
            self.height = aHeight
            self.canvas = Tkinter.Canvas(
                        self.root,
                        width = self.width,
                        height = self.height,
                  )
            self.canvas.pack(expand = Tkinter.YES, fill = Tkinter.BOTH)
            self.bindEvents()
            self.initCitys()
            self.new()
            self.title("TSP")


      def initCitys(self):
            self.citys = []

            #中国34城市经纬度
            self.citys.append((116.46, 39.92))
            self.citys.append((117.2,39.13))
            self.citys.append((121.48, 31.22))
            self.citys.append((106.54, 29.59))
            self.citys.append((91.11, 29.97))
            self.citys.append((87.68, 43.77))
            self.citys.append((106.27, 38.47))
            self.citys.append((111.65, 40.82))
            self.citys.append((108.33, 22.84))
            self.citys.append((126.63, 45.75))
            self.citys.append((125.35, 43.88))
            self.citys.append((123.38, 41.8))
            self.citys.append((114.48, 38.03))
            self.citys.append((112.53, 37.87))
            self.citys.append((101.74, 36.56))
            self.citys.append((117,36.65))
            self.citys.append((113.6,34.76))
            self.citys.append((118.78, 32.04))
            self.citys.append((117.27, 31.86))
            self.citys.append((120.19, 30.26))
            self.citys.append((119.3, 26.08))
            self.citys.append((115.89, 28.68))
            self.citys.append((113, 28.21))
            self.citys.append((114.31, 30.52))
            self.citys.append((113.23, 23.16))
            self.citys.append((121.5, 25.05))
            self.citys.append((110.35, 20.02))
            self.citys.append((103.73, 36.03))
            self.citys.append((108.95, 34.27))
            self.citys.append((104.06, 30.67))
            self.citys.append((106.71, 26.57))
            self.citys.append((102.73, 25.04))
            self.citys.append((114.1, 22.2))
            self.citys.append((113.33, 22.13))

            #坐标变换
            minX, minY = self.citys[0][0], self.citys[0][1]
            maxX, maxY = minX, minY
            for city in self.citys[1:]:
                  if minX > city[0]:
                        minX = city[0]
                  if minY > city[1]:
                        minY = city[1]
                  if maxX < city[0]:
                        maxX = city[0]
                  if maxY < city[1]:
                        maxY = city[1]

            w = maxX - minX
            h = maxY - minY
            xoffset = 30
            yoffset = 30
            ww = self.width - 2 * xoffset
            hh = self.height - 2 * yoffset
            xx = ww / float(w)
            yy = hh / float(h)
            r = 5
            self.nodes = []
            self.nodes2 = []
            for city in self.citys:
                  x = (city[0] - minX ) * xx + xoffset
                  y = hh - (city[1] - minY) * yy + yoffset
                  self.nodes.append((x, y))
                  node = self.canvas.create_oval(x - r, y -r, x + r, y + r,
                        fill = "#ff0000",
                        outline = "#000000",
                        tags = "node",)
                  self.nodes2.append(node)

            

            
      def distance(self, order):
            distance = 0.0
            for i in range(-1, len(self.citys) - 1):
                  index1, index2 = order[i], order[i + 1]
                  city1, city2 = self.citys[index1], self.citys[index2]
                  distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            return distance


      def matchFun(self):
            return lambda life: 1.0 / self.distance(life.gene)


      def title(self, text):
            self.root.title(text)


      def line(self, order):
            self.canvas.delete("line") 
            for i in range(-1, len(order) -1):
                  p1 = self.nodes[order[i]]
                  p2 = self.nodes[order[i + 1]]
                  self.canvas.create_line(p1, p2, fill = "#000000", tags = "line")
 


      def bindEvents(self):
            self.root.bind("n", self.new)
            self.root.bind("g", self.start)
            self.root.bind("s", self.stop)


      def new(self, evt = None):
            self.isRunning = False
            order = range(len(self.citys))
            self.line(order)
            self.ga = GA(aCrossRate = 0.7, 
                  aMutationRage = 0.02, 
                  aLifeCount = self.lifeCount, 
                  aGeneLenght = len(self.citys), 
                  aMatchFun = self.matchFun())


      def start(self, evt = None):
            self.isRunning = True
            while self.isRunning:
                  self.ga.next()
                  distance = self.distance(self.ga.best.gene)
                  self.line(self.ga.best.gene)
                  self.title("TSP-gen: %d" % self.ga.generation)
                  self.canvas.update()


      def stop(self, evt = None):
            self.isRunning = False


      def mainloop(self):
            self.root.mainloop()


def main():
      #tsp = TSP()
      #tsp.run(10000)

      tsp = TSP_WIN(Tkinter.Tk())
      tsp.mainloop()


if __name__ == '__main__':
      main()