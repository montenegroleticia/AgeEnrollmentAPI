def test_get_age_groups(test_app):
    response = test_app.get("/age-groups/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
