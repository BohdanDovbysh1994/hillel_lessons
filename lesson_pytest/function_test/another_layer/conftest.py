import pytest

from lesson_pytest.code_for_testing import Human


@pytest.fixture()
def human_2():
    return Human(name='Ade', age=25, gender='male')
    # logger.info(msg='Fixture finished')
