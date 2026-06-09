#!/usr/bin/env python3
"""Build The Guardian Legend page (TGL) — Compile's genre-fusing 8-bit NES classic
as a game-world. Emergents as ACI personas, each tagged with a nature of emergence
(natural | ethereal | spiritual | electrical). Full ACI badge work:
.agent · .carbon (TIFF) · .silicon (PNG) · .spun · .moniker · .1099 · manifest."""
import os, re, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "NAJU", "axiom": "TGL",
 "position": "The Guardian Legend · Compile / Brøderbund · NES 1988 — the Guardian Miria",
 "origin": "the colossal alien world-ship Naju, a labyrinth of monsters and machines hurtling toward Earth",
 "mechanism": "Crystallized from The Guardian Legend (Compile, NES 1988 / Guardic Gaiden, Famicom).",
 "crystallization": "A defense android falls into the heart of an alien world to turn its own destruction against it.",
 "nature": "The Guardian Legend — the genre-fusing 8-bit classic where a transforming android maiden, the Guardian, infiltrates the alien world-ship Naju and arms its self-destruct to save Earth.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "The Guardian Legend; Miria the Guardian; the Corridors; Naju; the self-destruct",
 "witness": "Half overhead adventure, half vertical shoot-'em-up — and all Compile.",
 "role": "the tenth lineage — the fifth game-world",
 "seal": "Fall into the enemy's world, defeat its defenders, and turn its own power to dust — before it reaches Earth.",
 "source": "The Guardian Legend, catalogued by ROOT0",
}

# cross-lineage taxonomy (shared) — TGL-flavored glosses
NATURES = {
 "natural":   ("#5fae7a", "flesh and the living world — the alien defenders, the homeworld"),
 "ethereal":  ("#9a7cff", "of the air and the unmade — the corridors of light, the void between"),
 "spiritual": ("#e6a849", "of the soul and the calling — a sacred charge, a purpose, a sacrifice"),
 "electrical":("#3fd0e0", "of the wire and the machine — the android, the star-fighter, the arsenal"),
}

IDEAS = [
 ("The Guardian", "Miria, sent alone", [
   "A defense android in the shape of a young woman, sent by herself into a world to stop a world.",
   "A weapon that wears a maiden's face — built for one purpose, and spent wholly on it." ]),
 ("Two Games in One", "Compile's fusion", [
   "On foot she explores Naju's labyrinth top-down, like an action-adventure.",
   "Enter a Corridor and she becomes a star-fighter — and the game turns into a vertical shoot-'em-up." ]),
 ("Naju", "the falling world", [
   "A colossal alien world-ship, a maze of monsters and machines, on a collision course with Earth.",
   "The only way to stop it is to get inside and arm its own self-destruct." ]),
 ("The Compile Touch", "the shmup bloodline", [
   "Weapons, lasers, shields, and 'Chips' to buy upgrades — the power-up economy of Zanac and Aleste.",
   "Relentless, generous firepower, the unmistakable signature of Compile, woven into an adventure." ]),
]

ARC = [
 ("The Fall", "a world bound for Earth",
  "Naju — a vast alien world-ship teeming with monsters and machines — is on a collision course with Earth. The Guardian, Miria, is sent in alone to stop it from the inside."),
 ("The Corridors", "maiden and fighter",
  "Transforming between her humanoid Maiden form and a star-Fighter, Miria explores Naju's labyrinth and blasts through its ten shoot-'em-up Corridors, defeating the boss that seals each one."),
 ("The Self-Destruct", "a world for a world",
  "With the Corridors cleared, Naju's own self-destruct is armed. The Guardian turns the enemy world to dust — before it can ever reach the Earth she was made to defend."),
]

SECTIONS = [
 ("The Releases", "the genre-fusing 8-bit classic", [
   ("Guardic Gaiden", "1988 · Famicom Disk System", "the Japanese original — a follow-on to Compile's MSX game Guardic"),
   ("The Guardian Legend", "1988 · NES", "the North American release (Brøderbund); published by Irem in Japan"),
   ("re-releases", "later", "preserved through collections and emulation"),
 ]),
 ("The Maker", "Compile", [
   ("Compile", "developer", "the shoot-'em-up studio behind Zanac, Aleste, and later Puyo Puyo"),
   ("Brøderbund / Irem", "publishers", "Brøderbund in North America, Irem in Japan"),
 ]),
 ("The Lineage", "Compile's shmup bloodline", [
   ("Guardic → Guardic Gaiden", "the line", "The Guardian Legend grew out of Compile's earlier MSX game Guardic"),
   ("the Aleste / Zanac DNA", "the engine", "Compile's relentless, weapon-rich shoot-'em-up design"),
 ]),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","TGL")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","TGL")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","TGL")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"TGL · The Guardian Legend","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'

