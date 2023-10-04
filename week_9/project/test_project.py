from project import coordinate_calc, coordinate_gms, check_number

def test_coordinate_calc():
    try:
        coordinate_calc(-48.3425, "latitude")
        assert True
    except ValueError:
        raise ValueError("Invalid Values")


def test_coordinate_calc_2():
    try:
        coordinate_calc("-50.4578", "longitude")
        assert True
    except ValueError:
        raise ValueError("Invalid Values")



def test_coordinate_gms():
    try:
        coordinate_gms(-48.6224, 48, 37, 20.64, "longitude")
        assert True
    except ValueError:
        raise ValueError("Invalid Values")


def test_check_number():
    try:
        check_number(15)
        assert True
    except ValueError:
        raise ValueError("Invalid Values")
