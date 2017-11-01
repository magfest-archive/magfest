from magfest import *


@all_renderable(c.PEOPLE)
class Root:
    def index(self, session, message=''):
        raise HTTPRedirect('../dept_checklist/?message={}', message)

    def treasury(self, session, department_id, submitted=None, csrf_token=None):
        attendee = session.admin_attendee()
        department_id = Department.to_id(department_id)
        department = session.query(Department).options(
            subqueryload(Department.dept_checklist_items)).get(department_id)
        if submitted:
            slug = 'treasury'
            item = department.checklist_item_for_slug(slug)
            if not item:
                item = DeptChecklistItem(
                    attendee=attendee, department=department, slug=slug)
            check_csrf(csrf_token)  # since this form doesn't use our normal utility methods, we need to do this manually
            session.add(item)
            raise HTTPRedirect(
                '../dept_checklist/index?department_id={}&message={}',
                department_id,
                'Thanks for completing the MPoints form!')

        return {'department': department}

    def allotments(self, session, department_id, submitted=None, csrf_token=None, **params):
        attendee = session.admin_attendee()
        department_id = Department.to_id(department_id)
        department = session.query(Department).options(
            subqueryload(Department.dept_checklist_items)).get(department_id)
        conf = DeptChecklistConf.instances['allotments']
        if submitted:
            slug = 'allotments'
            item = department.checklist_item_for_slug(slug)
            if not item:
                item = DeptChecklistItem(
                    attendee=attendee, department=department, slug=slug)
            check_csrf(csrf_token)  # since this form doesn't use our normal utility methods, we need to do this manually
            item.comments = render('magfest_dept_checklist/allotments.txt', params).decode('utf-8')
            session.add(item)
            raise HTTPRedirect(
                '../dept_checklist/index?department_id={}&message={}',
                department_id,
                'Treasury checklist data uploaded')

        return {'department': department}

    def tech_requirements(self, session, department_id, submitted=None, csrf_token=None):
        attendee = session.admin_attendee()
        department_id = Department.to_id(department_id)
        department = session.query(Department).options(
            subqueryload(Department.dept_checklist_items)).get(department_id)
        if submitted:
            slug = 'tech_requirements'
            item = department.checklist_item_for_slug(slug)
            if not item:
                item = DeptChecklistItem(
                    attendee=attendee, department=department, slug=slug)
            check_csrf(csrf_token)  # since this form doesn't use our normal utility methods, we need to do this manually
            session.add(item)
            raise HTTPRedirect(
                '../dept_checklist/index?department_id={}&message={}',
                department_id,
                'Thanks for completing the tech requirements form!')

        return {'department': department}
