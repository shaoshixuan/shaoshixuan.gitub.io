import json
# from flask import Flask, request, render_template
# import pandas as pd
# from scipy import stats
# import numpy as np

# app = Flask(__name__)


# app = Flask(__name__,
#            template_folder='./static',
#            static_folder='./static',
#            static_url_path="")
# with open('D:/dataview/Data-Mining-project/model.json','r') as json_file:
#     json0 = json.load(json_file)
#     for i in range(len(json0)):
#         score_main = json0[i]
#         print(score_main)
#         activated_core_user_scored = score_main.get['activated_core_user_score']
#
#         # 计算平均值
#         average = sum(activated_core_user_scored) / len(activated_core_user_scored)
#
#     print(score_main_avg)
#     print(json.dumps(json0,indent=4))

#
# @app.route('/')
# def test_index():
#     # diab = datasets.load_iris()
#     #
#     # x1 = [item[0] for item in diab.data]
#     # gkde = stats.gaussian_kde(dataset=x1)
#     # x = np.linspace(start=4, stop=8, num=200)
#     #
#     # y = gkde.evaluate(x)
#
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=25001)