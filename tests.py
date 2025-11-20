from core.tests import BaseDomainTestCase


class CourseModelTests(BaseDomainTestCase):
    def test_course_string_representation(self):
        self.assertEqual(str(self.course), "Navigation Basics")

    def test_course_requirement_relationship(self):
        self.assertIn(self.requirement, self.course.requirements.all())
