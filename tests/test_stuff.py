import pandas as pd
from pandas._testing import assert_frame_equal
from pathlib import Path
from src.main import load_data  # import the function from your main.py file

def test_load_data():
    # Create a temporary CSV file for testing
    test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    test_data.to_csv('test.csv', index=False)

    # Call the function and get the result
    result = load_data(Path('test.csv'))

    # Check that the result is as expected
    expected = pd.read_csv('test.csv')
    assert_frame_equal(result, expected)

    # Clean up the temporary file
    Path('test.csv').unlink()