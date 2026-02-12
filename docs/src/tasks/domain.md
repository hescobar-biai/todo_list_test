---
doc_type: fractal
domain: tasks.domain
owner: system
level: L3
tags:
  - expert:backend
  - level:L3
  - topic:api
idk:
  - task-entity
  - domain-entity
  - aggregate-root
  - lifecycle
  - todo
children: []
source_readmes: []
last_reviewed: 2025-02-12
---

# src/tasks/domain

## Overview

The `tasks/domain` module contains the Task domain entity - the core business entity of the Todo List Application. It extends the base Entity class with task-specific defaults and behavior.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Package initialization |
| `entities.py` | Task entity definition |

## Key Components

### Task (Entity)

**IDK:** task-entity, domain-entity, lifecycle

The Task class represents a todo item in the domain.

**Responsibility:**
- Represent a task/todo item in the domain
- Provide task-specific defaults for code and status
- Enable task lifecycle management

**Invariants:**
- code auto-generates as TASK-{8-char-uuid}
- status defaults to "pending"
- Inherits all Entity fields and methods

#### Field Defaults

| Field | Default | Description |
|-------|---------|-------------|
| `code` | `TASK-{uuid[:8]}` | Auto-generated task code |
| `status` | `"pending"` | Task status |

#### Task Status Values

Common status values for tasks:
- `pending` - Task is waiting to be started
- `in_progress` - Task is currently being worked on
- `completed` - Task has been finished
- `cancelled` - Task has been cancelled
- `on_hold` - Task is temporarily suspended

## Usage Example

```python
from src.tasks.domain.entities import Task

# Create a new task
task = Task(name="Complete documentation")
print(task.code)  # TASK-a1b2c3d4
print(task.status)  # pending

# Create task with custom status
task = Task(name="Review PR", status="in_progress")

# Activate task
task.activate(user_id="user-123")

# Complete task
task.status = "completed"
task.mark_updated(user_id="user-123")

# Soft delete task
task.delete(user_id="user-123")
```

## Inheritance

```
Entity (shared/domain/base_entity.py)
  └── Task (tasks/domain/entities.py)
```

Task inherits all fields and methods from Entity:
- Identity fields (id, code, name)
- Audit trail (created_at, created_by, updated_at, updated_by)
- State management (state, status, version)
- Multi-tenancy (organization_id, project_id, owner)
- Lifecycle methods (activate, deactivate, delete, mark_updated)
- State queries (is_active, is_deleted, is_inactive)

## Dependencies

- **src.shared.domain.base_entity**: Entity base class
- **pydantic**: ConfigDict, Field
- **uuid**: UUID generation for task codes

## Related Documentation

- [docs/src/tasks.md](../tasks.md)
- [docs/src/shared/domain.md](../../shared/domain.md)
- [docs/src.md](../../../src.md)
