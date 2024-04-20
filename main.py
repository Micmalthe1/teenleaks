import requests

TOKEN = "AjvrcE0XuuhwefeSKbl-e6H7FIv1wIrXyFQGK9XtPjXaSgcx4C4q9zTDilybBDtDwnlmhL9UG9UPNLWTyHBryw"

try:
    with open('cookies.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        MESSAGE = line.strip()

        response = requests.post(
            "https://paster.so/api/v2/publishers/pastes/markdown/create",
            headers={"Content-Type": "application/json", "Authorization": TOKEN},
            json={"content": MESSAGE, "title": "🎁"}
        )

        response_data = response.json()

        if "paste" in response_data and "url" in response_data["paste"]:
            paste_url = response_data["paste"]["url"]
            print("Uploaded line:", MESSAGE)
            print("URL:", paste_url)

            with open('valid.txt', 'a') as valid_file:
                valid_file.write(paste_url + '\n')
        else:
            print("Response did not contain a URL:", response_data)

except requests.exceptions.RequestException as e:
    print("Error making the request:", e)
except FileNotFoundError:
    print("Error: 'cookies.txt' file not found")
