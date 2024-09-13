import json 
def split_into_pages(data, page_size):
    # Dùng list comprehension để chia mảng thành các phần nhỏ
    return [data[i:i + page_size] for i in range(0, len(data), page_size)]

with open('chuyen_khoan.json', 'r') as file:
    data = json.load(file)




from flask import Flask, request, jsonify

app = Flask(__name__)


# Điểm cuối để lấy danh sách người dùng
@app.route('/pages/<int:num>', methods=['GET'])
def get_data(num):
    pages = split_into_pages(data['data'], 20)
    return jsonify(pages[num-1])
@app.route('/search/<string:keyword>', methods=['GET'])
def get_dt(keyword):
    ky = [i for i in data['data'] if keyword.lower() in i['detail'].lower()]
    return jsonify(ky)
@app.route('/sortbyMoney/pages/<int:num_pages>',methods = ['GET'])
def sortbyMoney(num_pages):
    sorted_list = sorted(data['data'], key=lambda x: int(x['credit']),reverse=True)
    pages = split_into_pages(sorted_list, 20)
    return jsonify(pages[num_pages -1])

if __name__ == '__main__':
    app.run(debug=True)