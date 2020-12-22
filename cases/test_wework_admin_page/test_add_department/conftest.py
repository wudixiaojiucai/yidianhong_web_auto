import time
import pytest


@pytest.fixture()
def back_fixture(main):
    yield
    main.add_depart_back()
