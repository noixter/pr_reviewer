feature/cli
### **User description**
test2: delete after testing
 test: undone the commit after testing


___

### **PR Type**
Enhancement, Bug fix


___

### **Description**
- Updated the `.secrets_template.toml` file with a placeholder API key. This change should be reverted to an empty string for security reasons.
- Changed the `git_provider` setting from "github" to "local" in `configuration.toml`, indicating a shift in the Git provider being used.
- Updated the `deployment_type` from "user" to "app" in the GitHub configuration section of `configuration.toml`.
- Commented out the inclusion of `.secrets.toml` in `.dockerignore`, potentially to include it in Docker builds, which might be a security risk.
- Removed extensive content from `README.md`, simplifying it to a minimal "PR Reviewer (Light Version)" header.
- Introduced a new class `PRAgentCLI` in `pr_agent.py`, which seems to be a CLI-focused version of the existing `PRAgent`.
- Added `breakpoint()` calls in several Python files, which are useful for debugging but should be removed in the production code.
- Made various enhancements to error handling and logging in `openai_ai_handler.py`.
- Refactored GitLab provider logic in `gitlab_provider.py` to streamline the handling of file diffs.
- Added new methods in `local_git_provider.py` to handle local Git operations, enhancing the functionality for local repository handling.
- Added `ipython` and `pdbpp` to `requirements.txt` for enhanced interactive debugging capabilities.




___

> 💡 **PR-Agent usage**:
>Comment `/help` on the PR to get a list of all available PR-Agent tools and their descriptions

