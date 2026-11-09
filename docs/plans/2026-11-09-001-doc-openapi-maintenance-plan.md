# Slice: Add OpenAPI Spec Maintenance Documentation

slice_id: doc-openapi-maintenance
title: Document OpenAPI spec maintenance in backend/CLAUDE.md
blockers: []
verification_mode: automated
test_level: none
functional_risk: low
execution_class: small
minimum_model_tier: medium
model_requirements:
  - Must understand FastAPI response_model pattern
  - Must match existing CLAUDE.md style and tone

## Context Packet

- backend/CLAUDE.md (existing guidance file to extend)
- backend/src/api/schemas.py (response schemas added by PR #423)
- backend/tests/test_schema_alignment.py (validation tests ensuring schema-entity alignment)

## Expected Files

- backend/CLAUDE.md (modified - add new section)

## Conflict Domains

None - documentation-only change, no code conflicts expected.

## Shared Resources

None.

## Proof Check

```bash
# Verify the new section exists in CLAUDE.md
grep -A 5 "OpenAPI" backend/CLAUDE.md | head -20
```

## HITL Classification

none - mechanical documentation addition with clear acceptance criteria.

## Acceptance Criteria

1. New section added to backend/CLAUDE.md titled "API Documentation / OpenAPI Spec" or similar
2. Section explains that response schemas are defined in `backend/src/api/schemas.py`
3. Section documents the pattern: entity.to_dict() output must match corresponding Pydantic schema
4. Section mentions the validation tests in `backend/tests/test_schema_alignment.py`
5. Section includes guidance for adding new endpoints (create schema, apply response_model)
6. Style matches existing CLAUDE.md conventions (concise, imperative, no marketing words)

## Test Scenarios

None - documentation-only change verified by proof check and manual review.

## Scope Boundary

Only modify backend/CLAUDE.md. Do not touch frontend/CLAUDE.md or root CLAUDE.md for this slice. Do not modify any code files.
