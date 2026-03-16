# Prototype GitHub Pages Fix

**Assignment:** Group Assignment 1 - Initial Prototype (todo list app)
**Repo:** https://github.com/kevinle1021/prototype
**Expected URL:** https://kevinle1021.github.io/prototype/

## Problem
The URL returns 404. GitHub Pages is not enabled on the repo.

## What's Already Done
- `gh-pages` branch exists with correctly built files
- `base href` is set to `/prototype/`
- Angular app is built and deployed via `angular-cli-ghpages`
- All static files (index.html, JS, CSS) are present on the branch

## Fix Required
Someone with **admin access** to kevinle1021/prototype needs to:
1. Go to **Settings > Pages**
2. Set Source to "Deploy from a branch"
3. Set Branch to `gh-pages` / `/ (root)`
4. Save

Laws has push access but not admin. Kevin (repo owner) needs to do this.

## If Re-deploy Is Needed After Pages Is Enabled
```bash
cd "C:\Users\lawss\Documents\Repos\prototype"
npx ng deploy --base-href=/prototype/
```
