"""Generează paginile site-ului Plate (python build.py), în 5 limbi.

Româna rămâne la rădăcină (linkurile vechi și cel din Google Play merg în continuare), celelalte în en/, es/, fr/, de/.
Textele legale trebuie ținute la fel ca în aplicație.
"""

import html
import pathlib

CONTACT = "vladbaracut7@yahoo.com"
OUT = pathlib.Path(__file__).parent
LIMBI = [("ro", "Română"), ("en", "English"), ("es", "Español"), ("fr", "Français"), ("de", "Deutsch")]

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
.limbi{display:flex;gap:10px;flex-wrap:wrap;font-size:13px;margin:-24px 0 32px}
.limbi a{color:var(--dim);text-decoration:none}
.limbi b{color:var(--text)}
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

# ---------------------------------------------------------------------------------------------
# Textele, pe limbi. Paragrafele sunt text simplu; {C} = adresa de contact.
# ---------------------------------------------------------------------------------------------

T = {}

T["ro"] = dict(
    actualizat="noiembrie 2026",
    nav=("Confidențialitate", "Termeni", "Ștergerea contului"),
    footer=("Politica de confidențialitate", "Termeni și condiții", "Ștergerea contului"),
    index_titlu="Plate – planul de mese al săptămânii",
    index_desc="Plate îți face planul de mese pe o săptămână, după buget, calorii și aparatele tale.",
    index_h1="Ce gătim săptămâna asta?<br>Plate îți spune.",
    index_lead="Plate îți face planul de mese pentru 7 zile (mic dejun, prânz, cină și gustări), după bugetul, caloriile și aparatele tale, apoi îți dă lista de cumpărături gata făcută.",
    carduri=[
        ("Plan pe 7 zile", "Mesele pe care le alegi, în bugetul tău și în limita de calorii."),
        ("800 de rețete", "Pas cu pas, cu timere, pentru air fryer, cuptor, aragaz, microunde sau slow cooker."),
        ("Lista de cumpărături", "Cantitățile adunate pe raioane, cu ce ai deja acasă scos din listă."),
        ("5 limbi", "Română, engleză, spaniolă, franceză și germană, cu prețuri în moneda ta."),
    ],
    index_note=[
        "Plate e gratuit, cu reclame. Conturile noi primesc o lună de Premium gratuit: fără reclame, regenerări nelimitate, nutriție avansată și favorite.",
        "Întrebări? Scrie-ne la {C}.",
    ],
    conf_titlu="Politica de confidențialitate – Plate", conf_h1="Politica de confidențialitate", conf_desc="Ce date colectează Plate, de ce și cum le protejează.",
    term_titlu="Termeni și condiții – Plate", term_h1="Termeni și condiții", term_desc="Termenii de utilizare a aplicației Plate.",
    ultima="Ultima actualizare",
    termeni=[
        ("Cine suntem", ["Plate este o aplicație de planificare a meselor, făcută de un dezvoltator independent din România. Contact: {C}."]),
        ("Contul tău", [
            "Ai nevoie de un cont ca să folosești Plate. Îl poți crea cu adresa de email și o parolă (confirmată cu un cod trimis pe email) sau cu contul Google. Păstrează-ți parola doar pentru tine; ești responsabil pentru ce se întâmplă în contul tău.",
            "Poți șterge contul oricând, din aplicație: Setări → Șterge contul.",
        ]),
        ("Ce oferă aplicația", [
            "Plate îți propune mesele pentru o săptămână (mic dejun, prânz, cină și gustări, cum alegi tu), după bugetul, caloriile, gusturile și aparatele tale, cu rețete pas cu pas și lista de cumpărături.",
            "Costurile afișate sunt estimări orientative, calculate din prețuri medii de referință din țara aleasă. Prețurile reale din magazine pot fi mai mici sau mai mari.",
            "Rețetele sunt scrise în română și traduse în celelalte limbi. Dacă o traducere ți se pare neclară, cantitățile, temperaturile și timpii sunt aceiași ca în original.",
        ]),
        ("Versiunea gratuită și Premium", [
            "Plate este gratuit: planul pe 7 zile (cu o regenerare pe săptămână), toate rețetele, modul de gătit, lista de cumpărături și contul cu sincronizare. Versiunea gratuită afișează reclame. Plate Premium este un abonament opțional, fără reclame, care adaugă regenerări și alternative nelimitate pentru mese, nutriția avansată (high protein, proteine și carbohidrați pe zi, calculatorul de necesar) și rețetele favorite.",
            "Fiecare cont nou primește Premium gratuit în primele 30 de zile. Nu ai nevoie de card și nu se plătește nimic; după aceea aplicația continuă ca versiune gratuită. Prețul abonamentului și eventuala perioadă de probă sunt afișate în Google Play, în moneda ta, înainte să te abonezi. Abonamentul se reînnoiește automat până îl anulezi.",
            "Plățile, reînnoirile și rambursările sunt gestionate de Google Play. Ca să eviți următoarea plată, anulează cu cel puțin 24 de ore înainte de sfârșitul perioadei: Google Play → Plăți și abonamente → Abonamente.",
        ]),
        ("Recenzii", [
            "Poți da o notă de la 1 la 5 stele unei rețete și poți scrie un comentariu scurt. Recenzia apare pentru toți utilizatorii, cu numele de afișare ales de tine.",
            "Scrie doar despre rețetă. Nu publica date personale, reclame, insulte sau conținut ilegal. Oricine poate raporta o recenzie, iar recenziile care încalcă aceste reguli pot fi șterse fără avertisment. Îți poți modifica sau șterge oricând propria recenzie.",
        ]),
        ("Sănătate", ["Valorile nutriționale sunt calculate din ingrediente și sunt orientative. Plate nu oferă sfaturi medicale. Dacă ai o afecțiune, alergii sau un regim recomandat de medic, verifică rețetele și ingredientele înainte să le gătești."]),
        ("Utilizare corectă", ["Nu folosi serviciul abuziv: fără încercări de a accesa datele altor persoane, de a supraîncărca serverele sau de a ocoli abonamentul."]),
        ("Răspundere", ["Aplicația este oferită „ca atare”. În limitele permise de lege, nu răspundem pentru pierderi de date sau pentru rezultatele rețetelor. Datele tale sunt salvate în cont; poți descărca oricând o copie a datelor personale (Setări → Exportă datele)."]),
        ("Modificări", ["Putem actualiza acești termeni. Modificările importante vor fi anunțate în aplicație. Versiunea în română este cea de referință."]),
    ],
    confidentialitate=[
        ("Ce date colectăm", [
            "Contul: adresa de email și parola, păstrată criptat (hash). Dacă te loghezi cu Google, primim de la Google numele, adresa de email și poza de profil, în loc de parolă.",
            "Preferințele pe care le introduci: limba aplicației, numărul de persoane, bugetul, câte zile gătești, categoriile preferate, restricțiile alimentare și alimentele excluse, aparatele din bucătărie și obiectivele nutriționale. Dacă folosești calculatorul de calorii, și vârsta, sexul, înălțimea, greutatea, nivelul de activitate și obiectivul.",
            "Ce creezi în aplicație: planurile săptămânale, istoricul lor, rețetele favorite, lista de cumpărături (ce ai bifat și ce ai deja acasă) și recenziile pe care le scrii.",
            "Dacă te abonezi: starea abonamentului, de la Google Play. Nu vedem niciodată datele cardului.",
            "Nu folosim localizarea telefonului și nu vindem datele nimănui.",
        ]),
        ("Recenziile sunt publice", [
            "Dacă scrii o recenzie, nota, comentariul, numele de afișare ales de tine și data apar pentru ceilalți utilizatori Plate. Adresa de email nu este afișată niciodată.",
            "Dacă cineva raportează o recenzie, administratorul vede recenzia raportată și o poate șterge. Îți poți șterge oricând recenzia, iar la ștergerea contului dispar și recenziile tale.",
        ]),
        ("Reclame (doar în versiunea gratuită)", [
            "Versiunea gratuită afișează reclame prin Google AdMob: un banner la capătul unor pagini și, cel mult o dată pe zi, o reclamă pe tot ecranul după ce termini o rețetă în modul de gătit. Cu Premium (inclusiv în luna de bun venit) nu vezi reclame.",
            "La prima pornire după configurarea inițială îți cerem acordul printr-un formular Google. Poți alege reclame personalizate sau nepersonalizate și îți poți schimba oricând alegerea din Setări → alegeri despre reclame.",
            "Pentru afișarea și măsurarea reclamelor, Google și partenerii săi pot folosi identificatorul de publicitate al telefonului, adresa IP (din care se poate deduce o localizare aproximativă) și informații despre dispozitiv și despre interacțiunea cu reclamele. Nu le trimitem planurile, preferințele sau alte date din contul tău. Detalii: policies.google.com/technologies/ads.",
        ]),
        ("De ce", ["Ca să funcționeze aplicația: să te logăm, să îți generăm planul, să îți salvăm datele, să le sincronizăm între telefoanele tale și să îți trimitem emailurile cu coduri în limba ta."]),
        ("Unde sunt păstrate", [
            "Pe telefonul tău și în contul tău, pe serverele Supabase din Uniunea Europeană (Frankfurt, Germania). Datele circulă prin conexiuni criptate, iar fiecare cont își poate citi doar propriile date (cu excepția recenziilor, care sunt publice).",
            "Furnizori: Supabase (baza de date și autentificarea), Google (logarea cu Google), Brevo (trimiterea emailurilor cu codurile de verificare), Google AdMob (reclamele din versiunea gratuită) și, dacă te abonezi, Google Play și RevenueCat (abonamentul).",
        ]),
        ("Permisiuni pe telefon", ["Internet (sincronizarea și reclamele), vibrații (timerul din modul de gătit) și identificatorul de publicitate (reclamele din versiunea gratuită; îl poți reseta sau șterge din setările telefonului). Aplicația nu cere acces la locație, cameră, microfon sau contacte."]),
        ("Drepturile tale (GDPR)", [
            "Poți vedea și corecta datele direct în aplicație, poți descărca o copie a datelor personale, în format CSV (Setări → Exportă datele) și poți șterge definitiv contul și toate datele lui (Setări → Șterge contul).",
            "Pentru orice altă cerere scrie la {C}. Poți depune și o plângere la autoritatea de protecție a datelor din țara ta; în România, aceasta este ANSPDCP.",
        ]),
        ("Cât timp le păstrăm", ["Cât timp există contul. Ștergerea contului elimină datele de pe servere."]),
        ("Vârsta", ["Plate nu este destinat copiilor sub 16 ani."]),
    ],
    sterg_titlu="Ștergerea contului – Plate", sterg_desc="Cum îți ștergi contul și datele din Plate.",
    sterg_h1="Șterge-ți contul Plate", sterg_lead="Poți șterge definitiv contul și toate datele lui, oricând.",
    sterg_app="Din aplicație",
    sterg_pasi=["Deschide Plate și mergi la <b>Setări → Șterge contul</b>.", "Scrie <b>STERGE</b> în câmpul de confirmare și apasă <b>Șterge contul</b>."],
    sterg_export="Opțional: înainte de ștergere, din <b>Setări → Exportă datele</b> îți poți păstra o copie a datelor tale (CSV).",
    sterg_email_h="Prin email",
    sterg_email="Dacă nu mai poți deschide aplicația, scrie la {L} de pe adresa de email a contului și cere ștergerea. O facem în cel mult 30 de zile.",
    sterg_subiect="Ștergerea contului Plate",
    sterg_ce_h="Ce se șterge",
    sterg_ce="Contul, preferințele, planurile, favoritele, lista de cumpărături și recenziile sunt eliminate definitiv de pe servere. Nu păstrăm nimic. Un abonament din Google Play trebuie anulat separat, din Google Play.",
)

