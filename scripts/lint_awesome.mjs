import process from 'node:process';
import awesomeLint from 'awesome-lint/index.js';
import defaultConfig from 'awesome-lint/config.js';

const isPullRequest = process.env.GITHUB_EVENT_NAME === 'pull_request';

// GitHub reports metadata for the repository's default branch, not the PR tree.
// Keep that rule visible without blocking the PR that adds its first license.
const config = defaultConfig.map(entry => {
  const rule = Array.isArray(entry) ? entry[0] : entry;
  return isPullRequest && rule.name === 'remark-lint:awesome-github'
    ? [rule, ['warn']]
    : entry;
});

if (isPullRequest) {
  console.log('GitHub repository metadata is advisory on PRs; file checks remain required.');
}

await awesomeLint.report({filename: 'README.md', config});
