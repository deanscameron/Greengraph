"""Greengraph functions file"""

# Counts the green areas at equidistant points between two locations
# Plots the values as a graph

from geolocation import geolocate, url, map_at
from create_png import count_green_in_png, show_green_in_png

# Define the locations and the points in-between them
from numpy import linspace
def location_sequence(start,end,steps):
  lats=linspace(start[0],end[0],steps)
  longs=linspace(start[1],end[1],steps)
  return zip(lats,longs)
 
def greengraph(start_city, end_city, steps):
  # Count the green areas at each of these points
  [count_green_in_png(map_at(*location,zoom=10,satellite=True))
              for location in location_sequence(
                  geolocate(start_city),
                  geolocate(end_city),
                  steps)]


  # Plot the counts of the green areas of the maps at each point
  import matplotlib
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  with open('green.png','w') as green:
      green.write(show_green_in_png(map_at(*geolocate(start_city),
          zoom=10,satellite=True)))

		
  plt.plot([
      count_green_in_png(
          map_at(*location,zoom=10,satellite=True))
            for location in location_sequence(
                geolocate(start_city),
                geolocate(end_city),steps)])

  # Save the plot as a file 'greengraph.png'
  plt.savefig('greengraph.png')