import json

data = '''
{"messageType":1,"messageId":"648729c3c0380","transactionId":null,"timestamp":"2023-06-12 06:20:51","timezone":{"timezone_diff":4,"timezone":"Asia\/Tbilisi"},"correlationID":null,"baseDomainSignature":null,"body":{"scoreValue":0.6515819219858449,"decision":"0","decisionText":"reject","cutOffID":"295","scoreVector":{"intercept":{"Inrange":0,"Coefficient":0,"ParamValue":1},"maritalStatus":{"Inrange":1,"Coefficient":"-.1250000000000000","ParamValue":2},"gender":{"Inrange":0,"Coefficient":0,"ParamValue":1},"loanDuration":{"Inrange":0,"Coefficient":0,"ParamValue":15},"closedLoans":{"Inrange":0,"Coefficient":0,"ParamValue":1},"isInstallment":{"Inrange":0,"Coefficient":0,"ParamValue":6},"regionRisk":{"Inrange":1,"Coefficient":".1480000000000000","ParamValue":"3"},"ceiScoreValue":{"Inrange":1,"Coefficient":".6030000000000000","ParamValue":257}},"posableCreditAmount":0}}'''

parsed_data = json.loads(data)

print("Message Type:", parsed_data["messageType"])
print("Message ID:", parsed_data["messageId"])
print("Timestamp:", parsed_data["timestamp"])
print("Timezone:", parsed_data["timezone"]["timezone"])
print("Score Value:", parsed_data["body"]["scoreValue"])
print("Decision:", parsed_data["body"]["decision"])
print("Decision Text:", parsed_data["body"]["decisionText"])
print("Cutoff ID:", parsed_data["body"]["cutOffID"])
print("Score Vector:")
for key, value in parsed_data["body"]["scoreVector"].items():
    print("\t", key, ":", value)
print("Posable Credit Amount:", parsed_data["body"]["posableCreditAmount"])
print("----------------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")
data1 = '''
{"body":{"dmSessionID":"152093","pid":"55001028171","saleLineID":1,"creditAmount":800.0000,"maritalStatus":2,"gender":1,"loanDuration":12,"regionID":7,"closedLoans":1,"isInstallment":6,"intercept":1}}
'''

parsed_data1 = json.loads(data1)

print("DM Session ID:", parsed_data1["body"]["dmSessionID"])
print("PID:", parsed_data1["body"]["pid"])
print("Sale Line ID:", parsed_data1["body"]["saleLineID"])
print("Credit Amount:", parsed_data1["body"]["creditAmount"])
print("Marital Status:", parsed_data1["body"]["maritalStatus"])
print("Gender:", parsed_data1["body"]["gender"])
print("Loan Duration:", parsed_data1["body"]["loanDuration"])
print("Region ID:", parsed_data1["body"]["regionID"])
print("Closed Loans:", parsed_data1["body"]["closedLoans"])
print("Is Installment:", parsed_data1["body"]["isInstallment"])
print("Intercept:", parsed_data1["body"]["intercept"])
for i, j in parsed_data1["body"].items():
    print("\t", i, ":", j)
print("Posible Credit Amount:", parsed_data1["body"]["creditAmount"])
