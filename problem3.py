import json
import random
import string

def read_json(path):
	with open(path, 'r') as f:
		data = json.load(f)
	return data

def write_json(path, data):
	with open(path, 'w') as out:
		json.dump(data, out)

def replace_quotes(string, a, b):
    return string.replace(a, b)

def str_to_dict(x):
	return json.loads(x)

def replace_with_random(dict_, keys):
    for key in keys:
        val_type = type(dict_[key])
        if val_type == str:
            length = len(dict_[key])
            dict_[key] = ''.join(random.choices(string.ascii_lowercase + string.digits, k= length))
        if val_type == 'float':
            dict_[key] = random.random()
    return dict_


def alter_data(data, trans_key, keys_to_replace):
	transactions = data[trans_key]
	altered_transactions = []
	
	for trans in transactions:
		val = trans[0]
		signature = trans[1]
		val = replace_quotes(val, '\'', '"')
		val = str_to_dict(val)
		val = replace_with_random(val, keys_to_replace)
		altered_data = json.dumps(val)
		altered_data = replace_quotes(altered_data, '"', '\'')
		altered_transactions.append([altered_data, signature])
	
	data[trans_key] = altered_transactions
	return data 
		

if __name__ == '__main__':
	input_path = 'testblock.json'
	output_path = 'alteredblock.json'
	data = read_json(input_path)
	data = alter_data(data, 'Transactions', ['RecipientAddress', 'SenderAddress', 'Amount'])
	write_json(output_path, data)

