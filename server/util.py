from config import PROFILE_PICTURES_DIR
import requests
import os


def get_and_save_profile_picture(gender, number):
    gender_map = {'male': 'men', 'female': 'women'}

    if gender not in gender_map:
        raise ValueError("Gender must be 'male' or 'female'.")

    mapped_gender = gender_map[gender]

    url = f"https://randomuser.me/api/portraits/{mapped_gender}/{number}.jpg"
    response = requests.get(url)

    if response.status_code == 200:
        os.makedirs(PROFILE_PICTURES_DIR, exist_ok=True)

        image_path = os.path.join(PROFILE_PICTURES_DIR, f"{number}.png")
        with open(image_path, 'wb') as file:
            file.write(response.content)

        print(f"Image saved to {image_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
