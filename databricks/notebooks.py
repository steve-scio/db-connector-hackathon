import constants

def list_notebooks():
    # Send a request to list notebooks
    params = {
        'path': '/Users/alexis.deschamps@databricks.com/example_folder_1'
    }
    response = constants.send_request("/api/2.0/workspace/list", params=params)
    print(response)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        notebooks = response.json()["objects"]
        print("Notebooks in the workspace:")
        for notebook in notebooks:
            print(notebook["path"])
    else:
        print(f"Failed to list notebooks. Status code: {response.status_code}")
        print(response.text)
        
list_notebooks()