T["en"] = dict(
    actualizat="November 2026",
    nav=("Privacy", "Terms", "Delete account"),
    footer=("Privacy policy", "Terms and conditions", "Delete your account"),
    index_titlu="Plate – your weekly meal plan",
    index_desc="Plate makes your meal plan for the week, based on your budget, calories and kitchen appliances.",
    index_h1="What are we cooking this week?<br>Plate tells you.",
    index_lead="Plate plans your meals for 7 days (breakfast, lunch, dinner and snacks) based on your budget, calories and appliances, then gives you a ready-made shopping list.",
    carduri=[
        ("7-day plan", "The meals you choose, within your budget and calorie limit."),
        ("800 recipes", "Step by step, with timers, for the air fryer, oven, hob, microwave or slow cooker."),
        ("Shopping list", "Quantities added up by aisle, with what you already have at home taken off."),
        ("5 languages", "English, Spanish, French, German and Romanian, with prices in your currency."),
    ],
    index_note=[
        "Plate is free, with ads. New accounts get one month of Premium for free: no ads, unlimited regenerations, advanced nutrition and favourites.",
        "Questions? Write to us at {C}.",
    ],
    conf_titlu="Privacy policy – Plate", conf_h1="Privacy policy", conf_desc="What data Plate collects, why, and how it is protected.",
    term_titlu="Terms and conditions – Plate", term_h1="Terms and conditions", term_desc="The terms of use of the Plate app.",
    ultima="Last updated",
    termeni=[
        ("Who we are", ["Plate is a meal planning app made by an independent developer from Romania. Contact: {C}."]),
        ("Your account", [
            "You need an account to use Plate. You can create one with your email address and a password (confirmed with a code sent by email) or with your Google account. Keep your password to yourself; you are responsible for what happens in your account.",
            "You can delete your account at any time in the app: Settings → Delete account.",
        ]),
        ("What the app offers", [
            "Plate suggests your meals for a week (breakfast, lunch, dinner and snacks, as you choose) based on your budget, calories, tastes and appliances, with step-by-step recipes and a shopping list.",
            "The costs shown are rough estimates, calculated from average reference prices in the selected country. Actual shop prices may be lower or higher.",
            "Recipes are written in Romanian and translated into the other languages. If a translation seems unclear, the quantities, temperatures and times are the same as in the original.",
        ]),
        ("Free version and Premium", [
            "Plate is free: the 7-day plan (with one regeneration per week), all recipes, cooking mode, the shopping list and an account with sync. The free version shows ads. Plate Premium is an optional, ad-free subscription that adds unlimited regenerations and meal alternatives, advanced nutrition (high protein, daily protein and carbs, the needs calculator) and favourite recipes.",
            "Every new account gets Premium for free for the first 30 days. You don't need a card and nothing is charged; afterwards the app continues as the free version. The subscription price and any free trial are shown in Google Play, in your currency, before you subscribe. The subscription renews automatically until you cancel it.",
            "Payments, renewals and refunds are handled by Google Play. To avoid the next charge, cancel at least 24 hours before the end of the period: Google Play → Payments and subscriptions → Subscriptions.",
        ]),
        ("Reviews", [
            "You can rate a recipe from 1 to 5 stars and write a short comment. Your review is visible to all users, with the display name you choose.",
            "Only write about the recipe. Don't post personal data, advertising, insults or illegal content. Anyone can report a review, and reviews that break these rules may be deleted without notice. You can edit or delete your own review at any time.",
        ]),
        ("Health", ["Nutritional values are calculated from the ingredients and are approximate. Plate does not give medical advice. If you have a medical condition, allergies or a diet prescribed by a doctor, check the recipes and ingredients before cooking them."]),
        ("Fair use", ["Don't abuse the service: no attempts to access other people's data, overload the servers or bypass the subscription."]),
        ("Liability", ["The app is provided \"as is\". To the extent permitted by law, we are not liable for data loss or for the results of the recipes. Your data is saved in your account; you can download a copy of your personal data at any time (Settings → Export data)."]),
        ("Changes", ["We may update these terms. Important changes will be announced in the app. The Romanian version is the reference version."]),
    ],
    confidentialitate=[
        ("What data we collect", [
            "Your account: your email address and password, stored encrypted (hashed). If you sign in with Google, we receive your name, email address and profile picture from Google instead of a password.",
            "The preferences you enter: the app language, number of people, budget, how many days you cook, favourite categories, dietary restrictions and excluded foods, kitchen appliances and nutrition goals. If you use the calorie calculator, also your age, sex, height, weight, activity level and goal.",
            "What you create in the app: weekly plans and their history, favourite recipes, the shopping list (what you've ticked and what you already have) and the reviews you write.",
            "If you subscribe: your subscription status, from Google Play. We never see your card details.",
            "We don't use your phone's location and we don't sell data to anyone.",
        ]),
        ("Reviews are public", [
            "If you write a review, your rating, comment, chosen display name and the date are visible to other Plate users. Your email address is never shown.",
            "If someone reports a review, the administrator can see the reported review and delete it. You can delete your review at any time, and your reviews are removed when you delete your account.",
        ]),
        ("Ads (free version only)", [
            "The free version shows ads through Google AdMob: a banner at the bottom of some pages and, at most once a day, a full-screen ad after you finish a recipe in cooking mode. With Premium (including the welcome month) you don't see ads.",
            "The first time you open the app after the initial setup, we ask for your consent with a Google form. You can choose personalised or non-personalised ads and change your choice at any time in Settings → ad choices.",
            "To show and measure ads, Google and its partners may use your phone's advertising ID, your IP address (from which an approximate location can be inferred) and information about your device and how you interact with ads. We don't send them your plans, preferences or any other data from your account. Details: policies.google.com/technologies/ads.",
        ]),
        ("Why", ["To make the app work: to sign you in, create your plan, save your data, sync it between your phones and send you the code emails in your language."]),
        ("Where it is stored", [
            "On your phone and in your account, on Supabase servers in the European Union (Frankfurt, Germany). Data travels over encrypted connections, and each account can only read its own data (except reviews, which are public).",
            "Providers: Supabase (database and authentication), Google (Google sign-in), Brevo (sending the verification code emails), Google AdMob (ads in the free version) and, if you subscribe, Google Play and RevenueCat (the subscription).",
        ]),
        ("Phone permissions", ["Internet (sync and ads), vibration (the cooking mode timer) and the advertising ID (ads in the free version; you can reset or delete it in your phone's settings). The app does not ask for access to your location, camera, microphone or contacts."]),
        ("Your rights (GDPR)", [
            "You can view and correct your data directly in the app, download a copy of your personal data in CSV format (Settings → Export data) and permanently delete your account and all its data (Settings → Delete account).",
            "For any other request, write to {C}. You can also lodge a complaint with the data protection authority in your country; in Romania, this is the ANSPDCP.",
        ]),
        ("How long we keep it", ["For as long as your account exists. Deleting your account removes the data from the servers."]),
        ("Age", ["Plate is not intended for children under 16."]),
    ],
    sterg_titlu="Delete your account – Plate", sterg_desc="How to delete your Plate account and data.",
    sterg_h1="Delete your Plate account", sterg_lead="You can permanently delete your account and all its data at any time.",
    sterg_app="In the app",
    sterg_pasi=["Open Plate and go to <b>Settings → Delete account</b>.", "Type <b>DELETE</b> in the confirmation field and tap <b>Delete account</b>."],
    sterg_export="Optional: before deleting, you can keep a copy of your data (CSV) from <b>Settings → Export data</b>.",
    sterg_email_h="By email",
    sterg_email="If you can no longer open the app, write to {L} from your account's email address and ask for deletion. We will do it within 30 days.",
    sterg_subiect="Delete my Plate account",
    sterg_ce_h="What is deleted",
    sterg_ce="Your account, preferences, plans, favourites, shopping list and reviews are permanently removed from the servers. We keep nothing. A Google Play subscription has to be cancelled separately, in Google Play.",
)

