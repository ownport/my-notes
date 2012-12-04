#!/usr/bin/env python
#
# simple k-means clustering implementation
# http://pandoricweb.tumblr.com/post/8646701677/python-implementation-of-the-k-means-clustering

import sys, math, random

class Point:
    def __init__(self, coords, reference=None):
        self.coords = coords
        self.n = len(coords)
        self.reference = reference
    def __repr__(self):
        return str(self.coords)

class Cluster:
    def __init__(self, points):
        if len(points) == 0: raise Exception("ILLEGAL: empty cluster")
        self.points = points
        self.n = points[0].n
        for p in points:
            if p.n != self.n: raise Exception("ILLEGAL: wrong dimensions")
        self.centroid = self.calculateCentroid()
    def __repr__(self):
        return str(self.points)
    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        return getDistance(old_centroid, self.centroid)
    def calculateCentroid(self):
        reduce_coord = lambda i:reduce(lambda x,p : x + p.coords[i],self.points,0.0)    
        centroid_coords = [reduce_coord(i)/len(self.points) for i in range(self.n)] 
        return Point(centroid_coords)

def kmeans(points, k, cutoff):
    initial = random.sample(points, k)
    clusters = [Cluster([p]) for p in initial]
    while True:
        lists = [ [] for c in clusters]
        for p in points:
            smallest_distance = getDistance(p,clusters[0].centroid)
            index = 0
            for i in range(len(clusters[1:])):
                distance = getDistance(p, clusters[i+1].centroid)
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i+1
            lists[index].append(p)
        biggest_shift = 0.0
        for i in range(len(clusters)):
            shift = clusters[i].update(lists[i])
            biggest_shift = max(biggest_shift, shift)
        if biggest_shift < cutoff: 
            break
    return clusters

def getDistance(a, b):
    if a.n != b.n: raise Exception("ILLEGAL: non comparable points")
    ret = reduce(lambda x,y: x + pow((a.coords[y]-b.coords[y]), 2),range(a.n),0.0)
    return math.sqrt(ret)

def makeRandomPoint(n, lower, upper):
    return Point([random.uniform(lower, upper) for i in range(n)])

def main():
    num_points, dim, k, cutoff, lower, upper = 10, 2, 3, 0.5, 0, 200
    points = map( lambda i: makeRandomPoint(dim, lower, upper), range(num_points) )
    clusters = kmeans(points, k, cutoff)

    for i,c in enumerate(clusters): 
        for p in c.points:
            print " Cluster: ",i,"\t Point :", p 

if __name__ == "__main__": 
    main()
