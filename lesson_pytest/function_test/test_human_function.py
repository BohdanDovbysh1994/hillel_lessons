import logging

import pytest

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.ui
def test_human_grow_age(create_custom_human):
    human_1 = create_custom_human(name='Anna', age=75, gender='male')
    human_2 = create_custom_human(name='Petro', age=105, gender='female')

    human_2.grow()
    with pytest.raises(Exception) as e:
        human_1.gender = 'TTTT'
    assert human_1.name == 'Anna', f'\nName is not as expected\nActual: {human_1.name}\nExpected:Anna'
    assert human_2.name == 'Petro!!!', f'MESSAGE'


@pytest.mark.regression_for_linux
@pytest.mark.skip('We want skip this test')
@pytest.mark.ui
def test_human_grow_age_2(human):
    logger.info('\nTEST START')
    human_a = human
    human_a.grow()
    assert human_a.age == 70, f'ERROR'


@pytest.mark.regression
def test_human_grow_age_3(create_old_woman):
    logger.info('\nTEST START')
    human_a = create_old_woman
    human_a.grow()
    assert human_a.age == 100, f'ERROR'

# @pytest.mark.custom_mark
# def test_02(human):
#     assert human.age == 25


# def test_03(custom_human, action):
#     human_1 = custom_human(name='Ade', age=25, gender='male', action=action)
#     human_2 = custom_human(name='Molly', age=50, gender='female', action=action)
#     new_g = 'male'
#     human_2.gender = new_g
#     assert human_1.age != human_2.age, f'\nAge is not as expected'
