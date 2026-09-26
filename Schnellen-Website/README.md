# Schnellen – Website

Eine fertige, responsive Landingpage mit Original-App-Icon und App-Store-Screenshots. Reines HTML und CSS, kein JavaScript, kein Tracking, keine externen Schriftarten und keine kostenpflichtigen Abhängigkeiten.

## Vorschau

`index.html` im Browser öffnen. Alternativ im Ordner `python3 -m http.server 8000` starten und http://localhost:8000 öffnen.

## Kostenlos auf GitHub Pages veröffentlichen (empfohlen)

1. Auf GitHub ein **öffentliches** Repository anlegen, etwa `schnellen`. GitHub Free unterstützt Pages für öffentliche Repositories.
2. Den **gesamten Inhalt dieses Ordners** in den Hauptordner des Repositorys auf dem Branch `main` übernehmen, einschließlich `.github/workflows/pages.yml` und `.nojekyll`. Nicht das ZIP selbst hochladen. Beim Hochladen im Browser auf die versteckten Dateien achten; am einfachsten den entpackten Ordner mit GitHub Desktop übernehmen.
3. Im Repository **Settings → Pages → Build and deployment → Source → GitHub Actions** wählen.
4. Unter **Actions → Publish Schnellen website → Run workflow** starten. Spätere Änderungen an `main` veröffentlichen sich automatisch.
5. Nach erfolgreichem Durchlauf steht der fertige Link unter **Settings → Pages**. **Enforce HTTPS** aktivieren, sofern auswählbar.

Die Veröffentlichung trägt die tatsächliche Adresse automatisch in Canonical-Tags, Open-Graph-URL, `sitemap.xml` und `robots.txt` ein. Sie funktioniert auch unter einem Repository-Unterpfad. Du brauchst keine eigene Domain. Eine bereits vorhandene GitHub-Pages-Seite in einem anderen Repository bleibt unberührt.

## Alternative: direkt von einem Branch

Führe einmal `python3 tools/prepare-site.py https://DEIN-KONTO.github.io/DEIN-REPOSITORY/` mit deiner echten Adresse aus. Lade die Dateien einschließlich der dadurch erzeugten `sitemap.xml` und `robots.txt` hoch. Wähle unter Pages **Deploy from a branch → main → /(root)**. Den mitgelieferten Actions-Workflow bei dieser Variante nicht übernehmen. Bei einer anderen Adresse das Skript erneut ausführen.

## Inhalte und Quellen

- App: https://apps.apple.com/at/app/schnellen/id6793147112
- App-Metadaten: https://itunes.apple.com/lookup?id=6793147112&country=at
- Bestehender App-Datenschutz und Support: https://jillri.github.io/Schnellen-privacy/
- Allgemeiner Hintergrund zum traditionellen Spiel: https://de.wikipedia.org/wiki/Schnellen_(Kartenspiel)
- Kostenloses Hosting und IP-Protokollierung: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- GitHub-Datenschutz: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

Stand: 26. September 2026. App-Angaben basieren auf Version 1.2. Screenshots stammen aus dem öffentlichen Store-Eintrag; einzelne Ansichten zeigen ältere Versionsnummern. Originale lokal gespeichert, keine Bildanfragen an Apple beim Seitenbesuch. Die Verwendung erfolgt für die Website der App-Inhaberin; keine separate Lizenz für Weiterverwendung in anderen Projekten.

## Pflege

Texte: `index.html`; Farben/Layout: `styles.css`; Website-Datenschutz: `datenschutz.html`; Bilder: `assets/`. Die Website ist vollständig ohne JavaScript nutzbar. FAQs nutzen native aufklappbare Elemente; Screenshots öffnen als große Bilddatei. Auf kleinen Bildschirmen lässt sich die Screenshot-Reihe seitlich scrollen.

Die Support-Adresse `jillappcontact@gmail.com` und der Name Jill Marie Grontzki stammen aus den öffentlichen App-Angaben. Es wurde keine Anschrift erfunden. Die Website-Datenschutzseite beschreibt die technische Umsetzung und verlinkt den bestehenden App-Datenschutz; sie ist keine individuell juristisch geprüfte Erklärung. Etwaige zusätzliche Betreiber-/Impressumsangaben und die abschließende Datenschutzerklärung sind vor dem öffentlichen Einsatz durch die Betreiberin zu prüfen und bei Bedarf zu ergänzen.

## SEO

Deutscher Seitentitel und Beschreibung, eine H1, semantische Überschriften, Alt-Texte, mobile Darstellung, MobileApplication-Strukturdaten, Open-Graph-Titel und Beschreibung. Canonical-URL und Sitemap entstehen bei der Veröffentlichung. Keine erfundenen Bewertungen. Nach dem Veröffentlichen kann die finale Sitemap in der Google Search Console eingereicht werden. Indexierung und Ranking liegen bei Google und sind nicht garantiert.

Bei Projektseiten wirkt eine `robots.txt` unter dem Repository-Unterpfad nicht als domainweite Richtlinie: Suchmaschinen lesen sie nur im Domain-Hauptverzeichnis. Die Seite ist auch ohne diese Datei crawlbar. Die Sitemap direkt in der Search Console einreichen; bei Bedarf einen Sitemap-Verweis in der Domain-Root-robots.txt ergänzen.
