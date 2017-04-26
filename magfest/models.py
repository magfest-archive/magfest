from . import *


@Session.model_mixin
class Attendee:
    @property
    def age_discount(self):
        # We dynamically calculate the age discount to be half the current badge price
        if 'val' in self.age_group_conf and self.age_group_conf['val'] == c.UNDER_13:
            return math.ceil(c.BADGE_PRICE / 2) * -1
        else:
            return -self.age_group_conf['discount']
