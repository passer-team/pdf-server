import os

def test_puppeter():
    # os.system('node tests/test_node.js p1 p2')
    html_path = '/home/ziqiang_xu/Seafile/LiverDataExample\(12\)/selected/01190626V001/report/resources/report.html'
    os.system(f'node pdf.js {html_path} report.pdf')
    # r = os.popen('node tests/test_node.js p1 p2')
    # res = r.read()
    # r.close()
    # print(res)
