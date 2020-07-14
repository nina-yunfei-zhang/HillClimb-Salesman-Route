import pytest
from cities import *

# -----------------------test_compute_total_distance------------------------------
def test_compute_total_distance1():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    """
                                        Note
        ________________________________________________________________________________
        Need to pick up the coordinates in an empty tuple independently because
        the cities.py use data file with delimiter "\t" but in test the example use "," 
        ________________________________________________________________________________
    
    """"
    coords = []
    for i in range(len(road_map1)):
        coords.append((round(float(road_map1[i][2]), 2), round(float(road_map1[i][3]), 2)))

    assert compute_total_distance(cartesian_matx(coords),coords)==\
           pytest.approx(9.38+18.49+10.64, 0.01)

def test_compute_total_distance2():
    road_map1 = [("Alabama","Montgomery",32.361538,-86.279118),("Alaska","Juneau",58.301935,-134.41974),("Arizona","Phoenix",33.448457,-112.073844)]

    coords = []
    for i in range(len(road_map1)):
        coords.append((round(float(road_map1[i][2]), 2), round(float(road_map1[i][3]), 2)))

    assert compute_total_distance(cartesian_matx(coords),coords)==\
           pytest.approx(54.68+33.42+25.81, 0.01)

def test_compute_total_distance3():
    road_map1 = [("Maryland","Annapolis",38.972945,-76.501157),("Massachusetts","Boston",42.2352,-71.0275),("Michigan","Lansing",42.7335,-84.5467)]

    coords = []
    for i in range(len(road_map1)):
        coords.append((round(float(road_map1[i][2]), 2), round(float(road_map1[i][3]), 2)))

    assert compute_total_distance(cartesian_matx(coords),coords)==\
           pytest.approx(6.37+13.53+8.88, 0.01)

def test_compute_total_distance4():
    road_map1 = [("South Carolina","Columbia",34,-81.035),("South Dakota","Pierre",44.367966,-100.336378),("Tennessee","Nashville",36.165,-86.784)]

    coords = []
    for i in range(len(road_map1)):
        coords.append((round(float(road_map1[i][2]), 2), round(float(road_map1[i][3]), 2)))

    assert compute_total_distance(cartesian_matx(coords),coords)==\
           pytest.approx(21.92+15.85+6.14, 0.01)

def test_compute_total_distance5():
    road_map1 = [("South Carolina","Columbia",34,-81.035),("South Dakota","Pierre",44.367966,-100.336378),("Tennessee","Nashville",36.165,-86.784),("South Carolina","Columbia",34,-81.035),("South Dakota","Pierre",44.367966,-100.336378),("Maryland","Annapolis",38.972945,-76.501157)]

    coords = []
    for i in range(len(road_map1)):
        coords.append((round(float(road_map1[i][2]), 2), round(float(road_map1[i][3]), 2)))

    assert compute_total_distance(cartesian_matx(coords),coords)==\
           pytest.approx(21.92+15.85+6.14+21.92+24.44+6.72, 0.01)

# -----------------------test_all_pairs------------------------------

def test_all_pairs1():

    expected = [(0, 0), (0, 1), (1, 0), (1, 1)]
    pairs = list(all_pairs(2))
    assert len(expected) == len(pairs)
    for pair in expected:
        assert (pair in pairs)


def test_all_pairs2():

    expected = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    pairs = list(all_pairs(3))
    assert len(expected) == len(pairs)
    for pair in expected:
        assert (pair in pairs)


def test_all_pairs3():

    expected = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0),
                (3, 1), (3, 2), (3, 3)]
    pairs = list(all_pairs(4))
    assert len(expected) == len(pairs)
    for pair in expected:
        assert (pair in pairs)


def test_all_pairs4():

    expected = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2),
                (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    pairs = list(all_pairs(5))
    assert len(expected) == len(pairs)
    for pair in expected:
        assert (pair in pairs)


def test_all_pairs5():

    expected = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 0),
                (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 0), (4, 1),
                (4, 2), (4, 3), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
    pairs = list(all_pairs(6))
    assert len(expected) == len(pairs)
    for pair in expected:
        assert (pair in pairs)


