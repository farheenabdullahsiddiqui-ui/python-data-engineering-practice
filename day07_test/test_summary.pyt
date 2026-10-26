from day05_grouping import group_salaries

def test_empty_list_gives_empty_list():
    assert(group_salaries.summarise_by_department([]))=={}


def test_two_departments():
    rows = [
        {"Name": "Alice", "Department": "Engineering", "Salary": "85000"},
        {"Name": "Bob", "Department": "Engineering", "Salary": "65000"},
        {"Name": "Carla", "Department": "Sales", "Salary": "61000"},
    ]
    result = group_salaries.summarise_by_department(rows)
    assert result["Engineering"]["count"] == 2
    assert result["Engineering"]["total_salary"] == 150000
    assert result["Sales"]["count"]==1