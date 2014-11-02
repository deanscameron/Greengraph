"""Grengraph test file"""

# Some tests for Greengraph

from nose.tools import assert_almost_equal, assert_equal, assert_false
from ..geolocation import geolocate
from ..create_png import is_green


# Test that geolocation gives returns the correct coordinates
# Compare the values returned to ones looked up
def test_geolocation():
    coordinates_birmingham = geolocate("Birmingham")
    assert_almost_equal(coordinates_birmingham[0], 52.4774376, places = 1)
    assert_almost_equal(coordinates_birmingham[1], -1.8636315, places = 1)

	
# Test the is_green function
# Give the function values of (r,g,b) that should pass and fail
def test_is_green():
    assert(is_green(1,2,1))
    assert_false(is_green(2,1,1))