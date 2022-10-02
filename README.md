# Project: HeadwayProgream


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 

  

### Description: 

- Using KpiService via django

  

### Utilities names: 

- Service Name: `djangotask` 

- Table Name in Database: `task1` 


  

### Requirements 

- Python 3.x 

- Django==4.1.1 

- mysql-connector-python 

         

### Contents 

The project have a structure as below: 



*  Main Files Description 

 

`manage.py` manage file to manage the django file 


How To Run 

you need to run the server by using this command
```bash 
python manage.py --runserver 
``` 
### server urls:
https://localhost/kpi_app/kpi_info ``used to create a new kpi equation and get all the current kpi equations``

https://localhost/kpi_app/kpi_link_device ``used to link kpi equation to an asset(device) so that when a new message is sent it emurates all the equations that contains the same asset as the id``

https://localhost/kpi_app/send_message ``used to send a message as json and get the results example '{"asset_id": "123", "attribute_id": "#", "timestamp": "2022-07-31T23:28:37Z[UTC]", "value": 1}'``



