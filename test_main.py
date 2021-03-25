import main 
import tempfile
import json


'''
In an actual production environment, we would have integration tests.
However, for local testing purposes this suffices.
'''

def test_directoryHunt():

    with tempfile.TemporaryDirectory() as directory:
        print('The created temporary directory is %s' % directory)

        with open(directory + '/randomfile.txt', 'w') as writer:
            writer.write("Random file with random text in it!")

        response = main.directoryHunt(directory, "")
        assert json.loads(response) == [
            {
                "permission":"drwx------",
                "owner":"rebeccahsieh",
                "group":"staff",
                "size":"96",
                "name":"."
            },
            {
                "permission":"drwx------@",
                "owner":"rebeccahsieh",
                "group":"staff",
                "size":"3968",
                "name":".."
            },
            {
                "permission":"-rw-r--r--",
                "owner":"rebeccahsieh",
                "group":"staff",
                "size":"35",
                "name":"randomfile.txt"
            }
        ]

def test_directoryHunt_nofile():
    with tempfile.TemporaryDirectory() as directory:
        print('The created temporary directory is %s' % directory)

        response = main.directoryHunt(directory, "")
        assert json.loads(response) == [
            {
                "permission":"drwx------",
                "owner":"rebeccahsieh",
                "group":"staff",
                "size":"64",
                "name":"."
            },
            {
                "permission":"drwx------@",
                "owner":"rebeccahsieh",
                "group":"staff",
                "size":"3968",
                "name":".."
            }
        ]

def test_directoryHunt_periodinput():
    response = main.directoryHunt(".")
    assert json.loads(response) == {
        "error": "Please put in a valid path"
    }

def test_directoryHunt_multiperiodinput():
    response = main.directoryHunt("..")
    print("!! response is ", response)
    assert json.loads(response) == {
        "error": "Please put in a valid path"
    }
