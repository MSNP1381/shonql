import json
import os
from urllib import response
import black
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from tqdm import tqdm
from prompts import main_prompt

import re
from parser import parse

load_dotenv()

def print_res(old_d: dict, result, just_ans=True):
    d = old_d.copy()
    d["tools"] = json.loads(d["tools"])
    if just_ans:
        del d["tools"]
    d["answers"] = (d["answers"])
    print("-" * 12, end="\n\n\n")
    print(black.format_str(str(d), mode=black.Mode()))
    print("-" * 12, end="\n\n\n")
    print(result)


def handle_response(response):
    pattern = re.compile(r"(?s)```shonqol\s*([\s\S]*?)\s*```")
    matches = pattern.findall(response)

    # for code_block in matches:
    # return parse(matches[0])

    return matches[0]


def calc_hit_fn_arg(answers, extracted):
    hit_fn = 0
    hit_arg = 0
    tot_args = 0

    # Filter out non-dictionary entries and entries missing keys
    valid_answers = [
        a for a in answers if isinstance(a, dict) and "name" in a and "arguments" in a
    ]
    valid_extracted = [
        e for e in extracted if isinstance(e, dict) and "name" in e and "arguments" in e
    ]

    # Create a lookup for extracted functions by name
    extracted_lookup = [(e["name"], e) for e in valid_extracted]
    fn_names_set = set([e["name"] for e in valid_extracted])
    # Create a lookup for extracted functions by name mapping to a list of their 'arguments' lists
    extracted_lookup = {}
    for e in valid_extracted:
        extracted_lookup.setdefault(e["name"], []).append(e["arguments"])

    for a in valid_answers:
        fn_name = a["name"]
        if fn_name in extracted_lookup:
            hit_fn += 1
            ans_args = list(a["arguments"].values())
            tot_args += len(ans_args)
            for aarg in ans_args:
                # Check across all extracted function calls for this name, order doesn't matter
                if any(aarg in ext_args for ext_args in extracted_lookup[fn_name]):
                    hit_arg += 1

    print("hit_fn", hit_fn, "out of", len(valid_answers))
    print("hit_arg", hit_arg, "out of", tot_args)
    return (hit_fn, len(valid_answers)), (hit_arg, tot_args)


prompt = ChatPromptTemplate.from_messages(
    [("system", main_prompt), ("user", "{query}")]
)
llm = prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0) | StrOutputParser()

with open("brekeley/BFCL_v3_live_parallel_multiple_converted.json") as f:
    items_list = json.load(f)
os.makedirs("brekeley/shonqol_results", exist_ok=True)
for i in tqdm(items_list, desc="Processing"):
    result=llm.invoke(i)
    tqdm.write("query id: "+i['id'])
    tqdm.write("\n\n"+result+"\n\n")
    matched=handle_response(result)
    # print_res(i, response_handled)
    ans={'llm_response':matched,'answer':i['answers']}
    with open(f"brekeley/shonqol_results/{i['id']}.json","w") as f:
        f.write(json.dumps(ans,indent=2))  