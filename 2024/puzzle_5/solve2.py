def read_rules(lines: list[str]):
    rules = {}
    for line in lines:
        pre, post = line.split("|")
        posts = rules.get(pre, [])
        posts.append(post.strip())
        rules[pre] = posts
    return rules


def solve(lines: list[str], rules: dict[int, list[int]]):
    total = 0
    for line in lines:
        if is_incorrect(line, rules):
            new_lines = fix(line, rules)
            total += int(new_lines[int(len(new_lines) / 2 - 0.5)])
    return total


def is_incorrect(line, rules):
    pages = [x.strip() for x in line.split(",")]
    for index, number in enumerate(pages):
        posts = rules.get(number, [])
        for i in range(index):
            if pages[i] in posts:
                return index, i
    return False


def fix(line, rules):
    before_index, offender_index = is_incorrect(line, rules)
    pages = [x.strip() for x in line.split(",")]
    offender = pages.pop(offender_index)
    ",".join(pages.insert(offender,before_index))


if __name__ == "__main__":
    with open("input.txt", "r") as handle:
        lines = handle.readlines()

    with open("order.txt", "r") as rule_handle:
        rule_lines = rule_handle.readlines()
        rules = read_rules(rule_lines)
        print(rules)
    print(solve(lines, rules))
