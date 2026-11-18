"""Read a fixture and its events from API-SPORTS Football or Basketball."""
import os,json
from urllib.request import Request,urlopen
from serve import page
INTERVAL=15
def snapshot(o,m):
    def get(url):
        with urlopen(Request(url,headers={"x-apisports-key":os.environ["SPORTS_KEY"]}),timeout=9) as r:j=json.load(r)
        if j.get("errors"):raise ValueError("Provider rejected request or plan quota")
        return j["response"]
    sport=o["sport"];fid=int(o["event"])
    football=sport=="football"
    if sport not in ["football","basketball"]:raise ValueError("Choose football or basketball")
    url="https://v3.football.api-sports.io/fixtures?id=" if football else "https://v1.basketball.api-sports.io/games?id="
    rows=get(url+str(fid))
    if not rows:raise ValueError("No fixture returned")
    d=rows[0];st=d["fixture"]["status"] if football else d["status"]
    home,away=[d["teams"][side]["name"] for side in ("home","away")]
    scores=d["goals"] if football else {side:d["scores"][side]["total"] for side in ("home","away")}
    score=":".join(str(scores[x]) if scores[x] is not None else "-" for x in ("home","away"))
    clock=st.get("clock") or (str(st["elapsed"])+("'" if not st.get("extra") else "+"+str(st["extra"])+"'") if football and st.get("elapsed") is not None else st.get("timer") or "--")
    period=st.get("short","");pages=[page(home+" / "+away,score,home,away,period+" "+str(clock)),page("MATCH CLOCK",clock,home+" / "+away,period)]
    for event in reversed(d.get("events",[])):
        if event.get("type")=="Card":pages.append(page(event["detail"],event.get("player",{}).get("name") or "Unknown",event.get("team",{}).get("name",""),str(event["time"]["elapsed"])+"'"))
        if len(pages)>=30:break
    return dict(state=period+" / "+sport,key=score+period+str(len(pages)),pages=pages)