T["es"] = dict(
    actualizat="noviembre de 2026",
    nav=("Privacidad", "Términos", "Eliminar la cuenta"),
    footer=("Política de privacidad", "Términos y condiciones", "Eliminar la cuenta"),
    index_titlu="Plate – tu plan de comidas semanal",
    index_desc="Plate prepara tu plan de comidas de la semana según tu presupuesto, tus calorías y tus electrodomésticos.",
    index_h1="¿Qué cocinamos esta semana?<br>Plate te lo dice.",
    index_lead="Plate planifica tus comidas para 7 días (desayuno, almuerzo, cena y tentempiés) según tu presupuesto, tus calorías y tus electrodomésticos, y te da la lista de la compra ya hecha.",
    carduri=[
        ("Plan de 7 días", "Las comidas que eliges, dentro de tu presupuesto y tu límite de calorías."),
        ("800 recetas", "Paso a paso, con temporizadores, para air fryer, horno, fogón, microondas o slow cooker."),
        ("Lista de la compra", "Cantidades sumadas por secciones, sin lo que ya tienes en casa."),
        ("5 idiomas", "Español, inglés, francés, alemán y rumano, con precios en tu moneda."),
    ],
    index_note=[
        "Plate es gratis, con anuncios. Las cuentas nuevas reciben un mes de Premium gratis: sin anuncios, regeneraciones ilimitadas, nutrición avanzada y favoritos.",
        "¿Preguntas? Escríbenos a {C}.",
    ],
    conf_titlu="Política de privacidad – Plate", conf_h1="Política de privacidad", conf_desc="Qué datos recoge Plate, por qué y cómo los protege.",
    term_titlu="Términos y condiciones – Plate", term_h1="Términos y condiciones", term_desc="Los términos de uso de la app Plate.",
    ultima="Última actualización",
    termeni=[
        ("Quiénes somos", ["Plate es una app de planificación de comidas creada por un desarrollador independiente de Rumanía. Contacto: {C}."]),
        ("Tu cuenta", [
            "Necesitas una cuenta para usar Plate. Puedes crearla con tu correo electrónico y una contraseña (confirmada con un código enviado por correo) o con tu cuenta de Google. Guarda tu contraseña solo para ti; eres responsable de lo que ocurra en tu cuenta.",
            "Puedes eliminar tu cuenta en cualquier momento desde la app: Ajustes → Eliminar cuenta.",
        ]),
        ("Qué ofrece la app", [
            "Plate te propone las comidas de una semana (desayuno, almuerzo, cena y tentempiés, como elijas) según tu presupuesto, calorías, gustos y electrodomésticos, con recetas paso a paso y la lista de la compra.",
            "Los costes que se muestran son estimaciones orientativas, calculadas a partir de precios medios de referencia del país elegido. Los precios reales de las tiendas pueden ser más bajos o más altos.",
            "Las recetas están escritas en rumano y traducidas a los demás idiomas. Si una traducción te parece poco clara, las cantidades, temperaturas y tiempos son los mismos que en el original.",
        ]),
        ("Versión gratuita y Premium", [
            "Plate es gratis: el plan de 7 días (con una regeneración por semana), todas las recetas, el modo de cocina, la lista de la compra y la cuenta con sincronización. La versión gratuita muestra anuncios. Plate Premium es una suscripción opcional, sin anuncios, que añade regeneraciones y alternativas ilimitadas para las comidas, nutrición avanzada (high protein, proteínas y carbohidratos por día, calculadora de necesidades) y recetas favoritas.",
            "Cada cuenta nueva recibe Premium gratis durante los primeros 30 días. No necesitas tarjeta y no se cobra nada; después, la app sigue como versión gratuita. El precio de la suscripción y el posible periodo de prueba se muestran en Google Play, en tu moneda, antes de suscribirte. La suscripción se renueva automáticamente hasta que la canceles.",
            "Los pagos, las renovaciones y los reembolsos los gestiona Google Play. Para evitar el siguiente cobro, cancela al menos 24 horas antes del final del periodo: Google Play → Pagos y suscripciones → Suscripciones.",
        ]),
        ("Reseñas", [
            "Puedes valorar una receta de 1 a 5 estrellas y escribir un comentario breve. Tu reseña la ven todos los usuarios, con el nombre que elijas mostrar.",
            "Escribe solo sobre la receta. No publiques datos personales, publicidad, insultos ni contenido ilegal. Cualquiera puede denunciar una reseña, y las reseñas que incumplan estas normas pueden eliminarse sin aviso. Puedes editar o eliminar tu propia reseña en cualquier momento.",
        ]),
        ("Salud", ["Los valores nutricionales se calculan a partir de los ingredientes y son orientativos. Plate no ofrece consejo médico. Si tienes una enfermedad, alergias o una dieta indicada por tu médico, revisa las recetas y los ingredientes antes de cocinarlos."]),
        ("Uso correcto", ["No hagas un uso abusivo del servicio: sin intentos de acceder a datos de otras personas, sobrecargar los servidores o eludir la suscripción."]),
        ("Responsabilidad", ["La app se ofrece «tal cual». En la medida en que la ley lo permita, no respondemos de pérdidas de datos ni de los resultados de las recetas. Tus datos se guardan en tu cuenta; puedes descargar en cualquier momento una copia de tus datos personales (Ajustes → Exportar datos)."]),
        ("Cambios", ["Podemos actualizar estos términos. Los cambios importantes se anunciarán en la app. La versión de referencia es la versión en rumano."]),
    ],
    confidentialitate=[
        ("Qué datos recogemos", [
            "La cuenta: tu correo electrónico y tu contraseña, guardada cifrada (hash). Si entras con Google, recibimos de Google tu nombre, tu correo y tu foto de perfil en lugar de una contraseña.",
            "Las preferencias que introduces: el idioma de la app, el número de personas, el presupuesto, cuántos días cocinas, las categorías favoritas, las restricciones alimentarias y los alimentos excluidos, los electrodomésticos y los objetivos nutricionales. Si usas la calculadora de calorías, también la edad, el sexo, la altura, el peso, el nivel de actividad y el objetivo.",
            "Lo que creas en la app: los planes semanales y su historial, las recetas favoritas, la lista de la compra (lo que has marcado y lo que ya tienes) y las reseñas que escribes.",
            "Si te suscribes: el estado de la suscripción, desde Google Play. Nunca vemos los datos de tu tarjeta.",
            "No usamos la ubicación del teléfono y no vendemos los datos a nadie.",
        ]),
        ("Las reseñas son públicas", [
            "Si escribes una reseña, tu valoración, tu comentario, el nombre que elijas mostrar y la fecha son visibles para los demás usuarios de Plate. Tu correo electrónico nunca se muestra.",
            "Si alguien denuncia una reseña, el administrador puede verla y eliminarla. Puedes eliminar tu reseña en cualquier momento, y tus reseñas se eliminan al eliminar tu cuenta.",
        ]),
        ("Anuncios (solo en la versión gratuita)", [
            "La versión gratuita muestra anuncios mediante Google AdMob: un banner al final de algunas páginas y, como máximo una vez al día, un anuncio a pantalla completa al terminar una receta en el modo de cocina. Con Premium (incluido el mes de bienvenida) no ves anuncios.",
            "La primera vez que abres la app tras la configuración inicial te pedimos el consentimiento con un formulario de Google. Puedes elegir anuncios personalizados o no personalizados y cambiar tu elección en cualquier momento en Ajustes → opciones de anuncios.",
            "Para mostrar y medir los anuncios, Google y sus socios pueden usar el identificador de publicidad del teléfono, la dirección IP (de la que se puede deducir una ubicación aproximada) e información sobre el dispositivo y la interacción con los anuncios. No les enviamos tus planes, preferencias ni otros datos de tu cuenta. Más información: policies.google.com/technologies/ads.",
        ]),
        ("Para qué", ["Para que la app funcione: iniciar tu sesión, generar tu plan, guardar tus datos, sincronizarlos entre tus teléfonos y enviarte los correos con códigos en tu idioma."]),
        ("Dónde se guardan", [
            "En tu teléfono y en tu cuenta, en los servidores de Supabase de la Unión Europea (Fráncfort, Alemania). Los datos viajan por conexiones cifradas y cada cuenta solo puede leer sus propios datos (excepto las reseñas, que son públicas).",
            "Proveedores: Supabase (base de datos y autenticación), Google (acceso con Google), Brevo (envío de los correos con códigos de verificación), Google AdMob (anuncios de la versión gratuita) y, si te suscribes, Google Play y RevenueCat (la suscripción).",
        ]),
        ("Permisos del teléfono", ["Internet (sincronización y anuncios), vibración (temporizador del modo de cocina) e identificador de publicidad (anuncios de la versión gratuita; puedes restablecerlo o eliminarlo en los ajustes del teléfono). La app no pide acceso a la ubicación, la cámara, el micrófono ni los contactos."]),
        ("Tus derechos (RGPD)", [
            "Puedes ver y corregir tus datos directamente en la app, descargar una copia de tus datos personales en formato CSV (Ajustes → Exportar datos) y eliminar definitivamente tu cuenta y todos sus datos (Ajustes → Eliminar cuenta).",
            "Para cualquier otra solicitud, escribe a {C}. También puedes presentar una reclamación ante la autoridad de protección de datos de tu país; en España, la Agencia Española de Protección de Datos (AEPD).",
        ]),
        ("Cuánto tiempo los guardamos", ["Mientras exista la cuenta. Al eliminar la cuenta se borran los datos de los servidores."]),
        ("Edad", ["Plate no está destinada a menores de 16 años."]),
    ],
    sterg_titlu="Eliminar la cuenta – Plate", sterg_desc="Cómo eliminar tu cuenta y tus datos de Plate.",
    sterg_h1="Elimina tu cuenta de Plate", sterg_lead="Puedes eliminar definitivamente tu cuenta y todos sus datos en cualquier momento.",
    sterg_app="Desde la app",
    sterg_pasi=["Abre Plate y ve a <b>Ajustes → Eliminar cuenta</b>.", "Escribe <b>ELIMINAR</b> en el campo de confirmación y pulsa <b>Eliminar cuenta</b>."],
    sterg_export="Opcional: antes de eliminarla, puedes guardar una copia de tus datos (CSV) desde <b>Ajustes → Exportar datos</b>.",
    sterg_email_h="Por correo electrónico",
    sterg_email="Si ya no puedes abrir la app, escribe a {L} desde el correo de tu cuenta y pide la eliminación. La haremos en un plazo máximo de 30 días.",
    sterg_subiect="Eliminar mi cuenta de Plate",
    sterg_ce_h="Qué se elimina",
    sterg_ce="La cuenta, las preferencias, los planes, los favoritos, la lista de la compra y las reseñas se eliminan definitivamente de los servidores. No guardamos nada. Una suscripción de Google Play debe cancelarse por separado, en Google Play.",
)

