# Todo List Application

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](https://docs.pytest.org/)

A Domain-Driven Design (DDD) based task management system built with Python 3.12+ and modern tooling.

## Overview

This Todo List application demonstrates clean architecture principles with a focus on:

- **Domain-Driven Design (DDD)**: Clear separation of domain logic from infrastructure
- **Entity Pattern**: Base entity with audit trails, versioning, and state management
- **Type Safety**: Full Pydantic validation and type hints
- **Modern Python**: Python 3.12+ with latest language features

## Features

- **Task Management**: Create, update, and manage tasks with auto-generated codes
- **Entity Lifecycle**: Soft delete, activation, and deactivation patterns
- **Audit Trail**: Complete creation and modification tracking
- **State Management**: INACTIVE (0), ACTIVE (1), DELETED (2) states
- **Multi-tenancy Ready**: Organization and project scoping support

## Tech Stack

- **Python**: 3.12+
- **Package Manager**: [uv](https://docs.astral.sh/uv/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Testing**: [pytest](https://docs.pytest.org/)
- **Linting**: [ruff](https://docs.astral.sh/ruff/)

## Installation

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd todo_list
```

2. Create virtual environment and install dependencies:

```bash
uv sync
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

## Project Structure

```
todo_list/
├── src/
│   ├── app/              # Application layer
│   │   ├── __init__.py
│   │   └── __main__.py   # CLI entry point
│   ├── shared/           # Shared kernel
│   │   └── domain/
│   │       └── base_entity.py   # Base entity with audit trail
│   └── tasks/            # Task domain
│       └── domain/
│           └── entities.py      # Task entity
├── tests/                # Test suite
├── specs/                # Feature specifications
├── pyproject.toml        # Project configuration
└── README.md            # This file
```

## Usage

### Running the Application

```bash
# Run the CLI
uv run python -m app --version

# Or with activated environment
python -m app --version
```

### Creating a Task

```python
from src.tasks.domain.entities import Task

# Create a new task
task = Task(name="Complete documentation", description="Write README.md file")
print(task.code)  # TASK-a1b2c3d4
print(task.status)  # pending
```

### Entity Lifecycle

```python
# Activate a task
task.activate(user_id="user-123")

# Deactivate a task
task.deactivate(user_id="user-123")

# Soft delete a task
task.delete(user_id="user-123")

# Check state
if task.is_active():
    print("Task is active")
```

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run specific test file
uv run pytest tests/test_entities.py
```

### Linting and Formatting

```bash
# Check code style
uv run ruff check .

# Auto-fix issues
uv run ruff check . --fix

# Format code
uv run ruff format .
```

### Type Checking

```bash
# Run mypy (if configured)
uv run mypy src
```

## Architecture

### Base Entity

All domain entities inherit from `Entity` which provides:

- **Identity**: UUID v4 unique identifier
- **Business Code**: Human-readable reference
- **Audit Trail**: `created_at`, `created_by`, `updated_at`, `updated_by`
- **Versioning**: Optimistic locking support
- **State Management**: Lifecycle state transitions
- **Multi-tenancy**: `organization_id`, `project_id`, `owner`

### Entity States

| State | Value | Description |
|-------|-------|-------------|
| INACTIVE | 0 | Deactivated but recoverable |
| ACTIVE | 1 | Operational and visible |
| DELETED | 2 | Soft-deleted (archived) |

### Task Entity

The `Task` entity extends `Entity` with:

- Auto-generated codes: `TASK-{8-char-uuid}`
- Default status: `pending`
- Task-specific lifecycle management

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run tests: `uv run pytest`
5. Run linting: `uv run ruff check .`
6. Commit your changes: `git commit -am 'Add new feature'`
7. Push to the branch: `git push origin feature/my-feature`
8. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built with modern Python practices and clean architecture principles.
