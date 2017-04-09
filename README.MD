## ERROR_CODE

* 0000 Everything is ok

* 1001 password wrong
* 1002 username can not be null
* 1003 password can not be null
* 1004 need login
* 1005 token can not be null
* 1006 token expired
* 1007 token is invalid



## User Account


### login

`/user/login`

**request** `POST`

`{"password":"this is a password", "username":"this is a username"}`

**response** 

```{"status":ERROR_CODE}``` 

or 

```{"status":0, "data":{"token":"this is a token"}}```

**You should set the `token` into HTTP header using key-value `token:TOKEN_STRING` to access following resource**


### register

`/user/register`

**request** `POST`

	{
		"name": "daming",
	    "password": "456"
	}

**response**

	{
	  "data": {
	    "age": null,
	    "avatar": null,
	    "gender": null,
	    "id": 105,
	    "name": "daming",
	    "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ5Nzc0MjE1MSwiaWF0IjoxNDkxNzQyMTUxfQ.eyJpZCI6MTA1fQ.mC7mcxUFkjsQiGJhKlZd-BYIc4SG6Xn5yag4_pFobj4"
	  },
	  "status": 0
	}

## Table 

### explore all tables
`/table/`

**request** `GET`

**response**

```{
  "data": [
    {
      "available": 1,
      "id": 10,
      "uid": null # if is unavailable, uid will be user's id 
    },
    {
      "available": 1,
      "id": 11,
      "uid": null
    }
  ],
  "status": 0
}```


## Menu

### explore all menus
`/menu/`

**request** `GET`
**reponse** 
	{
	  "data": [
	    {
	      "category": null,
	      "id": 6,
	      "name": "Barbara Bratcher",
	      "price": 6,
	      "subcategory": null
	    },
	    {
	      "category": null,
	      "id": 7,
	      "name": "Matt Cruz",
	      "price": 7,
	      "subcategory": null
	    },
	    {
	      "category": null,
	      "id": 8,
	      "name": "Jason Decker",
	      "price": 8,
	      "subcategory": null
	    },
	    {
	      "category": null,
	      "id": 9,
	      "name": "Charles Montgomery",
	      "price": 9,
	      "subcategory": null
	    }
	  ],
	  "status": 0
	}