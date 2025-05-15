import pytest
import allure
from utils.request_handler import RequestHandler
from utils.yaml_handler import load_yaml

config = load_yaml("config/config.yaml")
test_data = load_yaml("data/test_data.yaml")

handler = RequestHandler(base_url=config["base_url"], timeout=config.get("timeout", 10))

@pytest.mark.parametrize("case", test_data["cases"])
def test_api(case):
    with allure.step("发送请求"):
        response = handler.send_request(
            method=case["method"],
            endpoint=case["endpoint"],
            data=case["payload"],
            headers=config["headers"]
        )
    with allure.step("打印响应内容"):
        print("接口返回：", response.json())
        allure.attach(str(response.json()), name="接口返回内容", attachment_type=allure.attachment_type.TEXT)
    with allure.step("断言响应状态码"):
        assert response.status_code == case["expected"]["status_code"]
    with allure.step("断言响应关键字段"):
        resp_json = response.json()
        assert resp_json["code"] == case["expected"]["response"]["code"]
        assert resp_json["msg"] == case["expected"]["response"]["msg"]