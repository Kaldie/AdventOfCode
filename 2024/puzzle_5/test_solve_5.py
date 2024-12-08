from pytest import fixture
from solve import read_rules, solve


@fixture
def test_input():
    return """
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".split()

@fixture
def test_rules():
    return read_rules("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13""".split())

def test_solve(test_input,test_rules):
    assert solve(test_input, test_rules) == 143