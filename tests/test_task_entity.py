"""
Tests for Task domain entity

Validates that Task entity properly implements domain requirements:
- Auto-generated UUID id
- Auto-generated TASK-{uuid} code
- Default status of "pending"
- Default state of 1 (ACTIVE)
- Inheritance of Entity lifecycle methods
"""

from uuid import UUID

import pytest

from src.tasks.domain.entities import Task


class TestTaskInstantiation:
    """Test Task entity can be instantiated with correct defaults"""

    def test_task_with_name_only(self):
        """Task instantiation with name only should populate defaults"""
        task = Task(name="Buy milk")
        assert task.name == "Buy milk"

    def test_auto_generated_id_uuid_format(self):
        """Task should auto-generate UUID format id"""
        task = Task(name="Buy milk")
        # Verify it's a valid UUID
        try:
            UUID(task.id)
            assert True
        except ValueError:
            pytest.fail(f"id '{task.id}' is not a valid UUID")

    def test_auto_generated_code_task_format(self):
        """Task should auto-generate code with TASK- prefix"""
        task = Task(name="Buy milk")
        assert task.code.startswith("TASK-")
        # Verify format is TASK-{8-char-uuid}
        parts = task.code.split("-")
        assert len(parts) == 2
        assert len(parts[1]) == 8

    def test_default_status_pending(self):
        """Task should default to pending status"""
        task = Task(name="Buy milk")
        assert task.status == "pending"

    def test_default_state_active(self):
        """Task should default to state=1 (ACTIVE)"""
        task = Task(name="Buy milk")
        assert task.state == 1


class TestTaskCodeUniqueness:
    """Test that Task code generation produces unique values"""

    def test_code_unique_across_instances(self):
        """Each Task instance should have a unique auto-generated code"""
        task1 = Task(name="Task 1")
        task2 = Task(name="Task 2")
        assert task1.code != task2.code


class TestTaskConfigValidation:
    """Test Task model configuration"""

    def test_forbid_extra_fields(self):
        """Task model_config should forbid extra fields"""
        with pytest.raises(ValueError):
            Task(name="Buy milk", unknown_field="value")


class TestTaskInheritance:
    """Test Task inherits Entity methods"""

    def test_has_mark_updated_method(self):
        """Task should inherit mark_updated() from Entity"""
        task = Task(name="Buy milk")
        assert hasattr(task, "mark_updated")
        assert callable(task.mark_updated)

    def test_has_activate_method(self):
        """Task should inherit activate() from Entity"""
        task = Task(name="Buy milk")
        assert hasattr(task, "activate")
        assert callable(task.activate)

    def test_has_deactivate_method(self):
        """Task should inherit deactivate() from Entity"""
        task = Task(name="Buy milk")
        assert hasattr(task, "deactivate")
        assert callable(task.deactivate)

    def test_has_delete_method(self):
        """Task should inherit delete() from Entity"""
        task = Task(name="Buy milk")
        assert hasattr(task, "delete")
        assert callable(task.delete)
