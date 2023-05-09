import logging
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    from_number = req.params.get('From')
    to_number = "9866715527"
    CallerId_number = "04048215409"
    if not from_number:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            action = req_body['queryResult']['intent']['displayName']
            if(action == 'call_cst_phone'):
                from_number = req_body['queryResult']['parameters']['phone_number']


    if from_number and to_number and CallerId_number:

        payload={}
        headers = {}

        response = requests.request("POST", "https://id:secretkey@api.exotel.com/v1/Accounts/eunimart1/Calls/connect?From={}&To={}&CallerId={}".format(from_number,to_number,CallerId_number), headers=headers, data=payload)
        return func.HttpResponse("Success")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass all mandatory fields",
             status_code=200
        )
