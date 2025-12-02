'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in)

'''
import heapq
def KClosest(points,k):
    def dist(x,y):
        return x*x + y*y
    
    heap = []
    for x,y in points:
        if len(heap) < k:
            heapq.heappush(heap, (-dist(x,y),x,y))
        else:
            heapq.heappushpop(heap, (-dist(x,y),x,y))
    return [list(h[1:]) for h in heap]

