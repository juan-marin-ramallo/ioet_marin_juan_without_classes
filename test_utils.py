import utils

def test_get_next_day_worked():
  assert utils.get_next_day_worked("SU") == "MO", "Should be MO Monday"
  assert utils.get_next_day_worked("MO") == "TU", "Should be TU Tuesday"
  assert utils.get_next_day_worked("XX") == "", "Should be empty because there is no exists XX day"


if __name__ == "__main__":
    test_get_next_day_worked()
    print("Everything passed")