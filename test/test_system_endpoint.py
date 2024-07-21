from assertpy import assert_that
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest import mock

from api.endpoints.system import api as system_api

def test_get_system_loading_SUCCESS():
    
    app = FastAPI()
    
    system_api.register_endpoints(app)
    
    test_client = TestClient(app)
    rsp = test_client.get("system/loading",
                          headers={"accept": "application/json"})
    
    assert_that(rsp.status_code).is_equal_to(200)

@mock.patch("psutil.cpu_percent", side_effect=Exception("something wrong"))
def test_get_system_loading_FAIL(mocker):
    
    app = FastAPI()
    
    system_api.register_endpoints(app)
    
    test_client = TestClient(app)
    rsp = test_client.get("system/loading",
                          headers={"accept": "application/json"})
    
    assert_that(rsp.status_code).is_equal_to(502)