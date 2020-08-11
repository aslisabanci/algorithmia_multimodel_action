import Algorithmia


def call_algo(mgmt_api_key: str, orchestrator_algo_path: str, algo_input: str):
    client = Algorithmia.client(api_key=mgmt_api_key)
    algo = client.algo(orchestrator_algo_path)
    print(algo.pipe(algo_input).result)
