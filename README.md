# Course App

The `course` package defines the catalog of offerings that facilities can schedule and factions can
assign to their members.

## Responsibilities

- Core catalog models (`course.models`) for `Course`, `Requirement`, and `FacilityClass`.
- Validation and relationships that tie organization-specific course offerings to
  facility enrollments via `enrollment` models.
- Admin, serializer, and form helpers used by the facility + enrollment apps.

## Key Concepts

- **Course** – canonical record (name, description, duration, popularity, tags) that can
  require prerequisites.
- **Requirement** – reusable prerequisite metadata used across multiple courses.
- **FacilityClass** – binds a course to a specific facility enrollment/session and
  enforces max enrollment counts; referenced by the scheduling service when attendees
  enroll in classes.

## Development Notes

- When you create a new facility class, ensure the related `FacilityEnrollment` dates align
  with the session/periods defined in the enrollment app.
- Add tests or fixtures under `course/tests.py` if you introduce additional catalog features.

## Tests

```bash
python manage.py test course
```

Running the course tests validates model constraints and ensures requirements/courses
behave as expected.
