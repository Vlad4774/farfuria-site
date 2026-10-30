"""Generează paginile site-ului Farfuria (python build.py). Textele legale trebuie ținute la fel ca în aplicație."""

import html
import pathlib

CONTACT = "vladbaracut7@yahoo.com"
ACTUALIZAT = "octombrie 2026"
OUT = pathlib.Path(__file__).parent

CSS = """
:root{--bg:#fbf7ee;--top:#eef6d6;--surface:#fff;--border:#e9e2d0;--text:#2b2a26;--dim:#6f6b60;--hl:#5f7f12;--hlsoft:#ecf8cc}
@media (prefers-color-scheme:dark){:root{--bg:#161512;--top:#1f2614;--surface:#211f1b;--border:#36332c;--text:#f4f0e6;--dim:#aba595;--hl:#c6f05a;--hlsoft:#2a3516}}
*{box-sizing:border-box}
body{margin:0;background:linear-gradient(var(--top),var(--bg) 420px) no-repeat,var(--bg);color:var(--text);font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:var(--hl)}
.wrap{max-width:760px;margin:0 auto;padding:24px 16px 64px}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:40px}
.brand{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font-weight:900;font-size:22px;letter-spacing:1px}
.brand img{width:36px;height:36px}
nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px}
nav a{color:var(--dim);text-decoration:none}
nav a:hover{color:var(--text)}
h1{font-size:38px;line-height:1.1;margin:0 0 12px;letter-spacing:-1px}
h2{font-size:20px;margin:32px 0 8px}
.lead{color:var(--dim);font-size:18px;margin:0 0 32px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:32px 0}
.card{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:18px}
.card b{display:block;margin-bottom:4px}
.card span{color:var(--dim);font-size:14px}
.muted{color:var(--dim);font-size:14px}
ol li,ul li{margin-bottom:6px}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--border);color:var(--dim);font-size:14px;display:flex;gap:16px;flex-wrap:wrap}
footer a{color:var(--dim)}
"""


def pagina(fisier, titlu, corp, descriere):
    doc = f"""<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titlu)}</title>
<meta name="description" content="{html.escape(descriere)}">
<link rel="icon" href="favicon.png">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header>
  <a class="brand" href="./"><img src="logo.png" alt="">FARFURIA</a>
  <nav><a href="confidentialitate.html">Confidențialitate</a><a href="termeni.html">Termeni</a><a href="stergere-cont.html">Ștergerea contului</a></nav>
</header>
{corp}
<footer><span>© 2026 Farfuria</span><a href="confidentialitate.html">Politica de confidențialitate</a><a href="termeni.html">Termeni și condiții</a><a href="stergere-cont.html">Ștergerea contului</a><a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</div>
</body>
</html>
"""
    (OUT / fisier).write_text(doc, encoding="utf-8")


def sectiuni(items):
    out = []
    for h, ps in items:
        out.append(f"<h2>{html.escape(h)}</h2>")
        out.extend(f"<p>{html.escape(p)}</p>" for p in ps)
    return "\n".join(out)


