import pytest

from numbers_parser import Document
from numbers_parser.cell import EmptyCell, TextCell, NumberCell


def test_empty_document():
    doc = Document()
    data = doc.sheets[0].tables[0].rows()
    assert len(data) == 22
    assert len(data[0]) == 7
    assert type(data[0][0]) == EmptyCell


def test_save_document(tmp_path):
    doc = Document("tests/data/test-1.numbers")
    sheets = doc.sheets
    tables = sheets[0].tables
    cell_values = tables["ZZZ_Table_1"].rows(values_only=True)

    sheets["ZZZ_Sheet_1"].name = "ZZZ_Sheet_1 NEW"
    tables["ZZZ_Table_1"].name = "ZZZ_Table_1 NEW"

    new_filename = tmp_path / "test-1-new.numbers"
    doc.save(new_filename)

    new_doc = Document(new_filename)
    new_sheets = new_doc.sheets
    new_tables = new_sheets["ZZZ_Sheet_1 NEW"].tables
    new_cell_values = new_tables["ZZZ_Table_1 NEW"].rows(values_only=True)

    assert cell_values == new_cell_values


def test_save_merges(tmp_path, pytestconfig):
    doc = Document("tests/data/test-save-1.numbers")
    sheets = doc.sheets
    table = sheets[0].tables[0]
    table.add_column(2)
    table.add_row(3)
    table.write("B2", "merge_1")
    table.write("B5", "merge_2")
    table.write("D2", "merge_3")
    table.merge_cells("B2:C2")
    table.merge_cells(["B5:E5", "D2:D4"])

    if pytestconfig.getoption("save_file") is not None:
        new_filename = pytestconfig.getoption("save_file")
    else:
        new_filename = tmp_path / "test-1-new.numbers"
    doc.save(new_filename)

    doc = Document(new_filename)
    sheets = doc.sheets
    table = sheets[0].tables[0]
    assert table.merge_ranges == ["B2:C2", "B5:E5", "D2:D4"]


def test_create_table(tmp_path, pytestconfig):
    doc = Document()
    sheets = doc.sheets

    with pytest.raises(IndexError) as e:
        _ = sheets[0].add_table("TablE 1")
    assert "table 'TablE 1' already exists" in str(e.value)

    table = sheets[0].add_table()
    assert table.name == "Table 2"
    table.write("B1", "Column B")
    table.write("C1", "Column C")
    table.write("D1", "Column D")
    table.write("B2", "Mary had")
    table.write("C2", "a little")
    table.write("D2", "lamb")

    if pytestconfig.getoption("save_file") is not None:
        new_filename = pytestconfig.getoption("save_file")
    else:
        new_filename = tmp_path / "test-1-new.numbers"
    doc.save(new_filename)

    doc = Document(new_filename)
    sheets = doc.sheets

    table = sheets[0].tables[1]
    assert sheets[0].tables[1].name == "Table 2"
    assert table.cell("B1").value == "Column B"
    assert table.cell("C1").value == "Column C"
    assert table.cell("D1").value == "Column D"
    assert table.cell("B2").value == "Mary had"
    assert table.cell("C2").value == "a little"
    assert table.cell("D2").value == "lamb"


def test_create_sheet(tmp_path, pytestconfig):
    doc = Document()
    sheets = doc.sheets

    with pytest.raises(IndexError) as e:
        _ = doc.add_sheet("SheeT 1")
    assert "sheet 'SheeT 1' already exists" in str(e.value)

    doc.add_sheet("New Sheet", "New Table")
    sheet = doc.sheets["New Sheet"]
    table = sheet.tables["New Table"]
    table.write(0, 1, "Column 1")
    table.write(0, 2, "Column 2")
    table.write(0, 3, "Column 3")
    table.write(1, 1, 1000)
    table.write(1, 2, 2000)
    table.write(1, 3, 3000)

    if pytestconfig.getoption("save_file") is not None:
        new_filename = pytestconfig.getoption("save_file")
    else:
        new_filename = tmp_path / "test-1-new.numbers"
    doc.save(new_filename)

    doc = Document(new_filename)
    sheets = doc.sheets

    assert sheets[1].name == "New Sheet"

    table = sheets[1].tables[0]
    assert table.name == "New Table"

    assert type(table.cell(0, 1)) == TextCell
    assert table.cell(0, 1).value == "Column 1"
    assert type(table.cell(0, 1)) == TextCell
    assert type(table.cell(1, 3)) == NumberCell
    assert table.cell(1, 3).value == 3000


def test_create_multi(tmp_path, pytestconfig):
    doc = Document()

    doc.sheets[0].tables[0].write(0, 0, "S0T1 A1")

    doc.add_sheet()
    doc.sheets[1].add_table()
    doc.sheets[1].add_table()
    doc.sheets[1].tables[0].write(0, 0, "S1T0 A1")
    doc.sheets[1].tables[1].write(0, 0, "S1T1 A1")
    doc.sheets[1].tables[2].write(0, 0, "S1T2 A1")

    doc.add_sheet()
    doc.sheets[2].add_table(x=100.0)
    doc.sheets[2].add_table(x=0.0, y=700.0)
    doc.sheets[2].add_table()
    doc.sheets[2].tables[0].write(0, 0, "S2T0 A1")
    doc.sheets[2].tables[1].write(0, 0, "S2T1 A1")
    doc.sheets[2].tables[2].write(0, 0, "S2T2 A1")
    doc.sheets[2].tables[3].write(0, 0, "S2T3 A1")

    if pytestconfig.getoption("save_file") is not None:
        new_filename = pytestconfig.getoption("save_file")
    else:
        new_filename = tmp_path / "test-1-new.numbers"
    doc.save(new_filename)

    doc = Document(new_filename)
    assert doc.sheets[1].tables[1].height == 200
    assert doc.sheets[2].tables[1].coordinates == (100.0, 280.0)
    assert doc.sheets[2].tables[2].coordinates == (0.0, 700.0)
    assert doc.sheets[2].tables[3].coordinates == (0.0, 980.0)
    assert len(doc.sheets) == 3
    assert len(doc.sheets[2].tables) == 4
