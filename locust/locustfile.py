from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    def on_start(self) -> None:
        response = self.client.post("/accounts/api/v2/jwt/create/", data={
        "email": "a@a.ar",
        "password": "123"
        }).json()
        self.client.headers = {"Authorization": f"Bearer {response.get("access")}"}
        # return super().on_start()
        

    @task
    def post_api(self):
        self.client.get("/blog/api/v1/post/")


    @task
    def category_api(self):
        self.client.get("/blog/api/v1/category/")