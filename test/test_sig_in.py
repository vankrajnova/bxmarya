# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_sig_in(app):
    app.login_page(username="bxuser", password="bxuser")
    app.logout()


def test_sig_in_empty_password(app):
    app.login_page(username="bxuser", password="")



