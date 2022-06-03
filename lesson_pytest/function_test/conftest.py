import logging

import pytest

from lesson_pytest.code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


def _test_method():
    pass


@pytest.fixture()
def human(random_age):
    _test_method()
    logger.info(msg='\nFixture start')
    yield Human(name='Ade', age=random_age, gender='male')
    logger.info(msg='\nFixture finished')


@pytest.fixture()
def create_old_woman():
    yield Human(name='Lara', age=99, gender='female')


@pytest.fixture()
def create_custom_human():
    def human_factory(name, age, gender):
        return Human(name=name, age=age, gender=gender)

    yield human_factory
