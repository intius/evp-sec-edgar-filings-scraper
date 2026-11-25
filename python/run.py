import json
import os
from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
if not APIFY_TOKEN:
    raise SystemExit("Set APIFY_TOKEN before running this example.")

client = ApifyClient(APIFY_TOKEN)
run_input = json.loads('''{"ticker":"AAPL","forms":"10-K,10-Q,8-K","startDate":"2025-01-01","maxItems":10}''')
run = client.actor("evpp/sec-edgar-filings").call(run_input=run_input)
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(json.dumps(items[:5], indent=2, ensure_ascii=False))
print(f"Fetched {len(items)} items. Open the full dataset: https://console.apify.com/storage/datasets/{run['defaultDatasetId']}")