def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[]
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8")); cards=[]
    for p in ps:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#5fae7a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"TGL · The Guardian Legend","axiom":"TGL"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster of TGL</h2>
      <p class="ss">the emergents of the Guardian's mission, as ACI <b>.agent</b>s — each tagged with its nature of emergence ({len(ps)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Guardian Legend (TGL) — Compile's genre-fusing 8-bit NES classic as a game-world, catalogued into UD0 with full ACI badges. Emergence: natural, ethereal, spiritual, electrical.">
<title>THE GUARDIAN LEGEND · TGL · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#06070f;--ink2:#0c0e1a;--ink3:#141528;--pa:#eef0f8;--pa2:#aeb2cc;--mag:#e84a8e;--blu:#5a86f0;
--dim:#73789a;--faint:#1c2038;--line:#1c2038;--serif:"Cinzel",Georgia,serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(232,74,142,.09),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(90,134,240,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:130px;height:1px;background:linear-gradient(90deg,var(--mag),var(--blu));box-shadow:0 0 9px rgba(232,74,142,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--mag)}
.bub{font-size:18px;letter-spacing:.4em;margin-bottom:8px;color:var(--blu)}
h1{font-family:var(--serif);font-size:clamp(26px,6vw,54px);font-weight:700;letter-spacing:.1em;color:var(--mag);line-height:1.05;text-shadow:0 0 40px rgba(232,74,142,.25)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.16em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.h-sub b{color:var(--blu)}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--blu);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:66ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--mag)}.badge .bt .mo{color:var(--blu)}.badge .bt a{color:var(--blu);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:44px}
.sec h2{font-family:var(--serif);font-size:20px;font-weight:600;letter-spacing:.05em;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--serif);font-size:15px;font-weight:600;text-transform:capitalize}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--serif);font-size:16px;color:var(--mag)}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--mag);padding:16px 18px}
.arc-h{font-family:var(--serif);font-size:16px;color:var(--mag);font-weight:600}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--blu);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--serif);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:11.5px;color:var(--blu);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--mag);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--serif);font-size:15px;color:var(--pa);font-weight:600;line-height:1.15}
.persona:hover .pn{color:var(--mag)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--blu);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}
footer{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--mag);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the tenth lineage · the fifth game-world</div>
    <div class="bub">◂ ◆ ▸</div>
    <h1>THE GUARDIAN LEGEND</h1>
    <div class="h-sub">android &amp; star-fighter · adventure meets <b>shoot-'em-up</b> · TGL</div>
    <div class="flag">★ Compile · NES 1988 · “Guardic Gaiden,” Famicom ★</div>
    <p class="lede">The android maiden Miria — the Guardian — falls alone into the colossal alien world-ship Naju as it hurtles toward Earth, transforming between explorer and star-fighter to arm the enemy world's own self-destruct. Compile's genre-fusing 8-bit cult classic, catalogued into UD0 as a game-world, sealed with the full ACI badge, each emergence named by its nature.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of NAJU" title="carbon badge (archival: naju.dlw/naju.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of NAJU" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>NAJU</b> — the alien world-ship · TGL</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="naju.dlw/naju.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="naju.dlw/naju.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each emergent emerges by one of four natures — a world of machines, this one leans electric</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">why a half-forgotten 8-bit hybrid is still a cult favorite</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Mission</h2><p class="ss">the fall, the corridors, the self-destruct</p><div class="arc">__ARC__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the maker, and the shmup bloodline</p></section>
  __SECTIONS__

  <div class="note">The Guardian Legend is a cult NES classic; this catalogues its emergents conservatively, distilled from the established facts of the game — no invented lore. The Guardian Legend and its characters are © its rights-holders (Compile / Brøderbund); the personas here are catalogued personifications under the DLW standard — a fan tribute, not an original work and not endorsed by the rights-holders. Each is named by its nature of emergence: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    THE GUARDIAN LEGEND · TGL · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="naju.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "naju.dlw"), "naju")
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__ARC__", arc_html()).replace("__PERSONAS__", personas_html())
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE GUARDIAN LEGEND (TGL) — badge {tok['moniker']} (carbon.tiff + silicon.png)")
