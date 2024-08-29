from concurrent.futures import ThreadPoolExecutor, as_completed
from agent_utils.prompt_templates import task_prompt_template
import random

def generate_comments(agents_all, post, top_k_agents=4):
    author_id = post.get("author_id")
    print("author id", author_id)
    
    # sample agents excluding the author of the post
    sampled_agents = random.sample([agent for agent in agents_all if agent.user_details.get("id") != author_id], top_k_agents)


    def get_agent_comment(agent):
        return agent.get_ai_response(task_prompt_template(post))

    agent_comments = []
    
    with ThreadPoolExecutor() as executor:
        future_to_agent = {executor.submit(get_agent_comment, agent): agent for agent in sampled_agents}
        for future in as_completed(future_to_agent):
            agent_comment = future.result()
            agent_comments.append(agent_comment)
    
    return agent_comments