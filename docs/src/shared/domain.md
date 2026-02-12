---
doc_type: fractal
domain: shared.domain
owner: system
level: L3
tags:
  - expert:backend
  - level:L3
  - topic:db
idk:
  - domain-entity
  - base-model
  - audit-trail
  - state-machine
  - entity-lifecycle
  - soft-delete
  - optimistic-locking
  - multi-tenancy
children: []
source_readmes: []
last_reviewed: 2025-02-12
---

# src/shared/domain

## Overview

The `shared/domain` module provides the foundational domain entity class that serves as the base for all domain entities in the application. It implements common patterns including audit trails, state management, multi-tenancy, and optimistic locking.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Package initialization |
| `base_entity.py` | Base Entity class with audit, state, and lifecycle management |

## Key Components

### EntityState (Enum)

**IDK:** state-machine, entity-lifecycle, soft-delete

Defines valid entity states:
- `INACTIVE = 0` - Entity is deactivated but can be reactivated
- `ACTIVE = 1` - Entity is active and operational
- `DELETED = 2` - Entity is soft-deleted (archived)

**State Transitions:**
```
INACTIVE (0) -> ACTIVE (1) -> DELETED (2)
```

### Entity (BaseModel)

**IDK:** domain-entity, aggregate-root, audit-trail

Base class for all domain entities providing:

#### Core Identity Fields
| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Unique identifier (UUID v4) |
| `code` | str | Business code/reference (1-100 chars) |
| `name` | str | Human-readable name (1-255 chars) |

#### Business Metadata
| Field | Type | Description |
|-------|------|-------------|
| `description` | str \| None | Detailed description (max 1000 chars) |
| `type` | str \| None | Entity type discriminator (max 50 chars) |

#### Audit Trail - Creation
| Field | Type | Description |
|-------|------|-------------|
| `created_at` | datetime | UTC timestamp of creation |
| `created_by` | str \| None | User ID who created the entity |

#### Audit Trail - Modification
| Field | Type | Description |
|-------|------|-------------|
| `updated_at` | datetime | UTC timestamp of last update |
| `updated_by` | str \| None | User ID who last updated |
| `version` | int | Version number for optimistic locking (starts at 1) |

#### State Management
| Field | Type | Description |
|-------|------|-------------|
| `state` | int | Entity state: 0=inactive, 1=active, 2=deleted |
| `status` | str \| None | Business status (domain-specific) |

#### Multi-tenancy & Organization
| Field | Type | Description |
|-------|------|-------------|
| `organization_id` | str \| None | Organization/tenant identifier |
| `project_id` | str \| None | Project identifier |
| `owner` | str \| None | Owner user ID for access control |

## Methods

### Lifecycle Methods

#### `mark_updated(user_id: str | None = None) -> None`
Update audit trail on modification. Increments version and sets updated timestamps.

#### `deactivate(user_id: str | None = None) -> None`
Transition entity to INACTIVE state (state = 0).

#### `activate(user_id: str | None = None) -> None`
Transition entity to ACTIVE state (state = 1).

#### `delete(user_id: str | None = None) -> None`
Soft delete entity (state = 2). Data remains preserved for recovery.

### State Query Methods

#### `is_active() -> bool`
Returns True if entity state is ACTIVE (1).

#### `is_deleted() -> bool`
Returns True if entity state is DELETED (2).

#### `is_inactive() -> bool`
Returns True if entity state is INACTIVE (0).

## Invariants

- All entities have unique id (UUID v4)
- All entities track creation and modification metadata
- State transitions follow 0 (inactive) -> 1 (active) -> 2 (deleted)
- code is required and serves as business identifier
- created_at/updated_at always set to UTC
- version increments on each update

## Configuration

```python
model_config = ConfigDict(
    extra='forbid',           # Prevent extra fields
    validate_assignment=True,  # Validate on field assignment
    use_enum_values=True,      # Use enum values in serialization
)
```

## Dependencies

- **pydantic**: BaseModel, Field, ConfigDict, field_validator
- **datetime**: UTC timezone handling
- **uuid**: UUID v4 generation
- **enum**: IntEnum for state definitions

## Related Documentation

- [docs/src/shared.md](../shared.md)
- [docs/src.md](../../src.md)