T["fr"] = dict(
    actualizat="novembre 2026",
    nav=("Confidentialité", "Conditions", "Supprimer le compte"),
    footer=("Politique de confidentialité", "Conditions générales", "Supprimer le compte"),
    index_titlu="Plate – ton planning de repas de la semaine",
    index_desc="Plate prépare ton planning de repas de la semaine selon ton budget, tes calories et tes appareils.",
    index_h1="On cuisine quoi cette semaine ?<br>Plate te le dit.",
    index_lead="Plate planifie tes repas sur 7 jours (petit-déjeuner, déjeuner, dîner et en-cas) selon ton budget, tes calories et tes appareils, puis te donne la liste de courses toute prête.",
    carduri=[
        ("Planning sur 7 jours", "Les repas que tu choisis, dans ton budget et ta limite de calories."),
        ("800 recettes", "Pas à pas, avec minuteurs, pour air fryer, four, plaque, micro-ondes ou mijoteuse."),
        ("Liste de courses", "Les quantités regroupées par rayon, sans ce que tu as déjà à la maison."),
        ("5 langues", "Français, anglais, espagnol, allemand et roumain, avec les prix dans ta monnaie."),
    ],
    index_note=[
        "Plate est gratuit, avec des publicités. Les nouveaux comptes reçoivent un mois de Premium offert : sans publicité, régénérations illimitées, nutrition avancée et favoris.",
        "Des questions ? Écris-nous à {C}.",
    ],
    conf_titlu="Politique de confidentialité – Plate", conf_h1="Politique de confidentialité", conf_desc="Quelles données Plate collecte, pourquoi et comment elles sont protégées.",
    term_titlu="Conditions générales – Plate", term_h1="Conditions générales d’utilisation", term_desc="Les conditions d’utilisation de l’application Plate.",
    ultima="Dernière mise à jour",
    termeni=[
        ("Qui sommes-nous", ["Plate est une application de planification des repas, créée par un développeur indépendant basé en Roumanie. Contact : {C}."]),
        ("Ton compte", [
            "Tu as besoin d’un compte pour utiliser Plate. Tu peux le créer avec ton adresse email et un mot de passe (confirmé par un code envoyé par email) ou avec ton compte Google. Garde ton mot de passe pour toi ; tu es responsable de ce qui se passe dans ton compte.",
            "Tu peux supprimer ton compte à tout moment dans l’application : Réglages → Supprimer le compte.",
        ]),
        ("Ce que propose l’application", [
            "Plate te propose les repas d’une semaine (petit-déjeuner, déjeuner, dîner et en-cas, comme tu veux) selon ton budget, tes calories, tes goûts et tes appareils, avec des recettes pas à pas et la liste de courses.",
            "Les coûts affichés sont des estimations indicatives, calculées à partir de prix moyens de référence du pays choisi. Les prix réels en magasin peuvent être plus bas ou plus élevés.",
            "Les recettes sont rédigées en roumain et traduites dans les autres langues. Si une traduction te semble peu claire, les quantités, températures et temps sont les mêmes que dans l’original.",
        ]),
        ("Version gratuite et Premium", [
            "Plate est gratuit : le planning sur 7 jours (avec une régénération par semaine), toutes les recettes, le mode cuisine, la liste de courses et le compte avec synchronisation. La version gratuite affiche des publicités. Plate Premium est un abonnement facultatif, sans publicité, qui ajoute des régénérations et des alternatives illimitées pour les repas, la nutrition avancée (high protein, protéines et glucides par jour, calculateur de besoins) et les recettes favorites.",
            "Chaque nouveau compte reçoit Premium gratuitement pendant les 30 premiers jours. Tu n’as pas besoin de carte et rien n’est facturé ; ensuite, l’application continue en version gratuite. Le prix de l’abonnement et l’éventuelle période d’essai sont affichés dans Google Play, dans ta monnaie, avant que tu t’abonnes. L’abonnement se renouvelle automatiquement jusqu’à ce que tu l’annules.",
            "Les paiements, renouvellements et remboursements sont gérés par Google Play. Pour éviter le prochain prélèvement, annule au moins 24 heures avant la fin de la période : Google Play → Paiements et abonnements → Abonnements.",
        ]),
        ("Avis", [
            "Tu peux noter une recette de 1 à 5 étoiles et écrire un court commentaire. Ton avis est visible par tous les utilisateurs, avec le nom d’affichage que tu choisis.",
            "Écris uniquement au sujet de la recette. Ne publie ni données personnelles, ni publicité, ni insultes, ni contenu illégal. Tout le monde peut signaler un avis, et les avis qui enfreignent ces règles peuvent être supprimés sans préavis. Tu peux modifier ou supprimer ton propre avis à tout moment.",
        ]),
        ("Santé", ["Les valeurs nutritionnelles sont calculées à partir des ingrédients et sont indicatives. Plate ne donne pas de conseils médicaux. Si tu as une maladie, des allergies ou un régime prescrit par un médecin, vérifie les recettes et les ingrédients avant de les cuisiner."]),
        ("Utilisation correcte", ["N’utilise pas le service de manière abusive : pas de tentatives d’accéder aux données d’autres personnes, de surcharger les serveurs ou de contourner l’abonnement."]),
        ("Responsabilité", ["L’application est fournie « telle quelle ». Dans les limites prévues par la loi, nous ne sommes pas responsables des pertes de données ni du résultat des recettes. Tes données sont enregistrées dans ton compte ; tu peux télécharger à tout moment une copie de tes données personnelles (Réglages → Exporter les données)."]),
        ("Modifications", ["Nous pouvons mettre à jour ces conditions. Les changements importants seront annoncés dans l’application. La version en roumain fait foi."]),
    ],
    confidentialitate=[
        ("Quelles données nous collectons", [
            "Le compte : ton adresse email et ton mot de passe, conservé chiffré (hash). Si tu te connectes avec Google, nous recevons de Google ton nom, ton adresse email et ta photo de profil au lieu d’un mot de passe.",
            "Les préférences que tu saisis : la langue de l’application, le nombre de personnes, le budget, le nombre de jours où tu cuisines, les catégories préférées, les restrictions alimentaires et les aliments exclus, les appareils de cuisine et les objectifs nutritionnels. Si tu utilises le calculateur de calories, également l’âge, le sexe, la taille, le poids, le niveau d’activité et l’objectif.",
            "Ce que tu crées dans l’application : les plannings de la semaine et leur historique, les recettes favorites, la liste de courses (ce que tu as coché et ce que tu as déjà) et les avis que tu écris.",
            "Si tu t’abonnes : l’état de l’abonnement, fourni par Google Play. Nous ne voyons jamais les données de ta carte.",
            "Nous n’utilisons pas la localisation du téléphone et nous ne vendons les données à personne.",
        ]),
        ("Les avis sont publics", [
            "Si tu écris un avis, ta note, ton commentaire, le nom d’affichage que tu as choisi et la date sont visibles par les autres utilisateurs de Plate. Ton adresse email n’est jamais affichée.",
            "Si quelqu’un signale un avis, l’administrateur peut voir l’avis signalé et le supprimer. Tu peux supprimer ton avis à tout moment, et tes avis disparaissent quand tu supprimes ton compte.",
        ]),
        ("Publicités (version gratuite uniquement)", [
            "La version gratuite affiche des publicités via Google AdMob : une bannière en bas de certaines pages et, au plus une fois par jour, une publicité plein écran quand tu termines une recette en mode cuisine. Avec Premium (y compris le mois de bienvenue), tu ne vois pas de publicités.",
            "À la première ouverture après la configuration initiale, nous te demandons ton consentement via un formulaire Google. Tu peux choisir des publicités personnalisées ou non et modifier ton choix à tout moment dans Réglages → choix concernant les publicités.",
            "Pour afficher et mesurer les publicités, Google et ses partenaires peuvent utiliser l’identifiant publicitaire du téléphone, l’adresse IP (dont on peut déduire une localisation approximative) et des informations sur l’appareil et sur l’interaction avec les publicités. Nous ne leur envoyons pas tes plannings, tes préférences ni d’autres données de ton compte. Détails : policies.google.com/technologies/ads.",
        ]),
        ("Pourquoi", ["Pour faire fonctionner l’application : te connecter, générer ton planning, enregistrer tes données, les synchroniser entre tes téléphones et t’envoyer les emails avec les codes dans ta langue."]),
        ("Où elles sont conservées", [
            "Sur ton téléphone et dans ton compte, sur les serveurs Supabase de l’Union européenne (Francfort, Allemagne). Les données circulent par des connexions chiffrées, et chaque compte ne peut lire que ses propres données (sauf les avis, qui sont publics).",
            "Prestataires : Supabase (base de données et authentification), Google (connexion avec Google), Brevo (envoi des emails avec les codes de vérification), Google AdMob (publicités de la version gratuite) et, si tu t’abonnes, Google Play et RevenueCat (l’abonnement).",
        ]),
        ("Autorisations sur le téléphone", ["Internet (synchronisation et publicités), vibreur (minuteur du mode cuisine) et identifiant publicitaire (publicités de la version gratuite ; tu peux le réinitialiser ou le supprimer dans les réglages du téléphone). L’application ne demande pas l’accès à la localisation, à l’appareil photo, au micro ni aux contacts."]),
        ("Tes droits (RGPD)", [
            "Tu peux voir et corriger tes données directement dans l’application, télécharger une copie de tes données personnelles au format CSV (Réglages → Exporter les données) et supprimer définitivement ton compte et toutes ses données (Réglages → Supprimer le compte).",
            "Pour toute autre demande, écris à {C}. Tu peux aussi déposer une plainte auprès de l’autorité de protection des données de ton pays ; en France, la CNIL.",
        ]),
        ("Combien de temps nous les gardons", ["Tant que le compte existe. La suppression du compte efface les données des serveurs."]),
        ("Âge", ["Plate n’est pas destiné aux enfants de moins de 16 ans."]),
    ],
    sterg_titlu="Supprimer le compte – Plate", sterg_desc="Comment supprimer ton compte et tes données Plate.",
    sterg_h1="Supprime ton compte Plate", sterg_lead="Tu peux supprimer définitivement ton compte et toutes ses données à tout moment.",
    sterg_app="Dans l’application",
    sterg_pasi=["Ouvre Plate et va dans <b>Réglages → Supprimer le compte</b>.", "Tape <b>SUPPRIMER</b> dans le champ de confirmation et appuie sur <b>Supprimer le compte</b>."],
    sterg_export="Facultatif : avant la suppression, tu peux garder une copie de tes données (CSV) depuis <b>Réglages → Exporter les données</b>.",
    sterg_email_h="Par email",
    sterg_email="Si tu ne peux plus ouvrir l’application, écris à {L} depuis l’adresse email de ton compte et demande la suppression. Nous la faisons sous 30 jours maximum.",
    sterg_subiect="Supprimer mon compte Plate",
    sterg_ce_h="Ce qui est supprimé",
    sterg_ce="Le compte, les préférences, les plannings, les favoris, la liste de courses et les avis sont définitivement supprimés des serveurs. Nous ne gardons rien. Un abonnement Google Play doit être annulé séparément, dans Google Play.",
)

