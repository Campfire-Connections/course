from course.models.course import Course
from course.models.requirement import Requirement


def course_list_queryset():
    return Course.objects.select_related("parent").prefetch_related(
        "requirements",
        "prerequisites",
    )


def course_detail_queryset():
    return course_list_queryset()


def requirement_list_queryset():
    return Requirement.objects.order_by("name")


def requirement_detail_queryset():
    return Requirement.objects.all()
