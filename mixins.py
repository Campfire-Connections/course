# course/mixin.py

from django.core.exceptions import ValidationError

class TimeSlotMixin:
    """Mixin to manage class time slots and check for scheduling conflicts."""

    def is_time_slot_available(self, start_time, end_time, facility_enrollment):
        """Check if the time slot is available in the facility."""
        conflicting_classes = self.__class__.objects.filter(
            facility_enrollment=facility_enrollment,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()

        return not conflicting_classes

    def get_duration(self):
        """Get the duration of the scheduled class."""
        return self.end_time - self.start_time


class FacilityClassMixin(TimeSlotMixin):
    """Mixin to handle facility class operations."""

    def get_course(self):
        return self.course

    def is_course_available(self):
        """Check if the class is available."""
        return self.enrollments.count() < self.max_capacity

    def get_schedule(self):
        """Return the schedule of the class."""
        return {
            'start_time': self.start_time,
            'end_time': self.end_time,
            'facility': self.facility_enrollment.facility,
        }

    def schedule_class(self, start_time, end_time, facility_enrollment):
        """Schedule a class while checking for conflicts."""
        if self.is_time_slot_available(start_time, end_time, facility_enrollment):
            self.start_time = start_time
            self.end_time = end_time
            self.facility_enrollment = facility_enrollment
            self.save()
        else:
            raise ValidationError("This time slot is not available.")
