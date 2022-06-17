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
    g = Github().get_user('benchopt')
    content = """# Benchmarks gallery

    To reproduce / modify a benchmark,
    
    1. clone the benchmark repository and ``cd`` into it,

    ```shell
    $ git clone https://github.com/benchopt/{REPOSITORY_NAME}.git
    $ cd {REPOSITORY_NAME}
    ```

    2. install ``benchopt`` to use its API/CLI,

    ```shell
    $ pip install -U benchopt
    ```
    
    3. run the following command to reproduce the benchmark,

    ```shell
    $ benchopt run .
    ```

    Et Voilà! 
    
    Refer to [``Benchopt`` API](https://benchopt.github.io/cli.html#benchopt-run)
    to explore the different options for running a benchmark.


    ### Available benchmarks\n\n
    """

    for repo in g.get_repos():
        if repo.name.startswith('benchmark'):
            content += make_item(repo)

    with open('profile/gallery-benchmarks.md', 'w+') as f:
        f.write(content)
