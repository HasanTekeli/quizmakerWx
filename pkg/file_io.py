import json


def read_file(path=None):
    with open(path, "r") as file_in:
        data = json.load(file_in)
        return data


def write_file(path=None, question_dict=None):
    json_file = open(path, "r")
    indata = json.load(json_file)
    json_file.close()

    print(indata["exam"][0]["questions"])
    q_dict = indata["exam"][0]["questions"]

    q_dict["question"] = question_dict["question"]
    q_dict["ca"] = question_dict["ca"]
    q_dict["wa1"] = question_dict["wa1"]
    q_dict["wa2"] = question_dict["wa2"]
    q_dict["wa3"] = question_dict["wa3"]

    json_file = open(path, "w")
    json_file.write(json.dumps(indata, ensure_ascii=False, indent=4))
    json_file.close()

