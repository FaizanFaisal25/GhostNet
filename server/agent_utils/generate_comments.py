from concurrent.futures import ThreadPoolExecutor, as_completed
from agent_utils.prompt_templates import task_prompt_template

def generate_comments(agents, post):
    def get_agent_comment(agent):
        return agent.get_ai_response(task_prompt_template(post))

    agent_comments = []
    
    with ThreadPoolExecutor() as executor:
        future_to_agent = {executor.submit(get_agent_comment, agent): agent for agent in agents}
        for future in as_completed(future_to_agent):
            agent_comment = future.result()
            agent_comments.append(agent_comment)
    
    return agent_comments