import os
import random

def handler(request, response):
    uid = request.args.get("uid")

    if not uid:
        response.status_code = 400
        return response.json({"error": "UID required"})

    avatar_folder = "avatars"

    try:
        files = os.listdir(avatar_folder)
        images = [f for f in files if f.endswith(".png")]

        if not images:
            response.status_code = 500
            return response.json({"error": "No avatars found"})

        image = random.choice(images)

        file_path = os.path.join(avatar_folder, image)

        response.status_code = 200
        response.headers["Content-Type"] = "image/png"

        with open(file_path, "rb") as f:
            return response.send(f.read())

    except Exception as e:
        response.status_code = 500
        return response.json({"error": str(e)})