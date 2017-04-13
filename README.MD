## ERROR_CODE

	0000 Everything is ok

	# account
	1001 password wrong
	1002 username can not be null
	1003 password can not be null
	1004 need login
	1005 token can not be null
	1006 token expired
	1007 token is invalid
	# resource
	1008 table_id can not be null
	1009 menus_id can not be null
	1010 menu_id can not be null
	1011 menu not found
	1012 order_id can not be null
	1013 order not found


## User Account


### login

`/user/login`

**request** `POST`

	{
		"password":"this is a password", 
		"username":"this is a username"
	}

**response** 

	{
		"status":ERROR_CODE
	} 

or 

	{
		"status":0, 
		"data":
				{
					"token":"this is a token"
				}
	
	}

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

### explore all orders
`/user/order/`

**request** `GET`

**response**

	{
	  "data": [
	    {
	      "amount": null,
	      "createdAt": "2017-04-12 12:52:43",
	      "id": 1,
	      "menu_count": 3,
	      "menus": [
	        {
	          "category": null,
	          "id": 1,
	          "name": "Douglas Stewart",
	          "price": 1,
	          "subcategory": null
	        },
	        {
	          "category": null,
	          "id": 2,
	          "name": "Carlos Riggs",
	          "price": 2,
	          "subcategory": null
	        },
	        {
	          "category": null,
	          "id": 3,
	          "name": "John Meszaros",
	          "price": 3,
	          "subcategory": null
	        }
	      ],
	      "table_id": 19,
	      "uid": 31
	    }
	  ],
	  "status": 0
	}
​	


## Table 

### explore all tables
`/table/`

**request** `GET`

**response**

	{
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
	}


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

## Order

### create order
`order/create`

**request** `POST`

	{
	  "table_id" : 2,
	  "menus_id" : 1,3,4 # string, separate with ','
	}

**response**

	{
	  "data": {
	    "amount": 8,
	    "createdAt": "2017-04-12 14:42:39",
	    "id": 14,
	    "menus": [
	      {
	        "category": null,
	        "id": 1,
	        "name": "Douglas Stewart",
	        "price": 1,
	        "subcategory": null
	      },
	      {
	        "category": null,
	        "id": 3,
	        "name": "John Meszaros",
	        "price": 3,
	        "subcategory": null
	      },
	      {
	        "category": null,
	        "id": 4,
	        "name": "William Ortiz",
	        "price": 4,
	        "subcategory": null
	      }
	    ],
	    "table_id": 3,
	    "uid": 31
	  },
	  "status": 0
	}

### fetch order detail by id

**request** `POST`

	{
		"order_id":23
	}

**response**

	{
	  "data": {
	    "amount": 9,
	    "createdAt": "2017-04-12 17:16:05",
	    "id": 95,
	    "menus": [
	      {
	        "category": null,
	        "id": 1,
	        "name": "Douglas Stewart",
	        "price": 1,
	        "subcategory": null
	      },
	      {
	        "category": null,
	        "id": 3,
	        "name": "John Meszaros",
	        "price": 3,
	        "subcategory": null
	      },
	      {
	        "category": null,
	        "id": 5,
	        "name": "Melinda Carrasco",
	        "price": 5,
	        "subcategory": null
	      }
	    ],
	    "table_id": 34,
	    "uid": 31
	  },
	  "status": 0
	}