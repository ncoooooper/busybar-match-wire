# Match Wire

Keep a match score on the front display. Turn the wheel for the provider’s clock, quarter or half, then the player and team for each available football card. The last reported score stays visible when the feed drops.

## Setup

Get an API key in the API-SPORTS dashboard and enable the Football or Basketball product on your plan. Copy the example config. Set `sport` to `football` or `basketball`. Find the game in the dashboard’s Fixtures or Games explorer, then put its numeric ID in `event`. The example uses `0` as a placeholder. Set `SPORTS_KEY` in the companion’s environment. The bar checks its companion every 15 seconds. The companion asks the provider at most once a minute by default. Set `poll_seconds` to 90 or 120 on a small daily quota. Check the quota on your plan before following a full match.

From the repository root, copy the example and start the companion with Python 3.10 or newer.

```sh
cp companion/example.json config.json
# Edit config.json for your source before starting the server.
python3 companion/serve.py --config config.json
```

In the emulator, run `~/.busy-emulator/bin/busy-emulator allow-local 8770` and approve that port. Open **Apps → Match Wire → Setup**, set **Local companion URL** to `http://127.0.0.1:8770/reading`, save, then reopen the app. For a physical bar, start the companion with `--host YOUR_LAN_IP` and replace `127.0.0.1` with that address. Bind only to your trusted network. Open `/reading` on the host to inspect the current reading. Keep credentials in the host environment.

## Follow a football match

Read the two teams and score first. Turn once for the match clock. The recorded Ukraine–Poland fixture is an example at 3:2 and 78:54. The football feed usually supplies elapsed whole minutes and stoppage time. The display uses the precision the source sends.

![The example switches from Ukraine–Poland at 3:2 to 78:54.](media/guide/use-1.gif)

## Look up a booking or a quarter

Turn again for the latest football card. Read the player, team and minute on the back. To follow basketball, change the sport and event ID, then restart the companion. Look for the current quarter and the provider’s clock. Scheduled games show an empty score. Where a clock is unavailable the display shows two dashes.

![The sample fixture changes from the match clock to a yellow card.](media/guide/use-2.gif)

## Run in the emulator

Install BUSY Bar Emulator and open it. From this repository run the following command, then press **Back** when you finish.

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

The recordings use example responses on emulator firmware. Each display pixel is enlarged to a 9 × 9 square.

[Football fixtures](https://www.api-football.com/documentation-v3) · [Basketball games](https://api-sports.io/documentation/basketball/v1).

[Rear display](screenshots/back-1.png) · [MIT license](LICENSE)