T["de"] = dict(
    actualizat="November 2026",
    nav=("Datenschutz", "Nutzungsbedingungen", "Konto löschen"),
    footer=("Datenschutzerklärung", "Nutzungsbedingungen", "Konto löschen"),
    index_titlu="Plate – dein Wochenplan für Mahlzeiten",
    index_desc="Plate erstellt deinen Essensplan für die Woche, passend zu Budget, Kalorien und Küchengeräten.",
    index_h1="Was kochen wir diese Woche?<br>Plate sagt es dir.",
    index_lead="Plate plant deine Mahlzeiten für 7 Tage (Frühstück, Mittagessen, Abendessen und Snacks) nach deinem Budget, deinen Kalorien und deinen Geräten und gibt dir die fertige Einkaufsliste.",
    carduri=[
        ("7-Tage-Plan", "Die Mahlzeiten, die du wählst, im Rahmen deines Budgets und Kalorienlimits."),
        ("800 Rezepte", "Schritt für Schritt, mit Timern, für Airfryer, Backofen, Herd, Mikrowelle oder Slow Cooker."),
        ("Einkaufsliste", "Mengen nach Abteilungen zusammengefasst, ohne das, was du schon zu Hause hast."),
        ("5 Sprachen", "Deutsch, Englisch, Spanisch, Französisch und Rumänisch, mit Preisen in deiner Währung."),
    ],
    index_note=[
        "Plate ist kostenlos, mit Werbung. Neue Konten erhalten einen Monat Premium gratis: keine Werbung, unbegrenzte Neuerstellungen, erweiterte Ernährung und Favoriten.",
        "Fragen? Schreib uns an {C}.",
    ],
    conf_titlu="Datenschutzerklärung – Plate", conf_h1="Datenschutzerklärung", conf_desc="Welche Daten Plate erhebt, warum und wie sie geschützt werden.",
    term_titlu="Nutzungsbedingungen – Plate", term_h1="Nutzungsbedingungen", term_desc="Die Nutzungsbedingungen der App Plate.",
    ultima="Zuletzt aktualisiert",
    termeni=[
        ("Wer wir sind", ["Plate ist eine App zur Essensplanung, entwickelt von einem unabhängigen Entwickler aus Rumänien. Kontakt: {C}."]),
        ("Dein Konto", [
            "Du brauchst ein Konto, um Plate zu nutzen. Du kannst es mit deiner E-Mail-Adresse und einem Passwort (bestätigt mit einem per E-Mail gesendeten Code) oder mit deinem Google-Konto erstellen. Behalte dein Passwort für dich; du bist für alles verantwortlich, was in deinem Konto passiert.",
            "Du kannst dein Konto jederzeit in der App löschen: Einstellungen → Konto löschen.",
        ]),
        ("Was die App bietet", [
            "Plate schlägt dir die Mahlzeiten für eine Woche vor (Frühstück, Mittagessen, Abendessen und Snacks, wie du möchtest), passend zu Budget, Kalorien, Geschmack und Geräten, mit Schritt-für-Schritt-Rezepten und Einkaufsliste.",
            "Die angezeigten Kosten sind grobe Schätzungen, berechnet aus durchschnittlichen Referenzpreisen im gewählten Land. Die tatsächlichen Preise im Geschäft können niedriger oder höher sein.",
            "Die Rezepte sind auf Rumänisch geschrieben und in die anderen Sprachen übersetzt. Wenn dir eine Übersetzung unklar erscheint: Mengen, Temperaturen und Zeiten sind dieselben wie im Original.",
        ]),
        ("Kostenlose Version und Premium", [
            "Plate ist kostenlos: der 7-Tage-Plan (mit einer Neuerstellung pro Woche), alle Rezepte, der Kochmodus, die Einkaufsliste und das Konto mit Synchronisierung. Die kostenlose Version zeigt Werbung. Plate Premium ist ein optionales, werbefreies Abo, das unbegrenzte Neuerstellungen und Alternativen für Mahlzeiten, erweiterte Ernährung (High Protein, Eiweiß und Kohlenhydrate pro Tag, Bedarfsrechner) und Lieblingsrezepte hinzufügt.",
            "Jedes neue Konto erhält Premium in den ersten 30 Tagen kostenlos. Du brauchst keine Karte und es wird nichts berechnet; danach läuft die App als kostenlose Version weiter. Der Abopreis und eine eventuelle Testphase werden vor dem Abschluss in Google Play in deiner Währung angezeigt. Das Abo verlängert sich automatisch, bis du es kündigst.",
            "Zahlungen, Verlängerungen und Erstattungen werden von Google Play abgewickelt. Um die nächste Zahlung zu vermeiden, kündige mindestens 24 Stunden vor Ende des Zeitraums: Google Play → Zahlungen und Abos → Abos.",
        ]),
        ("Bewertungen", [
            "Du kannst ein Rezept mit 1 bis 5 Sternen bewerten und einen kurzen Kommentar schreiben. Deine Bewertung ist für alle Nutzer sichtbar, mit dem Anzeigenamen, den du wählst.",
            "Schreib nur über das Rezept. Veröffentliche keine personenbezogenen Daten, keine Werbung, keine Beleidigungen und keine rechtswidrigen Inhalte. Jeder kann eine Bewertung melden, und Bewertungen, die gegen diese Regeln verstoßen, können ohne Vorwarnung gelöscht werden. Du kannst deine eigene Bewertung jederzeit ändern oder löschen.",
        ]),
        ("Gesundheit", ["Die Nährwerte werden aus den Zutaten berechnet und sind Richtwerte. Plate gibt keine medizinischen Ratschläge. Wenn du eine Erkrankung, Allergien oder eine ärztlich verordnete Diät hast, prüfe die Rezepte und Zutaten vor dem Kochen."]),
        ("Faire Nutzung", ["Missbrauche den Dienst nicht: keine Versuche, auf Daten anderer zuzugreifen, die Server zu überlasten oder das Abo zu umgehen."]),
        ("Haftung", ["Die App wird „wie besehen“ angeboten. Soweit gesetzlich zulässig, haften wir nicht für Datenverluste oder für das Ergebnis der Rezepte. Deine Daten werden in deinem Konto gespeichert; du kannst jederzeit eine Kopie deiner personenbezogenen Daten herunterladen (Einstellungen → Daten exportieren)."]),
        ("Änderungen", ["Wir können diese Bedingungen aktualisieren. Wichtige Änderungen werden in der App angekündigt. Maßgeblich ist die rumänische Fassung."]),
    ],
    confidentialitate=[
        ("Welche Daten wir erheben", [
            "Das Konto: deine E-Mail-Adresse und dein Passwort, verschlüsselt gespeichert (Hash). Wenn du dich mit Google anmeldest, erhalten wir von Google statt eines Passworts deinen Namen, deine E-Mail-Adresse und dein Profilbild.",
            "Die Einstellungen, die du eingibst: Sprache der App, Anzahl der Personen, Budget, an wie vielen Tagen du kochst, bevorzugte Kategorien, Ernährungseinschränkungen und ausgeschlossene Lebensmittel, Küchengeräte und Ernährungsziele. Wenn du den Kalorienrechner nutzt, außerdem Alter, Geschlecht, Größe, Gewicht, Aktivitätslevel und Ziel.",
            "Was du in der App erstellst: die Wochenpläne und ihren Verlauf, Lieblingsrezepte, die Einkaufsliste (was du abgehakt hast und was du schon hast) und die Bewertungen, die du schreibst.",
            "Wenn du ein Abo abschließt: den Abostatus, von Google Play. Deine Kartendaten sehen wir nie.",
            "Wir nutzen nicht den Standort deines Telefons und verkaufen keine Daten an Dritte.",
        ]),
        ("Bewertungen sind öffentlich", [
            "Wenn du eine Bewertung schreibst, sind deine Sterne, dein Kommentar, dein gewählter Anzeigename und das Datum für andere Plate-Nutzer sichtbar. Deine E-Mail-Adresse wird nie angezeigt.",
            "Wenn jemand eine Bewertung meldet, kann der Administrator die gemeldete Bewertung sehen und löschen. Du kannst deine Bewertung jederzeit löschen, und beim Löschen deines Kontos werden auch deine Bewertungen entfernt.",
        ]),
        ("Werbung (nur in der kostenlosen Version)", [
            "Die kostenlose Version zeigt Werbung über Google AdMob: ein Banner am Ende einiger Seiten und höchstens einmal am Tag eine Vollbildanzeige, nachdem du ein Rezept im Kochmodus beendet hast. Mit Premium (auch im Willkommensmonat) siehst du keine Werbung.",
            "Beim ersten Start nach der Einrichtung bitten wir dich über ein Google-Formular um deine Einwilligung. Du kannst personalisierte oder nicht personalisierte Werbung wählen und deine Wahl jederzeit unter Einstellungen → Werbeoptionen ändern.",
            "Um Werbung anzuzeigen und zu messen, können Google und seine Partner die Werbe-ID deines Telefons, deine IP-Adresse (aus der sich ein ungefährer Standort ableiten lässt) sowie Informationen über dein Gerät und deine Interaktion mit der Werbung verwenden. Wir senden ihnen weder deine Pläne noch deine Einstellungen oder andere Daten aus deinem Konto. Details: policies.google.com/technologies/ads.",
        ]),
        ("Wozu", ["Damit die App funktioniert: um dich anzumelden, deinen Plan zu erstellen, deine Daten zu speichern, sie zwischen deinen Telefonen zu synchronisieren und dir die E-Mails mit Codes in deiner Sprache zu senden."]),
        ("Wo sie gespeichert werden", [
            "Auf deinem Telefon und in deinem Konto, auf Supabase-Servern in der Europäischen Union (Frankfurt, Deutschland). Die Daten werden verschlüsselt übertragen, und jedes Konto kann nur seine eigenen Daten lesen (außer den Bewertungen, die öffentlich sind).",
            "Dienstleister: Supabase (Datenbank und Authentifizierung), Google (Anmeldung mit Google), Brevo (Versand der E-Mails mit Bestätigungscodes), Google AdMob (Werbung in der kostenlosen Version) und, wenn du ein Abo abschließt, Google Play und RevenueCat (das Abo).",
        ]),
        ("Berechtigungen auf dem Telefon", ["Internet (Synchronisierung und Werbung), Vibration (der Timer im Kochmodus) und die Werbe-ID (Werbung in der kostenlosen Version; du kannst sie in den Einstellungen deines Telefons zurücksetzen oder löschen). Die App fragt nicht nach Zugriff auf Standort, Kamera, Mikrofon oder Kontakte."]),
        ("Deine Rechte (DSGVO)", [
            "Du kannst deine Daten direkt in der App ansehen und korrigieren, eine Kopie deiner personenbezogenen Daten im CSV-Format herunterladen (Einstellungen → Daten exportieren) und dein Konto mit allen Daten endgültig löschen (Einstellungen → Konto löschen).",
            "Für alle anderen Anfragen schreib an {C}. Du kannst dich auch bei der Datenschutzaufsichtsbehörde deines Landes beschweren; in Deutschland ist das die Datenschutzbehörde deines Bundeslandes.",
        ]),
        ("Wie lange wir sie speichern", ["Solange das Konto besteht. Mit dem Löschen des Kontos werden die Daten von den Servern entfernt."]),
        ("Alter", ["Plate richtet sich nicht an Kinder unter 16 Jahren."]),
    ],
    sterg_titlu="Konto löschen – Plate", sterg_desc="So löschst du dein Plate-Konto und deine Daten.",
    sterg_h1="Lösche dein Plate-Konto", sterg_lead="Du kannst dein Konto und alle seine Daten jederzeit endgültig löschen.",
    sterg_app="In der App",
    sterg_pasi=["Öffne Plate und geh zu <b>Einstellungen → Konto löschen</b>.", "Gib <b>LOSCHEN</b> in das Bestätigungsfeld ein und tippe auf <b>Konto löschen</b>."],
    sterg_export="Optional: Vor dem Löschen kannst du unter <b>Einstellungen → Daten exportieren</b> eine Kopie deiner Daten (CSV) behalten.",
    sterg_email_h="Per E-Mail",
    sterg_email="Wenn du die App nicht mehr öffnen kannst, schreib an {L} von der E-Mail-Adresse deines Kontos und bitte um die Löschung. Wir erledigen das innerhalb von 30 Tagen.",
    sterg_subiect="Mein Plate-Konto löschen",
    sterg_ce_h="Was gelöscht wird",
    sterg_ce="Konto, Einstellungen, Pläne, Favoriten, Einkaufsliste und Bewertungen werden endgültig von den Servern entfernt. Wir behalten nichts. Ein Google-Play-Abo musst du separat in Google Play kündigen.",
)


