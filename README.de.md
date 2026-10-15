# Agentic Coding Starter Kit

**Version 0.1.0** · 🇬🇧 **English version: [README.md](README.md)**

Minimale, mitwachsende Basis für agentische Entwicklung (Claude Code, Codex, GitHub Copilot) mit Git und [Backlog.md](https://github.com/MrLesk/Backlog.md) – token-sparsam und nachvollziehbar.

## Nutzung

**Standardweg (kein technisches Wissen nötig):** [ZIP herunterladen](https://github.com/Akku/agentic-coding-starter-kit/archive/refs/heads/main.zip), entpacken, den Ordner im Agenten öffnen und den Prompt aus [STARTE_HIER.md](STARTE_HIER.md) geben. Der Agent installiert fehlende Werkzeuge gemeinsam mit dir, richtet Git und Backlog.md ein, passt das Harness an dein Ziel an und legt die ersten Tasks an.

**Technisch Versierte:** auf GitHub **Use this template** wählen oder das Repository klonen, dann derselbe Prompt.

Pro Sitzung führt der Agent `scripts/session-start.sh` aus (kurzer Zustandsüberblick).

## Start-Prompt

Gib dies dem Agenten, nachdem du den Ordner geöffnet hast:

> Richte dieses Projekt mit dem Skill `project-setup` ein (`.claude/skills/project-setup/SKILL.md`). Arbeite in meiner Sprache und führe mich Schritt für Schritt durch die Installation von allem, was fehlt. Was ich entwickeln will, ist folgendes: *<deine Idee: was, für wen, woran erkennt man „fertig“ – ein paar Sätze>*

## Inhalt

| Datei | Zweck |
| --- | --- |
| `STARTE_HIER.md` / `START_HERE.md` | Anleitung für Menschen (DE/EN) |
| `.claude/skills/` | Skills: `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices` |
| `.claude/agents/` | Agenten: `ux-designer` (für Projekte mit Oberfläche) |
| `AGENTS.md` | Gemeinsame Kernregeln (Codex & kompatible Tools) |
| `CLAUDE.md` / `.github/copilot-instructions.md` | Dünne Adapter, verweisen auf `AGENTS.md` |
| `scripts/run.sh` | Kompakte Ausgabe für Tests/CI/CLI (Exitcode bleibt erhalten, Volllog außerhalb des Repos) |
| `scripts/session-start.sh` | Lesender Sitzungsstart (Branch, Änderungen, Tasks, Übergabe) |
| `docs/agent/OPERATING_MODEL.md` | Regeln mit stabilen IDs (`R-*`), gezielt per ID geladen |
| `docs/agent/ADVANCED.md` | Selten gebrauchte Regeln (Parallelität, Messung, Routing, lokale Modelle) |
| `docs/agent/LEARNINGS.md` | Beobachtungen für die Retro (enthält Startpunkte für die erste Retro) |
| `docs/agent/PITFALLS.md` | Wachsende Liste technischer Stolperfallen |
| `docs/agent/PROCESS_IMPROVEMENTS.md` | Retro-Behandlung und Rückfluss ins Kit |

## Prinzipien

- Informationsarchitektur statt „kürzer antworten": kurze Einstiege, Vertiefung nach Bedarf, Volllogs außerhalb des Kontexts.
- Eine verbindliche Quelle je Regel; Adapter verweisen nur.
- Das Harness wächst durch Retros, nicht durch Vorrat (`R-DECISION`).

## Beitragen

Bewährte Learnings aus Projekten bitte per Pull Request einbringen (Muster: Problem, Muster, Geltungsbereich, Evidenz – siehe `docs/agent/PROCESS_IMPROVEMENTS.md`). Keine Projekt- oder Firmeninterna, keine Zugangsdaten – das Repository ist öffentlich.
