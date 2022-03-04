def message(input_dict):
    output = "In " + input_dict["movie"] + ", name is a " + input_dict["role"] + "."
    return output

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