# ---------------------------------------------------------------------------------------------

def esc(s):
    return html.escape(s, quote=False)


def cu_contact(s):
    return esc(s).replace("{C}", f'<a href="mailto:{CONTACT}">{CONTACT}</a>')


def pagina(limba, fisier, titlu, corp, descriere):
    t = T[limba]
    pre = "" if limba == "ro" else "../"
    baza = "" if limba == "ro" else f"{limba}/"
    limbi = " ".join(
        f"<b>{nume}</b>" if l == limba else f'<a href="{pre}{"" if l == "ro" else l + "/"}{fisier}" hreflang="{l}">{nume}</a>'
        for l, nume in LIMBI
    )
    alternate = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{pre}{"" if l == "ro" else l + "/"}{fisier}">' for l, _ in LIMBI
    )
    doc = f"""<!doctype html>
<html lang="{limba}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(titlu)}</title>
<meta name="description" content="{html.escape(descriere)}">
{alternate}
<link rel="icon" href="{pre}favicon.png">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header>
  <a class="brand" href="./"><img src="{pre}logo.png" alt="">PLATE</a>
  <nav><a href="confidentialitate.html">{esc(t["nav"][0])}</a><a href="termeni.html">{esc(t["nav"][1])}</a><a href="stergere-cont.html">{esc(t["nav"][2])}</a></nav>
</header>
<div class="limbi">{limbi}</div>
{corp}
<footer><span>© 2026 Plate</span><a href="confidentialitate.html">{esc(t["footer"][0])}</a><a href="termeni.html">{esc(t["footer"][1])}</a><a href="stergere-cont.html">{esc(t["footer"][2])}</a><a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</div>
</body>
</html>
"""
    dest = OUT / baza / fisier
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(doc, encoding="utf-8", newline="\n")


