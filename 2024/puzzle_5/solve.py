def read_rules(lines:list[str]):
    rules = {}
    for line in lines:
        pre, post = line.split("|")
        posts = rules.get(pre,[])
        posts.append(post.strip())
        rules[pre]=posts
    return rules

def solve(lines: list[str], rules:dict[int,list[int]]):
    total = 0
    for line in lines:
        outcome = check_line(line,rules)
        if outcome:
            total += int(outcome)
    return total
        
def check_line(line,rules):
        pages = [x.strip() for x in line.split(",")]
        for index,number in enumerate(pages):
            posts = rules.get(number,[])
            for i in range(index):
                if pages[i] in posts:
                    return None
        return pages[int(len(pages)/2-0.5)]

if __name__ == "__main__":
    with open("input.txt", "r") as handle:
        lines = handle.readlines()

    with open("order.txt","r") as rule_handle:
        rule_lines = rule_handle.readlines()
        rules = read_rules(rule_lines)
        print(rules)
    print(solve(lines, rules))
