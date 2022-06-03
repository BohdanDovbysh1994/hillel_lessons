import logging

import pytest

from lesson_pytest.code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


class TestHuman:

    @pytest.fixture(autouse=True)
    def human(self):
        self.human = Human(name='Taras', age=20, gender='male')

    def setup_class(self):
        logger.info(msg='Setup for suite')

    def setup(self):
        self.hima
        logger.info(msg='Setup for each test')

    def test_01(self):
        self.human.grow()
        assert self.human.age == 21, f'\nAge not as expected\nActual: {self.human.age}\nExpected: 21'

    def test_02(self):
        self.human.grow()
        assert self.human.age == 21, f'\nAge not as expected\nActual: {self.human.age}\nExpected: 25'

    def teardown(self):
        logger.info(msg='Tear down after each test')

    def teardown_class(self):
        logger.info(msg='Tear down class')
