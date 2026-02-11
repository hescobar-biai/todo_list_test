"""
IDK: task-entity, domain-entity, aggregate-root

Module: entities

Responsibility:
- Define Task domain entity
- Enforce task-specific business rules
- Manage task lifecycle and state transitions

Key Components:
- Task: Domain entity inheriting from Entity with task-specific defaults

Invariants:
- All tasks have auto-generated TASK-{uuid} code
- All tasks default to "pending" status
- Tasks follow entity lifecycle: inactive -> active -> deleted

Related Docs:
- docs/tasks/domain/task-entity.md
"""

from uuid import uuid4

from pydantic import ConfigDict, Field

from src.shared.domain.base_entity import Entity


class Task(Entity):
    """
    IDK: task-entity, domain-entity, lifecycle

    Responsibility:
    - Represent a task/todo item in the domain
    - Provide task-specific defaults for code and status
    - Enable task lifecycle management

    Invariants:
    - code auto-generates as TASK-{8-char-uuid}
    - status defaults to "pending"
    - Inherits all Entity fields and methods

    Collaborators:
    - Entity: base class providing identity and lifecycle
    - Pydantic: validation and serialization

    Related Docs:
    - docs/tasks/domain/task-entity.md
    """

    model_config = ConfigDict(
        extra='forbid',
        validate_assignment=True,
        use_enum_values=True,
    )

    code: str = Field(
        default_factory=lambda: f"TASK-{str(uuid4())[:8]}",
        min_length=1,
        max_length=100,
        description="Auto-generated task code (TASK-{uuid})",
    )

    status: str | None = Field(
        default="pending",
        max_length=50,
        description="Task status (pending, in_progress, completed, etc)",
    )
