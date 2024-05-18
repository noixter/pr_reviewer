
# PR Reviewer (Light Version)

## Setup
### Docker
Download and build the image, targeting to the CLI stage on Dockerfile, following this steps
```shell
docker build . -t pr_agent:cli -f docker/Dockerfile --targe cli
```

give another image tag if is necessary, but if not, keep the `pr_agent:cli`
the `Dockerfile` is on the docker folder, **Don't forget to refer the actual Dockerfile


## Considerations Before Running
- the tool needs to simulate an actual PR/MR from a git cloud based tool, so, for that,
it is necessary the current new branch will be selected, and then set the target branch to the branch that will be compared to
  (that branch needs to be fetched as well)
- make sure on the [configuration.toml](pr_agent/settings/configuration.toml) the paramaters `describe_path`, `review_path`, and `suggestion_path` are set up properly
do not change the current path, unless, will it be strictly necessary
- this project is already setup for a lightweight use, however, if its needed, take a deep dive on the [docs](docs) to notice what is this capable of
- the resulting files would be storage on the analyzed project root's, make sure those will be properly generated

## Running
The project needs 3 main params to execute a successful prediction, those are:
- a volume, pointing to the current local project to examine (it need the docker volume syntax to work) and it always need to point to the internal folder `/app/data'
- pr_url, with the target branch in which the project would be predicted
- command, there are 3 main commands to be executed `describe`, `review`, `improve` 
take a look at these [Describe](docs/docs/tools/describe.md), [Review](docs/docs/tools/review.md), [Improve](docs/docs/tools/improve.md)

once those parameters will be fulfilled, run the command following this structure 
```shell
docker run -it -v '/path/to/project:app/data' -t pr_agent:cli --pr_url=<target_branch> <command>
```