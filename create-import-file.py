#!/usr/bin/python3

filename = 'quotes'

def quote_to_json(quote,i):
    json = f"""
        {{
            "PutRequest": 
                {{"Item": 
                    {{
                        "quote-id": {{"N": "{i}" }},
                        "quote": {{"S": "{quote}" }}
                    }}
                }}
        }}
        """
    return json

def clean(quote):
    return quote.strip().replace('"','\\"')


with open(filename) as f:
    content = map(clean,f.readlines())
    json_put_objects = [quote_to_json(quote, i) for i,quote in enumerate(content) if quote]
    total_nbr_objects = len(json_put_objects)

    # aws cli batch write can only proccess maximum of 25 items
    for i, pos in enumerate(range(0,total_nbr_objects, 25)):
        batch = ','.join(json_put_objects[pos:pos+25])
        out_file = open(f'dynamo_import_{i}.json', "w")
        out_file.write(f"""{{ 
                        "linus-quotes": [{batch}]
                    }}""")
        out_file.close()
