# Benefit Service
Jika ada pertanyaan, langsung tanya di discord #questions / tag @ProjectLeader(s)
Jika dirasa perlu menambah service lain silahkan
## Request: Fetch Data Benefit
![GET](https://badgen.net/badge/Method/GET/green)<span style="padding:10px">**/api/benefit**</span>


### Responses:
#### Fetch Data Benefit
![OK](https://badgen.net/badge/OK/200/green)
```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Benefit 1",
            "description": "all product",
            "point_required": 100,
            "discount": 10
        },
        {
            "id": 2,
            "name": "Benefit 2",
            "description": "all product",
            "point_required": 200,
            "discount": 20
        }
    ]
}
```

<br>
## Request: Benefit data entry
![POST](https://badgen.net/badge/Method/POST/yellow)<span style="padding:10px">**/api/benefit**</span>

```json
{
    "name": "Benefit 1",
    "description": "all product",
    "point_required": 100,
    "discount": 10
}
```

### Responses:
#### Benefit data entry
![Created](https://badgen.net/badge/Created/201/green)
```json
{
    "status": "success",
    "message": "Benefit created successfully",
    "data": {
        "id_benefit": 1,
        "name": "Benefit 1",
        "description": "all product",
        "point_required": 100,
        "discount": 10
    }
}
```

<br>
## Request: Check the availability of benefits data
![GET](https://badgen.net/badge/Method/GET/green)<span style="padding:10px">**/api/benefit/`<int:benefit_id>`**</span>


### Responses:
#### Check the availability of benefits data
![OK](https://badgen.net/badge/OK/200/green)
```json
{
    "status": "success",
    "data": {
        "id_benefit": 1,
        "name": "Benefit 1",
        "description": "all product",
        "point_required": 100,
        "discount": 10
    }
}
```
#### Checking the availability of Benefit not found data
![Not Found](https://badgen.net/badge/Not Found/404/red)
```json
{
    "status": "error",
    "message": "Benefit not found"
}
```

<br>
## Request: Edit Benefit Data
![PUT](https://badgen.net/badge/Method/PUT/blue)<span style="padding:10px">**/api/benefit/`<int:benefit_id>`**</span>

```json
{
    "name": "Gebyar Diskon",
    "description": "Spesial 11/11",
    "point_required": 150,
    "discount": 20
}
```

### Responses:
#### Edit Benefit Data
![OK](https://badgen.net/badge/OK/200/green)
```json
{
    "status": "success",
    "message": "Benefit updated successfully",
    "data": {
        "id_benefit": 1,
        "name": "Gebyar Diskon",
        "description": "Spesial 11/11",
        "point_required": 150,
        "discount": 20
    }
}
```
#### Edit Benefit Data (Benefit Not Found)
![Not Found](https://badgen.net/badge/Not Found/404/red)
```json
{
    "status": "error",
    "message": "Benefit not found"
}
```

<br>

