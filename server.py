from csv import list_dialects
import json
from operator import truediv
from flask import Flask, abort
from aboutme import me
from mock_data import catalog  # import data
app = Flask('organika')


@app.route("/", methods=['GET'])
def home():
    return "This is home page!!"


# Creat an about endpoint to return your name


@app.route("/about", methods=['GET'])
def about():
    return me["first"] + " " + me["last"]


@app.route("/myaddress")
def address():
    return f'{me["address"]["number"]}{me["address"]["street"]}'


#####################################################
#################### API End Point ##################
#####################################################

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)


@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    # Here... Count how many products are in list catalog
    counts = len(catalog)
    return json.dumps(counts)  # return the value


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    for pro in catalog:
        if(pro["_id"] == id):
            return json.dumps(pro)
    # return json.dumps(id)
    return abort(404, " ID does not match any product")


# @app.route("/api/catalog/total", methods=["GET"])

@app.get("/api/catalog/total")
def get_total():
    # Here... Count how many products are in list catalog
    total = 0
    for prod in catalog:
        total = total + prod["price"]
    return json.dumps(total)  # return the value


@app.get("/api/products/<category>")
def get_cate(category):
    # Here... Count how many products are in list catalog
    list = []
    category = category.lower()
    for prod in catalog:
        if prod["category"].lower() == category:
            list.append(prod)
    return json.dumps(list)
   # return abort(404, "there no product")  # return the value

# get the list of category


@app.get("/api/categories")
def get_listcategory():
    list = []
    for pro in catalog:
        if pro["category"] not in list:
            list.append(pro["category"])
    return json.dumps(list)

# get the cheapest product


@app.get("/api/product/cheapest")
def get_cheapestProduct():
    #low = 20
    result = catalog[0]
    for prod in catalog:
        if prod["price"] < result["price"]:
            result = prod
    return json.dumps(result)


@app.get("/api/exercise1")
def get_exe1():
    nums = [123, 123, 654, 124, 8865, 532, 4768, 8476, 45762,
            345, -1, 234, 0, -12, -456, -123, -865, 532, 4768]
    solution = {}

    # print the lowest number
    solution["a"] = min(nums)

    # count and print how many numbers are lowe than 500
    count = 0
    listLower500 = []
    for result in nums:
        if result < 500:
            listLower500.append(result)
            count += 1
    solution["b"] = count, listLower500

    # sum and print all the negatives
    total = 0
    list_negative = []
    for result in nums:
        if result < 0:
            list_negative.append(result)
            total += result
    solution["c"] = total, list_negative

    # return the sum of numbers except negatives
    total2 = 0
    list_positive = []
    for result in nums:
        if result > 0:
            list_positive.append(result)
            total2 += result
    solution["d"] = total2, list_positive
    return json.dumps(solution)


app.run(debug=True)
