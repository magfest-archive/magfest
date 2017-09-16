from . import *


@Session.model_mixin
class Attendee:
    @property
    def age_discount(self):
        # We dynamically calculate the age discount to be half the current badge price.
        # If for some reason the default discount (if it exists) is greater than half off, we use that instead.
        if 'val' in self.age_group_conf and self.age_group_conf['val'] == c.UNDER_13:
            half_off = math.ceil(c.BADGE_PRICE / 2)
            if not self.age_group_conf['discount'] or self.age_group_conf['discount'] < half_off:
                return -half_off
        return -self.age_group_conf['discount']

@Session.model_mixin
class Band:
    @property
    def panel_status(self):
        return str(len(self.group.leader.panel_applications)) + " Panel Application(s)" \
            if self.group.leader.panel_applications else self.status('panel')
