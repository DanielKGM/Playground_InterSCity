from services.api_client import APIClient
from models.resource import Resource
from models.capability import Capability


class CatalogService:
    def __init__(self):
        self.api_client = APIClient()

    def create_resource(self, data: dict) -> Resource:
        data = {"data":data}
        json_response = self.api_client.request(method="POST", endpoint="/catalog/resources", data=data, first=True)
        return Resource.model_validate(json_response)

    def list_resources(self, params: dict = None) -> list[Resource]:
        json_response = self.api_client.request(method="GET", endpoint="/catalog/resources", params=params, first=True)
        return [Resource.model_validate(item) for item in json_response]

    def list_sensors(self) -> list[Resource]:
        json_response = self.api_client.request(method="GET", endpoint="/catalog/resources/sensors",first=True)
        return [Resource.model_validate(item) for item in json_response]

    def list_actuators(self) -> list[Resource]:
        json_response = self.api_client.request(method="GET", endpoint="/catalog/resources/actuators", first=True)
        return [Resource.model_validate(item) for item in json_response]

    def search_resources(self, query: dict) -> list[Resource]:
        json_response = self.api_client.request(method="GET", endpoint="/catalog/resources/search", params=query, first=True)
        return [Resource.model_validate(item) for item in json_response]

    def get_resource(self, uuid: str) -> Resource:
        json_response = self.api_client.request(method="GET", endpoint=f"/catalog/resources/{uuid}", first=True)
        return Resource.model_validate(json_response)

    def update_resource(self, uuid: str, data: dict) -> Resource:
        data = {"data":data}
        json_response = self.api_client.request(method="PUT", endpoint=f"/catalog/resources/{uuid}", data=data, first=True)
        return Resource.model_validate(json_response)

    def update_capability(self, name: str, data: dict) -> Capability:
        json_response = self.api_client.request(method="PATCH", endpoint=f"/catalog/capabilities/{name}", data=data)
        return Capability.model_validate(json_response)

    def create_capability(self, data: dict) -> Capability:
        json_response = self.api_client.request(method="POST", endpoint="/catalog/capabilities", data=data)
        return Capability.model_validate(json_response)

    def list_capabilities(self) -> list[Capability]:
        json_response = self.api_client.request(method="GET", endpoint="/catalog/capabilities", first=True)
        return [Capability.model_validate(item) for item in json_response]

    def get_capability(self, name: str) -> Capability:
        json_response = self.api_client.request(method="GET", endpoint=f"/catalog/capabilities/{name}")
        return Capability.model_validate(json_response)

    def delete_capability(self, name: str) -> dict:
        json_response = self.api_client.request(method="DELETE", endpoint=f"/catalog/capabilities/{name}")
        return json_response
