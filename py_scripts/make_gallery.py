import sys
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
    ACCESS_TOKEN = sys.argv[0]

    g = Github(ACCESS_TOKEN).get_user('benchopt')
    content = "# Gallery of Benchmarks\n\n"

    for repo in g.get_repos():
        if repo.name.startswith('benchmark'):
            content += make_item(repo)

    with open('profile/gallery-benchmarks.md', 'w+') as f:
        f.write(content)
