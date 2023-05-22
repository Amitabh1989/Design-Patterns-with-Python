import pytest
from io import StringIO
import adapter
from adapter import *
import pytest_mock
from pytest_mock import mocker


def test_csv_to_json_converter(mocker):
    csv_file = CSVFile("data.csv")
    csv_to_json_converter = CSVtoJSONConvertor(csv_file)

    mocker.patch.object(csv_file, "read_csv", return_value="Reading CSV data")
    mocker.patch.object(csv_file, "write_json", return_value="Writing CSV data to JSON file")

    output = StringIO()
    mocker.patch("sys.stdout", new=output)

    csv_to_json_converter.convert()

    assert csv_file.read_csv.called
    assert csv_file.write_json.called
    assert output.getvalue() == "Conversion complete!\n"

def test_json_to_csv_converter(mocker):
    json_file = JSONFile("data.json")
    json_file_converter = JSONtoCSVConvertor(json_file)

    mocker.patch.object(json_file, "read_json", return_value="Reading JSON data")
    mocker.patch.object(json_file, "write_csv", return_value="Writing JSON data to CSV file")

    output = StringIO()
    mocker.patch("sys.stdout", new=output)

    assert json_file.read_json.called
    assert json_file.write_csv.called
    assert output.getvalue() == "Conversion complete!\n"