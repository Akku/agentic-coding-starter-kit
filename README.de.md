# Agentic Coding Starter Kit

*English: [README.md](README.md)*

Minimale, mitwachsende Basis für agentische Entwicklung (Claude Code, Codex, GitHub Copilot) mit Git und [Backlog.md](https://github.com/MrLesk/Backlog.md) – token-sparsam und nachvollziehbar.

## Nutzung

1. Auf GitHub **„Use this template"** wählen (oder den Ordner kopieren) und das neue Projekt lokal öffnen.
2. Dem Agenten den Ordner freigeben und sagen: *„Folge START_HERE.md. Mein Projektziel: …"*
3. Der Agent prüft Voraussetzungen, richtet Git und Backlog.md ein, passt das Harness an dein Ziel an und legt die ersten Tasks an. Danach beginnt die Entwicklung.

Pro Sitzung führt der Agent `scripts/session-start.sh` aus (kurzer Zustandsüberblick).

## Inhalt

| Datei | Zweck |
| --- | --- |
| `STARTE_HIER.md` / `START_HERE.md` | Anleitung für Menschen (DE/EN) |
| `.claude/skills/` | Skills: `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices` |
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
