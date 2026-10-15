# Starte hier

**Version 0.2.0** · 🇬🇧 **English version: [START_HERE.md](START_HERE.md)**

Dieses Kit ist ein Startpunkt für agentische Entwicklung mit Git und Backlog.md. Du gibst dem Agenten dein Projektziel; er installiert, was fehlt, richtet die Werkzeuge ein, passt die Regeln an dein Ziel an und arbeitet danach Task für Task. Im Standardweg ist kein technisches Wissen nötig.

## Standardweg: ZIP herunterladen

1. **Lade** das Kit **herunter**: [agentic-coding-starter-kit.zip](https://github.com/Akku/agentic-coding-starter-kit/archive/refs/heads/main.zip) (alternativ: grüner Button **Code** → **Download ZIP** auf der GitHub-Seite).
2. **Entpacke** es (macOS: Doppelklick; Windows: Rechtsklick → *Alle extrahieren*). Benenne den Ordner nach deinem Projekt um und lege ihn dort ab, wo du Projekte aufbewahrst.
3. **Öffne deinen Agenten** (z. B. die Claude-Desktop-App, Tab Code) und wähle diesen Ordner als Arbeitsordner.
4. **Gib dem Agenten diesen Prompt**, mit deinem Ziel:

   > Richte dieses Projekt mit dem Skill `project-setup` ein (`.claude/skills/project-setup/SKILL.md`). Arbeite in meiner Sprache und führe mich Schritt für Schritt durch die Installation von allem, was fehlt. Was ich entwickeln will, ist folgendes: *<deine Idee: was, für wen, woran erkennt man „fertig“ – ein paar Sätze>*

5. **Beantworte die Rückfragen** (Technologie, welche Agenten du nutzt, GitHub ja/nein). Der Agent prüft, welche Werkzeuge fehlen (Git, Node.js, Backlog.md), und führt dich Schritt für Schritt durch die Installation. Du genehmigst jede Installation. Fragt ein Installer nach deinem Computer-Passwort, gib es selbst dort ein, niemals im Chat. Unter Windows brauchen die Hilfsskripte Git für Windows (enthält *Git Bash*); der Agent führt dich dabei.
6. **Am Ende** fasst der Agent zusammen, was angelegt wurde und welcher Task zuerst kommt. Sag ihm, dass er starten soll.

## Für technisch Versierte: über GitHub

- Klicke auf der GitHub-Seite auf **Use this template** (erzeugt ein eigenes Repository), klone es, öffne es in deinem Agenten und gib den Prompt aus Schritt 4. Oder: dieses Repository mit `git clone` holen und den Ordner `.git` löschen, um mit frischer Historie zu starten.
- `git`, `node` und `backlog` schon installiert? Der Agent erkennt das und überspringt die Installationsschritte.
- Verbesserungen und bewährte Learnings sind als Pull Request willkommen (Skill `promote-learning`).

## Was du bekommst

- Git, Backlog.md und die ersten 3–7 Tasks aus deinem Ziel.
- Kurze Agentenregeln (`AGENTS.md`), die weitere Regeln nur bei Bedarf laden – das spart Tokens.
- `scripts/run.sh` hält lange Test-/CI-Ausgaben aus dem Kontext; `scripts/session-start.sh` liefert beim Sitzungsstart einen kompakten Stand.
- Skills für wiederkehrende Aufgaben: `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices`.

## Im Alltag

- Die Arbeit ist backlog-getrieben: jede Änderung ist ein Task mit Akzeptanzkriterien. Ansehen mit `backlog board` oder `backlog browser`.
- Eine Sitzung endet mit dem Skill `handoff`; die nächste beginnt mit `docs/agent/HANDOFF.md`.
- Nach dem ersten Meilenstein: Retro (Skill `retro`). Sie prüft auch das Harness selbst, inklusive der offenen Fragen in `docs/agent/LEARNINGS.md`.
- Keine Zugangsdaten ins Repository.

## Kit an einem echten Projekt testen: worauf achten

- Hat der Agent zu Beginn nur `AGENTS.md` gelesen statt alles?
- Sind `backlog/` und die ersten Tasks da, und ist `AGENTS.md` unversehrt?
- Läuft die Verifikation über `scripts/run.sh`?
- Steht `Setup status: DONE` in `AGENTS.md` und ist alles committet?
- Macht eine zweite Sitzung über `scripts/session-start.sh` ohne Nachfragen weiter?
- Stolperstellen oder Unklarheiten notieren (oder den Agenten als `Learning:` festhalten lassen). Sie sind die Eingabe für die erste Retro.

## Sprache

Diese Dateien sind für Menschen (Englisch und Deutsch). Anweisungen für Agenten sind auf Englisch, aber Agenten sprechen mit dir in deiner Sprache.
