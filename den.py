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

      - name: Update rate and history
        run: |
          python -c "
import json, random, time

with open('rate.json', 'r') as f:
    data = json.load(f)

old_rate = data['rate']
old_history = data.get('history', [])

trend = random.randint(-10, 10)
new_rate = round(old_rate + old_rate * trend / 100, 2)
if new_rate < 0.30:
    new_rate = 0.30

data['rate'] = new_rate
data['last_updated'] = int(time.time())

old_history.append(new_rate)
data['history'] = old_history[-30:]

with open('rate.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f'✅ Курс обновлён: {old_rate} -> {new_rate}')
"

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config.user.email "github-actions[bot]@users.noreply.github.com"
          git add rate.json
          git commit -m "auto update" || echo "no changes"
          git push
