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
      "uid": null
    },
    {
      "available": 1,
      "id": 11,
      "uid": null
    }
  ],
  "status": 0
}```