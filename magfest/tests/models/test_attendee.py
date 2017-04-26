from uber import config
from uber.tests import *
from uber.tests.conftest import *


class TestCosts:
    @pytest.fixture(autouse=True)
    def mocked_prices(self, monkeypatch):
        monkeypatch.setattr(c, 'get_oneday_price', Mock(return_value=10))
        monkeypatch.setattr(c, 'get_attendee_price', Mock(return_value=40))

    def test_half_price_discount(self):
        # Age group discount not set: badge is half off
        assert 20 == Attendee(age_group=c.UNDER_13).badge_cost

    def test_half_price_overrides_age_discount(self, monkeypatch):
        # Age group discount is less than half off: badge is half off
        monkeypatch.setattr(Attendee, 'age_group_conf', {'val': c.UNDER_13, 'discount': 5})
        assert 20 == Attendee(age_group=c.UNDER_13).badge_cost

    def test_age_discount_overrides_half_price(self, monkeypatch):
        # Age group discount is greater than half off: badge price based on age discount instead
        monkeypatch.setattr(Attendee, 'age_group_conf', {'val': c.UNDER_13, 'discount': 30})
        assert 10 == Attendee(age_group=c.UNDER_13).badge_cost
