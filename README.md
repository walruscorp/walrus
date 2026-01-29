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
