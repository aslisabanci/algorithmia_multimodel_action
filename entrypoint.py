#!/usr/bin/python3

import os, json
from action_src import call_algo


if __name__ == "__main__":
    api_key = os.getenv("INPUT_API_KEY")
    parallel_algo_names = os.getenv("INPUT_PARALLEL_ALGO_NAMES")
    parallel_algo_inputs = os.getenv("INPUT_PARALLEL_ALGO_INPUT")

    repo_name = os.getenv("INPUT_PATH")
    algo_hash = os.getenv("GITHUB_SHA")

    repo_path = "/github/workspace/{}".format(repo_name)

    if not api_key:
        raise Exception("field 'api_key' not defined in workflow")
    if not parallel_algo_names:
        raise Exception("field 'parallel_algo_names' not defined in workflow")
    if not parallel_algo_inputs:
        raise Exception("field 'parallel_algo_inputs' not defined in workflow")

    if os.path.exists(repo_path):
        with open("{}/{}".format(repo_path, "algorithmia.conf")) as f:
            config_data = json.load(f)
        algo_name = "{}/{}".format(config_data["username"], config_data["algoname"])

        algo_input_dict = {
            "parallel_algo_names": parallel_algo_names,
            "parallel_algo_inputs": parallel_algo_inputs,
        }

        algo_input = json.dumps(algo_input_dict)
        call_algo(api_key, algo_name, algo_hash, algo_input)
    else:
        raise Exception(
            "actions/checkout on the local repo must be run before this action can be completed"
        )
