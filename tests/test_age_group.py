def test_create_age_group(test_app):
    response = test_app.post("/age-groups/", json={"min_age": 18, "max_age": 25})
    assert response.status_code == 200
    assert isinstance(response.json(), str)

def test_get_age_groups(test_app):
    response = test_app.get("/age-groups/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
