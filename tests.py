from django.urls import reverse

from core.tests import BaseDomainTestCase


class CourseModelTests(BaseDomainTestCase):
    def test_course_string_representation(self):
        self.assertEqual(str(self.course), "Navigation Basics")

    def test_course_requirement_relationship(self):
        self.assertIn(self.requirement, self.course.requirements.all())

    def test_absolute_url_targets_slug_route(self):
        url = self.course.get_absolute_url()
        self.assertIn(self.course.slug, url)


class CourseViewTests(BaseDomainTestCase):
    def test_show_view_by_slug(self):
        url = reverse("courses:show", kwargs={"course_slug": self.course.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)

    def test_show_view_by_id(self):
        url = reverse("courses:show_by_id", kwargs={"course_id": self.course.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)
