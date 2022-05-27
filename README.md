### Prerequisites
Clone the repository
```
$ git clone https://github.com/NYYCS/vox-backend-assignment.git
$ cd vox-backend-assignment
```

To install dependencies
```
$ pip install -r requirements.txt
```

### Running
```
$ uvicorn main:app
```
and the API can be accessed on `localhost:8000`, documentation can be accessed on `localhost:8000/docs`

### Testing
Ratelimit on the `/api/v1/hooli/message` can be tested by running
```
$ python -m unittest
```

### Notes
Is the mock api broken? Can't seem to do a POST request to it and get JSON response.
Currently just doing a GET request