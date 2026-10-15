# Branch strategy

Use this reference during G04 planning when work is parallel, spans multiple releases, crosses ownership boundaries, or the repository has no clear branch convention. Choose the least complex strategy that fits the team and release model; repository policy and observed protections take precedence.

## Choose a shape

| Situation | Starting strategy | Add complexity only when |
|---|---|---|
| Small team or continuous delivery | One protected mainline with short-lived task branches and reviewable PRs | Release support or isolation requirements demand another line |
| Many independent parallel tasks | Short-lived branches per task and isolated worktrees where available | Shared files or dependencies require coordination |
| One large change with ordered, reviewable slices | A short stack of dependent PRs with explicit base/head links | The stack is too costly to rebase or review; then split by stable interfaces |
| Multiple versions supported at once | Mainline plus named release branches | The project commits to maintaining each older version |
| Monorepo with separate ownership | The same branch model plus confirmed CODEOWNERS and component-scoped checks | Build/test cost requires path-aware CI or queue policy |

Do not create long-lived team or feature branches by default. Do not assume GitFlow, a naming convention, merge method, branch protection, CODEOWNERS, or merge queue is configured; inspect project policy and live controls where available.

## Record a branch plan

For each work item or coordinated batch, record:

- base branch and the observed source of that choice;
- branch name pattern and one accountable writer/owner;
- expected lifetime and merge method, following repository policy;
- dependencies and stack order, if any;
- ownership boundaries and required checks/reviewers;
- conflict/rebase and recovery approach;
- when a branch can be deleted after integration.

Scale parallel work by splitting independent outcomes, assigning one writer per file/scope at a time, and keeping shared interfaces explicit. A larger number of agents does not justify shared mutable branches. If branch policy, target branch, or write authority is unknown, propose the plan and stop before creating or changing branches.