def sectiuni(items):
    out = []
    for h, ps in items:
        out.append(f"<h2>{esc(h)}</h2>")
        out.extend(f"<p>{cu_contact(p)}</p>" for p in ps)
    return "\n".join(out)


for limba, t in T.items():
    carduri = "\n".join(f'  <div class="card"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in t["carduri"])
    note = "\n".join(f'<p class="muted">{cu_contact(n)}</p>' for n in t["index_note"])
    pagina(limba, "index.html", t["index_titlu"],
           f'<h1>{t["index_h1"]}</h1>\n<p class="lead">{esc(t["index_lead"])}</p>\n<div class="grid">\n{carduri}\n</div>\n{note}',
           t["index_desc"])
    pagina(limba, "confidentialitate.html", t["conf_titlu"],
           f'<h1>{esc(t["conf_h1"])}</h1><p class="muted">{esc(t["ultima"])}: {esc(t["actualizat"])}</p>\n' + sectiuni(t["confidentialitate"]),
           t["conf_desc"])
    pagina(limba, "termeni.html", t["term_titlu"],
           f'<h1>{esc(t["term_h1"])}</h1><p class="muted">{esc(t["ultima"])}: {esc(t["actualizat"])}</p>\n' + sectiuni(t["termeni"]),
           t["term_desc"])
    link = f'<a href="mailto:{CONTACT}?subject={html.escape(t["sterg_subiect"]).replace(" ", "%20")}">{CONTACT}</a>'
    pasi = "\n".join(f"  <li>{p}</li>" for p in t["sterg_pasi"])
    pagina(limba, "stergere-cont.html", t["sterg_titlu"],
           f"""<h1>{esc(t["sterg_h1"])}</h1>
<p class="lead">{esc(t["sterg_lead"])}</p>
<h2>{esc(t["sterg_app"])}</h2>
<ol>
{pasi}
</ol>
<p>{t["sterg_export"]}</p>
<h2>{esc(t["sterg_email_h"])}</h2>
<p>{esc(t["sterg_email"]).replace("{L}", link)}</p>
<h2>{esc(t["sterg_ce_h"])}</h2>
<p>{esc(t["sterg_ce"])}</p>""",
           t["sterg_desc"])
print("gata:", ", ".join(T))
