import openpyxl
import json
import os
import requests
from datetime import datetime

ProductURL = r""
CategoryURL = r""
token:str = ''


def loadData(sheet):
    rows = list(sheet.iter_rows(values_only=True))
    if not rows:
        return []
    headers = rows[0] 
    data_list = []
    for row in rows[1:]:
        row_dict = {headers[i]: row[i] or '' for i in range(len(headers))}
        data_list.append(row_dict)
    return data_list

def postApi(url,payload):
    headers = { 
        "sec-ch-ua-platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "DNT": "1",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?0",
        "authorization": f'Bearer {token}'
    }
    body = json.dumps(payload)
    try:
        response = requests.post(url,data=body,headers=headers)
        return response.json()
    except Exception as e:
        print(str(e))


def getToken(username:str, password:str):
    headers = { 
        "sec-ch-ua-platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "DNT": "1",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?0",
    }
    payload = {"Email": f'{username}',"Password": f"{password}"}
    body = json.dumps(payload)
    try:
        url = ""
        response = requests.post(url, data=body, headers=headers)
        return response.json()
    except Exception as e:
        print(str(e))


def main():
    global token

    try:
        currDir = os.path.dirname(__file__)
        inputjsonPath = os.path.join(currDir,'input.json')
        with open(inputjsonPath, 'r', encoding='Utf-8') as f:
            data = json.load(f)
            excelname = data.get('fileName', '')
            username = data.get('username', '')
            password = data.get('password', '')
            if(excelname == ""):
                print("Invalid File Name")
                return
            excelFilePath = os.path.join(currDir, excelname)
            wb = openpyxl.load_workbook(excelFilePath)
            category_sheet = wb['category']
            products_sheet = wb['products']

            categorys = loadData(category_sheet)
            products = loadData(products_sheet)

            signInResponse = getToken(username,password)
            status = signInResponse.get('status')
            if(status):
                token = signInResponse.get('responseData', {}).get('token','')
                for value in categorys:
                    value['InventoryCategId'] = 0
                    postApi(CategoryURL,value)
                for value in products:
                    value['InventoryId'] = 0
                    # value['InventoryCategId'] = 0
                    value['Sku'] = ''
                    value['productImage'] = ''
                    value['IsActive'] = True
                    dt = datetime.today().isoformat()
                    value['CreatedAt'] = dt
                    value['CreatedBy'] = 0
                    value['BranchId'] = 1
                    postApi(ProductURL,value)

            else:
                print(token = signInResponse.get('message', 'error'))

    except FileNotFoundError:
        print(f"{inputjsonPath} file not found in the root path")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
main()