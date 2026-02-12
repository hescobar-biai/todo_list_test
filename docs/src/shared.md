---
doc_type: fractal
domain: shared
owner: system
level: L2
tags:
  - expert:backend
  - level:L2
  - topic:db
idk:
  - domain-entity
  - base-model
  - shared-kernel
  - audit-trail
children:
  - domain
source_readmes: []
last_reviewed: 2025-02-12
---

# src/shared

## Overview

The `shared` module contains common domain primitives and foundational classes used across all domains in the application. It implements the Shared Kernel pattern from Domain-Driven Design, providing reusable building blocks that maintain consistency across bounded contexts.

## Folder Structure

```
shared/
└── domain/        # Domain primitives and base entities
```

## Key Components

### domain/
Contains the foundational domain entity class with:
- Identity management (UUID v4)
- Audit trail tracking (created/updated timestamps)
- State management lifecycle
- Multi-tenancy support
- Optimistic versioning

## Design Patterns

- **Shared Kernel**: Common domain concepts shared across bounded contexts
- **Base Entity**: Template for all domain entities ensuring consistency
- **Audit Trail**: Automatic tracking of entity lifecycle events
- **State Machine**: Controlled entity state transitions

## Related Documentation

- [docs/src/shared/domain.md](./shared/domain.md)
- [docs/src.md](../src.md)