# -----------------------test_reversed_sections------------------------------
def test_reversed_sections1():
    expected = [[2, 1]]
    rev = list(reversed_sections([1, 2]))
    assert (len(expected) == len(rev))
    for tour in expected:
        assert (tour in rev)


def test_reversed_sections2():
    expected = [[2, 1, 3], [3, 1, 2], [3, 2, 1], [1, 3, 2], [2, 3, 1]]
    rev = list(reversed_sections([1, 2, 3]))
    assert (len(expected) == len(rev))
    for tour in expected:
        assert (tour in rev)


def test_reversed_sections3():
    expected = [[4, 2, 3, 1], [1, 2, 4, 3], [4, 1, 2, 3], [1, 3, 2, 4], [1, 4, 3, 2], [4, 3, 1, 2], [2, 1, 3, 4],
                [3, 2, 1, 4], [4, 3, 2, 1], [2, 3, 4, 1], [3, 4, 2, 1]]
    rev = list(reversed_sections([1, 2, 3, 4]))
    assert (len(expected) == len(rev))
    for tour in expected:
        assert (tour in rev)


def test_reversed_sections4():
    expected = [[1, 2, 5, 4, 3], [5, 4, 2, 3, 1], [1, 2, 4, 3, 5], [5, 4, 1, 2, 3], [1, 5, 4, 3, 2], [1, 3, 2, 4, 5],
                [1, 4, 3, 2, 5], [5, 4, 3, 1, 2], [3, 4, 5, 2, 1], [2, 3, 4, 5, 1], [4, 5, 3, 2, 1], [5, 4, 3, 2, 1],
                [3, 2, 1, 4, 5], [2, 1, 3, 4, 5], [4, 3, 2, 1, 5], [1, 2, 3, 5, 4], [5, 3, 4, 2, 1], [5, 2, 3, 4, 1],
                [5, 1, 2, 3, 4]]
    rev = list(reversed_sections([1, 2, 3, 4, 5]))
    assert (len(expected) == len(rev))
    for tour in expected:
        assert (tour in rev)


def test_reversed_sections5():
    expected = [[6, 1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 5], [6, 3, 4, 5, 2, 1], [6, 2, 3, 4, 5, 1], [6, 4, 5, 3, 2, 1],
                [6, 5, 4, 1, 2, 3], [1, 2, 6, 5, 4, 3], [6, 5, 4, 2, 3, 1], [1, 2, 4, 3, 5, 6], [1, 2, 5, 4, 3, 6],
                [6, 5, 4, 3, 1, 2], [1, 6, 5, 4, 3, 2], [1, 3, 2, 4, 5, 6], [1, 4, 3, 2, 5, 6], [1, 5, 4, 3, 2, 6],
                [6, 5, 4, 3, 2, 1], [3, 2, 1, 4, 5, 6], [2, 1, 3, 4, 5, 6], [4, 3, 2, 1, 5, 6], [5, 4, 3, 2, 1, 6],
                [3, 4, 5, 6, 2, 1], [2, 3, 4, 5, 6, 1], [4, 5, 6, 3, 2, 1], [5, 6, 4, 3, 2, 1], [6, 5, 1, 2, 3, 4],
                [1, 2, 3, 6, 5, 4], [6, 5, 3, 4, 2, 1], [6, 5, 2, 3, 4, 1], [1, 2, 3, 5, 4, 6]]
    rev = list(reversed_sections([1, 2, 3, 4, 5, 6]))
    assert (len(expected) == len(rev))
    for tour in expected:
        assert (tour in rev)


# -----------------------test_swap_cities------------------------------
def test_swap_cities1():
    expected = [[2, 1]]
    swapped = list(swap_cities([1, 2]))
    assert len(expected) == len(swapped)
    for tour in expected:
        assert (tour in swapped)

def test_swap_cities2():
    expected = [[2, 1, 3], [3, 2, 1], [1, 3, 2]]
    swapped = list(swap_cities([1, 2, 3]))
    assert len(expected) == len(swapped)
    for tour in expected:
        assert (tour in swapped)