TERMENI = [
    ("Cine suntem", [f"Farfuria este o aplicație de planificare a meselor, făcută de un dezvoltator independent din România. Contact: {CONTACT}."]),
    ("Contul tău", [
        "Ai nevoie de un cont ca să folosești Farfuria. Îl poți crea cu adresa de email și o parolă (confirmată cu un cod trimis pe email) sau cu contul Google. Păstrează-ți parola doar pentru tine; ești responsabil pentru ce se întâmplă în contul tău.",
        "Poți șterge contul oricând, din aplicație: Setări → contul meu → șterge contul.",
    ]),
    ("Ce oferă aplicația", [
        "Farfuria îți propune prânzurile și cinele pentru o săptămână, după bugetul, caloriile, gusturile și aparatele tale, cu rețete pas cu pas și lista de cumpărături.",
        "Costurile afișate sunt estimări orientative, calculate din prețuri medii de referință. Prețurile reale din magazine pot fi mai mici sau mai mari.",
    ]),
    ("Versiunea gratuită și Premium", [
        "Farfuria este gratuită: planul pe 7 zile (cu o regenerare pe săptămână), toate rețetele, modul de gătit, lista de cumpărături și contul cu sincronizare. Farfuria Premium este un abonament opțional care adaugă regenerări și alternative nelimitate pentru mese, nutriția avansată (high protein, proteine și carbohidrați pe zi, calculatorul de necesar) și rețetele favorite.",
        "Fiecare cont nou primește Premium gratuit în primele 30 de zile. Nu ai nevoie de card și nu se plătește nimic; după aceea aplicația continuă ca versiune gratuită. Prețul abonamentului și eventuala perioadă de probă sunt afișate în Google Play, în moneda ta, înainte să te abonezi. Abonamentul se reînnoiește automat până îl anulezi.",
        "Plățile, reînnoirile și rambursările sunt gestionate de Google Play. Ca să eviți următoarea plată, anulează cu cel puțin 24 de ore înainte de sfârșitul perioadei: Google Play → Plăți și abonamente → Abonamente.",
    ]),
    ("Sănătate", ["Valorile nutriționale sunt calculate din ingrediente și sunt orientative. Farfuria nu oferă sfaturi medicale. Dacă ai o afecțiune, alergii sau un regim recomandat de medic, verifică rețetele și ingredientele înainte să le gătești."]),
    ("Utilizare corectă", ["Nu folosi serviciul abuziv: fără încercări de a accesa datele altor persoane, de a supraîncărca serverele sau de a ocoli abonamentul."]),
    ("Răspundere", ["Aplicația este oferită „ca atare”. În limitele permise de lege, nu răspundem pentru pierderi de date sau pentru rezultatele rețetelor. Datele tale sunt salvate în cont; poți descărca oricând o copie (Setări → backup și import → exportă datele)."]),
    ("Modificări", ["Putem actualiza acești termeni. Modificările importante vor fi anunțate în aplicație."]),
]

CONFIDENTIALITATE = [
    ("Ce date colectăm", [
        "Contul: adresa de email și parola, păstrată criptat (hash). Dacă te loghezi cu Google, primim de la Google numele, adresa de email și poza de profil, în loc de parolă.",
        "Preferințele pe care le introduci: numărul de persoane, bugetul, câte zile gătești, categoriile preferate, restricțiile alimentare și alimentele excluse, aparatele din bucătărie și obiectivele nutriționale. Dacă folosești calculatorul de calorii, și vârsta, sexul, înălțimea, greutatea, nivelul de activitate și obiectivul.",
        "Ce creezi în aplicație: planurile săptămânale, istoricul lor, rețetele favorite și lista de cumpărături (ce ai bifat și ce ai deja acasă).",
        "Dacă te abonezi: starea abonamentului, de la Google Play. Nu vedem niciodată datele cardului.",
        "Nu folosim localizarea, nu afișăm reclame și nu vindem datele nimănui.",
    ]),
    ("De ce", ["Ca să funcționeze aplicația: să te logăm, să îți generăm planul, să îți salvăm datele și să le sincronizăm între telefoanele tale."]),
    ("Unde sunt păstrate", [
        "Pe telefonul tău și în contul tău, pe serverele Supabase din Uniunea Europeană (Frankfurt, Germania). Datele circulă prin conexiuni criptate, iar fiecare cont își poate citi doar propriile date.",
        "Furnizori: Supabase (baza de date și autentificarea), Google (logarea cu Google), Brevo (trimiterea emailurilor cu codurile de verificare) și, dacă te abonezi, Google Play și RevenueCat (abonamentul).",
    ]),
    ("Permisiuni pe telefon", ["Internet (sincronizarea) și vibrații (timerul din modul de gătit). Aplicația nu cere acces la locație, cameră, microfon sau contacte."]),
    ("Drepturile tale (GDPR)", [
        "Poți vedea și corecta datele direct în aplicație, poți descărca o copie (Setări → backup și import → exportă datele) și poți șterge definitiv contul și toate datele lui (Setări → contul meu → șterge contul).",
        f"Pentru orice altă cerere scrie la {CONTACT}. Poți depune și o plângere la Autoritatea Națională de Supraveghere a Prelucrării Datelor cu Caracter Personal (ANSPDCP).",
    ]),
    ("Cât timp le păstrăm", ["Cât timp există contul. Ștergerea contului elimină datele de pe servere."]),
    ("Vârsta", ["Farfuria nu este destinată copiilor sub 16 ani."]),
]

