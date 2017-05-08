# Menu Category

```json
id  categoryname
0   今日推荐
1   盖浇饭
2   面食
3   炒饭
4   汤饭
```



## ERROR_CODE

```json
0000 Everything is ok
```

```json
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
1014 table not found
1015 restaurant_name can not be null(just for web)
1016 permission denied 
1017 menu_payload can not be null(just for web)
```


## User Account


### login

`/user/login`

**request** `POST`

```json
{
	"password":"this is a password", 
	"username":"this is a username"
}
```

**response** 

```json
{
	"status":ERROR_CODE
} 
```

or 

```json
{
  "data": {
    "age": null,
    "avatar": null,
    "gender": null,
    "id": 1,
    "name": "sss",
    "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ5ODI0Mjc5NywiaWF0IjoxNDkyMjQyNzk3fQ.eyJpZCI6MX0.7EFwSyWPNVsDyZhA8Hhj4yzqOK7FfRhIyEaeLtQ-fnw"
  },
  "status": 0
}
```

**You should set the `token` into HTTP header using key-value `token:TOKEN_STRING` to access following resource**


### register

`/user/register`

**request** `POST`

```json
{
	"name": "daming",
    "password": "456"
}
```

**response**

```json
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
```

### explore all orders
`/user/order/`

**request** `GET`

**response**

```json
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
```
​	


## Table 

### explore all tables
`/table/`

**request** `GET`

**response**

```json
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
```

### free table
`/table/free`

**request** `POST` `Admin`

```json
{
	"table_id":1
}
```

**response**

```json
{
	'status':0
}
```

## Menu

### explore all menus

`/menu/`

**request** `GET`

**reponse** 

```json
{
  "data": [
    {
      "category": "面食",
      "category_id": 2,
      "id": 1,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_7926ec20-dd34-11e5-bfb9-cfe874d78ed7/banner_img_1459825668511.jpg",
      "name": "Andrew Nason",
      "price": 10
    },
    {
      "category": "汤饭",
      "category_id": 4,
      "id": 2,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_-KCIu2C8d0VKakRE0WS2/banner_img_1459826335108.jpg",
      "name": "Jack Kotula",
      "price": 10
    },
    {
      "category": "面食",
      "category_id": 2,
      "id": 3,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_11191720-ecde-11e5-be0c-736255f75a6a/banner_img_1459826315532.jpg",
      "name": "Shawn Luckett",
      "price": 10
    },
    {
      "category": "汤饭",
      "category_id": 4,
      "id": 4,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_-KDMAcL0eOHqveMxdZ5Z/banner_img_1463520112187.jpg",
      "name": "Lawrence Barnes",
      "price": 10
    },
    {
      "category": "炒饭",
      "category_id": 3,
      "id": 5,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_0a870340-f96d-11e5-995c-1f7a52dfd439/banner_img_1459668323686.jpg",
      "name": "Christopher Steele",
      "price": 10
    },
    {
      "category": "炒饭",
      "category_id": 3,
      "id": 6,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_1ca204f0-f99d-11e5-9596-f1927f4bd785/banner_img_1459763801650.jpg",
      "name": "Benjamin Ehlers",
      "price": 10
    },
    {
      "category": "面食",
      "category_id": 2,
      "id": 7,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_470418e0-fc8c-11e5-9952-253f4304608b/banner_img_1460036239140.jpg",
      "name": "Vicki Richards",
      "price": 10
    },
    {
      "category": "汤饭",
      "category_id": 4,
      "id": 8,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_0720b1e0-0130-11e6-b9ce-ffaedafbed0a/banner_img_1460525692417.jpg",
      "name": "Rosa Childers",
      "price": 10
    },
    {
      "category": "炒饭",
      "category_id": 3,
      "id": 9,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_90d5e690-0562-11e6-91ae-416a68add056/banner_img_1460983583593.jpg",
      "name": "George Rambo",
      "price": 10
    },
    {
      "category": "今日推荐",
      "category_id": 0,
      "id": 10,
      "image": "http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_b9bf8c40-0dec-11e6-96d3-9b6ed08c86ad/banner_img_1461924473392.jpg",
      "name": "Tammy Dunkle",
      "price": 10
    }
  ],
  "status": 0
}
```

## Order

### create order
`order/create`

**request** `POST`

```json
{
  "table_id" : 2,
  "menus_id" : 1,3,4 # string, separate with ','
}
```

**response**

```json
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
```

### fetch order detail by id

**request** `POST`

```json
{
	"order_id":23
}
```

**response**

```json
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
```

## Admin

### login

`/admin/login`

**request** `POST`

```json
{
	"password":"this is a password", 
	"username":"this is a username"
}
```

**response** 

```json
{
	"status":ERROR_CODE
} 
```

or 

```json
{
  "data": {
    "age": null,
    "avatar": null,
    "gender": null,
    "id": 1,
    "name": "sss",
    "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ5ODI0Mjc5NywiaWF0IjoxNDkyMjQyNzk3fQ.eyJpZCI6MX0.7EFwSyWPNVsDyZhA8Hhj4yzqOK7FfRhIyEaeLtQ-fnw"
  },
  "status": 0
}
```
