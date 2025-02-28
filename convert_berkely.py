#%%
import json

# %%
with open("./brekeley/BFCL_v3_live_parallel_multiple.json") as f:
    items_q=f.readlines()
# %%
with open("brekeley/BFCL_v3_live_parallel_multiple_ans.json") as f:
    items_ans=f.readlines()
# %%
items=zip(items_q,items_ans)
# %%
items_list=[]
for q,ans in items:
    q=json.loads(q)
    ans=json.loads(ans)
    if len(q['question'][0])>1:
        print("more than one question")
    # d={'id':q['id'],
    #     'query':q['question'][0][0]['content'],
    #    'answers':ans['ground_truth'],
    #    "tools":json.dumps(q['function'],indent=2)
    #    }
    # items_list.append(d)
# %%
items_list
# %%
with open("brekeley/BFCL_v3_live_parallel_multiple_converted.json","w") as f:
    f.write(json.dumps(items_list,indent=2))
# %%
