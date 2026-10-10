# Starte hier

*English: [START_HERE.md](START_HERE.md)*

Dieses Kit ist ein Startpunkt für agentische Entwicklung mit Git und Backlog.md. Du gibst dem Agenten dein Projektziel; er richtet die Werkzeuge ein, passt die Regeln an dein Ziel an und arbeitet danach Task für Task.

## So startest du

1. Erzeuge dein Projekt aus diesem Template (GitHub: **Use this template**) oder kopiere diesen Ordner an den Zielort. Öffne ihn in deinem Agenten (Claude Code, Codex, Copilot).
2. Gib dem Agenten diesen Prompt, mit deinem Ziel:

   > Richte dieses Projekt mit dem Skill `project-setup` ein (`.claude/skills/project-setup/SKILL.md`). Projektziel: *<was, für wen, woran erkennt man „fertig“ – 3–5 Sätze>*. Arbeite in meiner Sprache.

3. Beantworte die Rückfragen (Technologie, welche Agenten du nutzt, GitHub-Repository ja/nein) und genehmige vorgeschlagene Installationen. Prüfe vorher, was installiert werden soll.
4. Am Ende fasst der Agent zusammen, was angelegt wurde und welcher Task zuerst kommt. Sag ihm, dass er starten soll.

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

## Sprache

Diese Dateien sind für Menschen (Englisch und Deutsch). Anweisungen für Agenten sind auf Englisch, aber Agenten sprechen mit dir in deiner Sprache.
