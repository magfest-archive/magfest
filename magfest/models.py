from . import *


@Session.model_mixin
class Attendee:
    @cost_property
    def child_discount(self):
        if 'val' in self.age_group_conf and self.age_group_conf['val'] == c.UNDER_13:
            return math.ceil(c.BADGE_PRICE / 2) * -1
        return 0
