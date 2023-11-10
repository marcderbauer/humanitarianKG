from pipeline.transform.transformer_util import convert_prompt_to_llm_query, process_response
from pipeline.transform.prompts import prompts # ! Where to move?
from pipeline.transform.llm import query_llm

# TODO: Move into config file
MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = 0
TOP_P = 0.8

class Transformer():
    def __init__(self) -> None:
        pass

    def process(data: str):
        results = {"entities": [], "relationships": []}

        for prompt in prompts: # ! not immediately visible where prompts comes from, move into config
            llm_query = convert_prompt_to_llm_query(data, prompt)
            response = query_llm(llm_query, model_name=MODEL_NAME, temperature=TEMPERATURE, top_p=TOP_P)
            result = process_response(response)
            results.update(result)

        return results