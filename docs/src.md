---
doc_type: fractal
domain: src
owner: system
level: L1
tags:
  - expert:backend
  - level:L1
  - topic:api
idk:
  - domain-entity
  - base-model
  - audit-trail
  - task-entity
  - aggregate-root
children:
  - app
  - shared
  - tasks
source_readmes: []
last_reviewed: 2025-02-12
---

# src

## Overview

The `src` directory contains the main source code for the Todo List Application. It follows a modular architecture with clear separation of concerns across three primary domains: `app` (entry points and CLI), `shared` (common domain primitives), and `tasks` (task management domain).

## Folder Structure

```
src/
├── app/           # Application entry points and CLI
├── shared/        # Shared domain primitives and base entities
└── tasks/         # Task domain entity and business logic
```

## Key Components

### app/
Application entry point providing CLI interface and command-line argument parsing.

### shared/
Shared domain foundation providing base entity class with audit trails, state management, and lifecycle patterns used across all domains.

### tasks/
Task domain implementation containing the Task entity with task-specific defaults and lifecycle management.

## Dependencies

- **pydantic**: Data validation and serialization
- **uuid**: Unique identifier generation
- **datetime**: UTC timestamp handling

## Related Documentation

- [docs/src/app.md](./src/app.md)
- [docs/src/shared.md](./src/shared.md)
- [docs/src/tasks.md](./src/tasks.md)
