from . import *


@prereg_validation.Attendee
def group_leader_under_13(attendee):
    if attendee.badge_type == c.PSEUDO_GROUP_BADGE and attendee.age_group_conf['val'] in [c.UNDER_6, c.UNDER_13]:
        return "Children under 13 cannot be group leaders."


@prereg_validation.Attendee
def total_cost_over_paid(attendee):
    if attendee.total_cost < attendee.amount_paid:
        if attendee.orig_value_of('birthdate') < attendee.birthdate and attendee.age_group_conf['val'] in [c.UNDER_6, c.UNDER_13]:
            return 'The date of birth you entered incurs a discount; please email {} to change your badge and receive a refund'.format(c.REGDESK_EMAIL)
        return 'You have already paid ${}, you cannot reduce your extras below that.'.format(attendee.amount_paid)
