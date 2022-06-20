from github import Github


def make_item(repo):
    description = _process_description(repo.description)
    return (f"- [{description}]({repo.url}) "
            f"![Test status](https://github.com/benchopt/{repo.name}/actions/workflows/main.yml/badge.svg)\n")


def _process_description(description):
    if description is None:
        return 'No description.'

    description = description
    description = description.lower()

    for stop_word in ('benchmark', 'for', 'repository', 'benchopt'):
        description = description.replace(stop_word, '')

    description = description.strip()
    description = description.capitalize()

    return description


if __name__ == "__main__":
    g = Github().get_user('benchopt')

    content = ""
    with open('py_scripts/starter-content.txt', 'r') as f:
        content = f.read()

    for repo in g.get_repos():
        if repo.name.startswith('benchmark'):
            content += make_item(repo)

    with open('profile/gallery-benchmarks.md', 'w+') as f:
        f.write(content)
