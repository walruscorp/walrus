[![Build Package and Test it](https://github.com/vineetbansal/walrus/actions/workflows/build.yml/badge.svg)](https://github.com/vineetbansal/walrus/actions/workflows/build.yml)

## Walrus

This package is to try out CI/testing/python coding/tooling in an isolated project, and hopefully have one place for field notes.

See also [https://github.com/walruscorp/walrus_es](https://github.com/walruscorp/walrus_es) for an avaiable plugin for this project.


### Pre-commit

`ruff format` actually fixes the format but **still returns non-zero** if it ended up fixing anything, so it can be used locally to reformat on commit, and on CI as a check (using `pre-commit run --all-files`).
Note that `ruff check --fix` comes *before* `ruff format`. Claude (as opposed to ChatGPT) seems to agree:

> ruff check --fix can make code changes when auto-fixing linting issues (e.g., removing unused imports, sorting imports, fixing style violations). These auto-fixes might not be
  perfectly formatted.
>
> ruff format should run last to ensure all code—including any changes made by the linter's auto-fix—is properly formatted.
>
> If you format first and then run check with --fix, the linter's fixes may introduce formatting inconsistencies that won't be corrected (since the formatter already ran).

### Versioning

```
pipx run bumpversion minor
```

Look at `.bumpversion.cfg`:
```
commit = True
tag = True
```

it commits and adds a tag, so be careful. If it does do so, it insists on a clean `git status` so that the version bump stays its own commit without other changes. Seems reasonable.

`setuptools-scm` is nice but it packages everything it finds in the `git` repo for inclusion in the sdist, forcing one to do acrobatics with `MANIFEST.in` etc..


#### Notes on uv

`uv` is not being used in this project. These notes are just general observations that sit here before there's a chance ot move them at a more appropriate place.

- `uv init` generates, among other files:
  - `pyproject.toml`
  - `.python_version` (git tracked) - This also goes as `requires-python` in `pyproject.toml`.
- `uvx cowsay -t moo` runs, but doesn't modify anything in the project.
- `uv run cowsay -t moo` fails (but creates a `uv.lock` since it was the first invocation of `uv run`).
- `uv run` is really just `.venv/bin/python ..` or `.venv/bin/python -m ..`
- `uv pip install cowsay` installs `cowsay` and we can now run `uv run cowsay -t moo`, but the requirement didn't go anywhere (`uv.lock` is unmodified, and no new files are created).
- `uv add cowsay` adds to `uv.lock`, as well as `pyproject.toml [dependencies]` (with a specific `"cowsay>=6.1"`, indicating what was used during `uv add`). We could have said "uv add cowsay>5" to be a bit more specific.
- `uv add --dev pytest` adds a "dependency group", not an "extra".

The general philosophy behind `uv.lock` seems to be that a developer specifying version X does not logically imply freezing all transitive dependencies forever. The graph should be resolved not later, but at declaration time.