pagina(
    "index.html",
    "Farfuria – planul de mese al săptămânii",
    """<h1>Ce gătim săptămâna asta?<br>Farfuria îți spune.</h1>
<p class="lead">Farfuria îți face planul de prânzuri și cine pentru 7 zile, după bugetul, caloriile și aparatele tale, apoi îți dă lista de cumpărături gata făcută.</p>
<div class="grid">
  <div class="card"><b>Plan pe 7 zile</b><span>Prânz și cină, în bugetul tău și în limita de calorii.</span></div>
  <div class="card"><b>150 de rețete</b><span>Pas cu pas, cu timere, pentru air fryer, cuptor, aragaz sau slow cooker.</span></div>
  <div class="card"><b>Lista de cumpărături</b><span>Cantitățile adunate pe raioane, cu ce ai deja acasă scos din listă.</span></div>
  <div class="card"><b>Gătești mai rar</b><span>Alegi de câte ori gătești pe săptămână; porțiile se calculează singure.</span></div>
</div>
<p class="muted">Farfuria e gratuită. Conturile noi primesc o lună de Premium gratuit: regenerări nelimitate, nutriție avansată și favorite.</p>
<p class="muted">Întrebări? Scrie-ne la <a href="mailto:""" + CONTACT + """">""" + CONTACT + """</a>.</p>""",
    "Farfuria îți face planul de prânzuri și cine pe o săptămână, după buget, calorii și aparatele tale.",
)

pagina(
    "confidentialitate.html",
    "Politica de confidențialitate – Farfuria",
    f'<h1>Politica de confidențialitate</h1><p class="muted">Ultima actualizare: {ACTUALIZAT}</p>\n' + sectiuni(CONFIDENTIALITATE),
    "Ce date colectează Farfuria, de ce și cum le protejează.",
)

pagina(
    "termeni.html",
    "Termeni și condiții – Farfuria",
    f'<h1>Termeni și condiții</h1><p class="muted">Ultima actualizare: {ACTUALIZAT}</p>\n' + sectiuni(TERMENI),
    "Termenii de utilizare a aplicației Farfuria.",
)

pagina(
    "stergere-cont.html",
    "Ștergerea contului – Farfuria",
    f"""<h1>Șterge-ți contul Farfuria</h1>
<p class="lead">Poți șterge definitiv contul și toate datele lui, oricând.</p>
<h2>Din aplicație</h2>
<ol>
  <li>Deschide Farfuria și mergi la <b>Setări → contul meu</b>.</li>
  <li>La final, scrie <b>STERGE</b> în câmpul de confirmare și apasă <b>șterge contul</b>.</li>
</ol>
<p>Opțional: înainte de ștergere, din <b>Setări → backup și import → exportă datele</b> îți poți păstra o copie a planurilor și preferințelor.</p>
<h2>Prin email</h2>
<p>Dacă nu mai poți deschide aplicația, scrie la <a href="mailto:{CONTACT}?subject=%C8%98tergerea%20contului%20Farfuria">{CONTACT}</a> de pe adresa de email a contului și cere ștergerea. O facem în cel mult 30 de zile.</p>
<h2>Ce se șterge</h2>
<p>Contul, preferințele, planurile, favoritele și lista de cumpărături sunt eliminate definitiv de pe servere. Nu păstrăm nimic. Un abonament din Google Play trebuie anulat separat, din Google Play.</p>""",
    "Cum îți ștergi contul și datele din Farfuria.",
)
print("gata")
