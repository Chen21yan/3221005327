import unittest
import numpy as np
import paper_check
import main

class MyTestCase(unittest.TestCase):

    # 测试读取空文件
    def test_read_empty_file(self):
        orig_path = ""
        orig_add_path = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_add.txt"
        paper_check.file_handle(orig_path, orig_add_path)

    # 测试读取不存在的文件
    def test_read_notExist_file(self):
        orig_path = "C:/Users/11708/Desktop/cnki/test_text/orig_add.txt"
        orig_add_path = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_add.txt"
        paper_check.file_handle(orig_path, orig_add_path)

    # 测试读取的文件能否过滤标点符号
    def test_filter_dot(self):
        orig_path = "C:/Users/11708/Desktop/cnki/test_text/orig.txt"
        orig_add_path = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_add.txt"
        orig_file, orig_add_file = paper_check.file_handle(orig_path, orig_add_path)
        print(orig_file, orig_add_file)

    # 测试文件内容分词效果
    def test_segment(self):
        orig_path = "C:/Users/11708/Desktop/cnki/test_text/orig.txt"
        orig_add_path = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_add.txt"
        orig_file, orig_add_file = paper_check.file_handle(orig_path, orig_add_path)
        orig_string, orig_add_string = paper_check.segment(orig_file, orig_add_file)
        print(orig_string, orig_add_string)

    # 测试分词向量化效果
    def test_vectorize(self):
        orig_string = '今天 星期天 天气 晴 舒适 看电影'
        orig_add_string = '今日 周天 天气 晴朗 愉快 看小说'
        vector1, vector2 = paper_check.vector_transform(orig_string, orig_add_string)
        print(vector1, vector2)

    # 测试余弦相似度计算
    def test_calculate_cos_similarity(self):
        vector1 = np.array([1, 2, 3, 4, 5, 6])
        vector2 = np.array([1, 2, 3, 4, 5, 6])
        similarity = paper_check.calculate_cos_similarity(vector1, vector2)
        print(similarity)

    # 测试输出结果到指定文件中
    def test_save_file(self):
        answer_path = "C:/Users/11708/Desktop/cnki/test_text/result02.txt"
        result = 0.86748569623
        similarity = paper_check.save_file(answer_path, result)
        print(similarity)

    # 测试输出结果到不存在文件中
    def test_save_not_exist_file(self):
        answer_path = ""
        result = 0.86748569623
        similarity = paper_check.save_file(answer_path, result)
        print(similarity)

    # 测试输出的结果不是浮点型
    def test_result_not_float(self):
        answer_path = "C:/Users/11708/Desktop/cnki/test_text/result03.txt"
        result = 2
        answer = paper_check.save_file(answer_path, result)
        print(answer)

    # 测试文章查重
    def test_paper_checked(self):
        main.paper_checked()


if __name__ == '__main__':
    unittest.main()