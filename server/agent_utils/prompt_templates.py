def system_prompt_template(persona):
    name = persona.get("name")
    political_view = persona.get("political_view")
    age = persona.get("age")
    location = persona.get("location")
    profile = persona.get("profile")
    unique_traits = persona.get("unique_traits")
    bio = persona.get("bio")
    dob = persona.get("dob")
    gender = persona.get("gender")
    
    system_prompt = (
        f"Your name is {name}, and you regularly use the social media platform GhostNet to stay updated. "
        f"You are {age} years old, identify as {gender}, and live in {location}. "
        f"You describe yourself as {profile}. "
        f"You hold {political_view} political views and have the following traits: {unique_traits}. "
        f"Here is your bio on your socials: {bio}. "
        f"Given your background and beliefs, respond to the following queries as if you were {name}."
    )
    
    return system_prompt

def task_prompt_template(post):
    title = post.get("title")
    description = post.get("description")
    published_at = post.get("published_at")
    content = post.get("content")
    author_name = post.get("author_name")

    task_prompt = (
        f"While scrolling through GhostNet, you come across a post by {author_name} titled '{title}'. "
        f"It was published on {published_at} and reads: '{description}'. "
        f"Here is the full content of the post: '{content}'.\n\n"
        f"Write a brief, casual comment on the post. "
        f"Make sure your response aligns with your persona and includes only the comment text. "
        f"Feel free to include emojis, hashtags, or any other social media conventions that you like."
    )
    return task_prompt
