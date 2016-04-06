# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_sig_in(app):
    app.session.login(username="bxuser", password="bxuser")
    app.session.logout()


def test_sig_in_empty_password(app):
    app.session.login(username="bxuser", password="")



