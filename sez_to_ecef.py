# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
# TConverts SEZ vector components to ECEF
# Parameters:
# o_lat_deg: latitude in degrees
# o_lon_deg: longitude in degrees
# o_hae_km: height above the ellipsoid in km
# s_km: SEZ s-component in km
# e_km: SEZ e-component in km
# z_km: SEZ z-component in km
# Output:
# Prints ECEF components (x,y,z) in kilometers
#
# Written by Celia Sterthous
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys # argv
import math
import numpy as np
# "constants"

# helper functions


# initialize script arguments
o_lat_deg = float('nan') # description of argument 1
o_lon_deg = float('nan') # description of argument 2
o_hae_km  = float('nan')
s_km      = float('nan')
e_km      = float('nan')
z_km      = float('nan')
# parse script arguments
if len(sys.argv)==7:
  o_lat_deg = sys.argv[1]
  o_lon_deg = sys.argv[2]
  o_hae_km  = sys.argv[3]
  s_km      = sys.argv[4]
  e_km      = sys.argv[5]
  z_km      = sys.argv[6]
else:
   print(\
      'Usage: '\
      'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
     )
   exit()

# write script below this line
lon_rad = o_lon_deg*math.pi/180
lat_rad = o_lat_deg*math.pi/180

R_y = np.array([[math.sin(lat_rad), 0, math.cos(lat_rad)], [0,1,0], [-math.cos(lat_rad), 0, math.sin(lat_rad)]])
sez_v = np.array([[s_km],[e_km],[z_km]])
one_rot = R_y.dot(sez_v)
R_z = np.array([[math.cos(lon_rad),-math.sin(lon_rad),0],[math.sin(lon_rad), math.cos(lon_rad),0],[0,0,1]])
two_rot = R_z.dot(one_rot)
ecef_x_km = two_rot[0]
ecef_y_km = two_rot[1]
ecef_z_km = two_rot[2]

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)