def test_swap_cities3():
    expected = [[2, 1, 3, 4],[4, 2, 3, 1],[3, 2, 1, 4],[1, 2, 4, 3],[1, 4, 3, 2],[1, 3, 2, 4]]
    swapped = list(swap_cities([1, 2, 3, 4]))
    assert len(expected) == len(swapped)
    for tour in expected:
        assert (tour in swapped)

def test_swap_cities4():
    expected = [[3, 2, 1, 4, 5],[4, 2, 3, 1, 5],[2, 1, 3, 4, 5],[5, 2, 3, 4, 1],[1, 2, 3, 5, 4],[1, 3, 2, 4, 5],[1, 4, 3, 2, 5],[1, 5, 3, 4, 2],[1, 2, 4, 3, 5],[1, 2, 5, 4, 3]]
    swapped = list(swap_cities([1, 2, 3, 4, 5]))
    assert len(expected) == len(swapped)
    for tour in expected:
        assert (tour in swapped)

def test_swap_cities5():
    expected = [[1, 2, 3, 6, 5, 4],[1, 2, 3, 5, 4, 6],[1, 2, 4, 3, 5, 6],[1, 2, 6, 4, 5, 3],[1, 2, 5, 4, 3, 6],[1, 2, 3, 4, 6, 5],[4, 2, 3, 1, 5, 6],[3, 2, 1, 4, 5, 6],[2, 1, 3, 4, 5, 6],[6, 2, 3, 4, 5, 1],[5, 2, 3, 4, 1, 6],[1, 4, 3, 2, 5, 6],[1, 3, 2, 4, 5, 6],[1, 6, 3, 4, 5, 2],[1, 5, 3, 4, 2, 6]]
    swapped = list(swap_cities([1, 2, 3, 4, 5, 6]))
    assert len(expected) == len(swapped)
    for tour in expected:
        assert (tour in swapped)

# -----------------------test_shift_cities------------------------------
def test_shift_cities1():
    expected = [[2,1]]
    shifted = list(shift_cities([1, 2]))
    assert len(expected) == len(shifted)
    for tour in expected:
        assert (tour in shifted)

def test_shift_cities2():
    expected = [[3, 1, 2],[2, 1, 3],[1, 3, 2]]
    shifted = list(shift_cities([1, 2, 3]))
    assert len(expected) == len(shifted)
    for tour in expected:
        assert (tour in shifted)

def test_shift_cities3():
    expected = [[1, 4, 2, 3],[1, 3, 2, 4],[4, 1, 2, 3],[3, 1, 2, 4],[2, 1, 3, 4],[1, 2, 4, 3]]
    shifted = list(shift_cities([1, 2, 3, 4]))
    assert len(expected) == len(shifted)
    for tour in expected:
        assert (tour in shifted)

def test_shift_cities4():
    expected = [[1, 2, 3, 5, 4],[1, 5, 2, 3, 4],[1, 4, 2, 3, 5],[1, 3, 2, 4, 5],[1, 2, 5, 3, 4],[1, 2, 4, 3, 5],[5, 1, 2, 3, 4],[4, 1, 2, 3, 5],[2, 1, 3, 4, 5],[3, 1, 2, 4, 5]]
    shifted = list(shift_cities([1, 2, 3, 4, 5]))
    assert len(expected) == len(shifted)
    for tour in expected:
        assert (tour in shifted)

def test_shift_cities5():
    expected = [[1, 2, 3, 4, 6, 5],[1, 6, 2, 3, 4, 5],[1, 4, 2, 3, 5, 6],[1, 3, 2, 4, 5, 6],[1, 5, 2, 3, 4, 6],[2, 1, 3, 4, 5, 6],[6, 1, 2, 3, 4, 5],[4, 1, 2, 3, 5, 6],[3, 1, 2, 4, 5, 6],[5, 1, 2, 3, 4, 6],[1, 2, 6, 3, 4, 5],[1, 2, 4, 3, 5, 6],[1, 2, 5, 3, 4, 6],[1, 2, 3, 6, 4, 5],[1, 2, 3, 5, 4, 6]]
    shifted = list(shift_cities([1, 2, 3, 4, 5, 6]))
    assert len(expected) == len(shifted)
    for tour in expected:
        assert (tour in shifted)