## JIRA Ticket
_Add ticket id_

## Description
_Add a few sentences describing the overall goals of the pull request's commits._

## TODO
- [ ] pycodestyle (`make lint`)
- [ ] tests (`make test`)

## Steps to Test or Reproduce
_Add detailed steps for testing/review team to verify._

## Setup Environment with PR

1. Cleanup previous state

```bash
make purge
```

2. Checkout PR

__Using git command (command line interface)__
```bash
pr_id=ADD_PR_NUMBER_HERE
git checkout master
git branch -D $pr_id
git fetch
git fetch origin pull/$pr_id/head:$pr_id
git checkout $pr_id
git submodule init
git submodule update --remote --recursive
```

__Using [Gitkraken](https://www.gitkraken.com/)__

+ In GitKraken, right click on the pull request you want to review. Select Add Remote and Checkout (the PR).

3. Start exchange

```bash
make start
```

4. Exchange Healthcheck

```bash
docker inspect --format '{{ .State.Health.Status }}' exchange
```

__NOTE:__ Only continue the following steps if the output from the above command is `healthy`. You may have to wait 
a few minutes.

---
@boundlessgeo/bex-qa