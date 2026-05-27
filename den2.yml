name: BITAMD Advanced

on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run update script
        run: python update.py

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config.user.email "github-actions[bot]@users.noreply.github.com"
          git add rate.json history.json
          git commit -m "auto update" || echo "no changes"
          git push
