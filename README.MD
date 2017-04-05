## User Account


### login

`/user/login`

**request**

`{"password":"this is a password", "username":"this is a username"}`

**response** 

```{"status":ERROR_CODE}``` 

or 

```{"status":0, "data":{"token":"this is a token"}}```
