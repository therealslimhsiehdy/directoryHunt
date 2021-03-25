from fastapi import FastAPI, Path

import uvicorn
import subprocess
import json

app = FastAPI()


@app.get("/")
@app.get("/{full_path:path}")

def directoryHunt(full_path: str = "", filepath = "/mnt/mydata"):
    """
    INPUT: A path in str type
    OUTPUT: JSON format of a directory showing the file name, owner, size, and permissions
    DESCRIPTION:
    directoryHunt takes in a path given by the user. We run the "ls -la" OS command on the path 
    and translate the output into JSON format
    """
    
    all_files = []
    return_dir = []

    try:
        stream = subprocess.check_output(["ls", "-la", filepath + "/" + full_path])

    except subprocess.CalledProcessError:
        return json.dumps({"error": "Please put in a valid path"})

    all_files = stream.decode("utf-8").split("\n")

    try:
        for eFile in all_files[1:-1]:
            sublist = eFile.split()
            permission = sublist[0]
            owner = sublist[2]
            group = sublist[3]
            size = sublist[4]
            name = sublist[8]

            return_dir.append(
                {
                    "permission": permission,
                    "owner": owner,
                    "group": group,
                    "size": size,
                    "name": name,
                }
            )

        return json.dumps(return_dir)

    except Exception as e:
        return str(e)

# Setting host and port for application to run on
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
