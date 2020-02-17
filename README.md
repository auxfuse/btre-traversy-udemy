# Python Django Dev to Deployment with Brad Traversy

Follow along Video tutorial series on <a href="https://www.udemy.com/course/python-django-dev-to-deployment/">Udemy.</a>

# Planning the Schemas

## MODEL/DB Fields

### Listing Table:

|Field name:            |Field Type:                |
|:---------------------:|:-------------------------:|
|id                     |INT                        |
|realtor                |INT (fk [realtor model])   |
|title                  |STR                        |
|address                |STR                        |
|city                   |STR                        |
|state                  |STR                        |
|zipcode                |STR                        |
|description            |TEXT                       |
|price                  |INT                        |
|bedrooms               |INT                        |
|bathrooms              |INT                        |
|garage                 |INT def[0]                 |
|sqft                   |INT                        |
|lot_size               |FLOAT                      |
|is_published           |BOOL def[True]             |
|list_date              |DATE                       |
|photo_main             |STR                        |
|photo_1                |STR                        |
|photo_2                |STR                        |
|photo_3                |STR                        |
|photo_4                |STR                        |
|photo_5                |STR                        |
|photo_6                |STR                        |

### Realtor Table:

|Field name:            |Field Type:                |
|:---------------------:|:-------------------------:|
|id                     |INT                        |
|name                   |STR                        |
|photo                  |STR                        |
|description            |TEXT                       |
|email                  |STR                        |
|phone                  |STR                        |
|is_mvp                 |BOOL def[false]            |
|hire_date              |DATE                       |

### Contact Table:

|Field name:            |Field Type:                |
|:---------------------:|:-------------------------:|
|id                     |INT                        |
|user_id                |INT                        |
|listing                |INT                        |
|listing_id             |INT                        |
|name                   |STR                        |
|email                  |STR                        |
|phone                  |STR                        |
|message                |TEXT                       |
|contact_date           |DATE                       |