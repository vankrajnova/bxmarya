# -*- coding: utf-8 -*-
import pytest
from application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.login_page(username="bxuser", password="bxuser")
    app.logout()


def test_login_empty_password(app):
    app.login_page(username="bxuser", password="")



