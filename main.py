import sys
import paper_check

# 获取命令行参数
def get_args():
    args = []
    try:
        if len(sys.argv) < 4:
            raise ValueError
        else:
            for i in range(1, 4):
                if isinstance(sys.argv[i], str):
                    args.append(sys.argv[i])
                else:
                    raise TypeError
    except ValueError:
        print("Please enter the correct number of parameters!")
        return ValueError
    except TypeError:
        print("Please enter the correct parameter type!")
        return TypeError
    return args


def paper_checked():
    # 测试文件路径
    orig_path = "C:/Users/11708/Desktop/cnki/test_text/orig.txt"
    orig_add_path1 = "C:/Users/11708/Desktop/cnki/test_text/orig.txt"
    orig_add_path2 = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_add.txt"
    orig_add_path3 = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_del.txt"
    orig_add_path4 = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_dis_1.txt"
    orig_add_path5 = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_dis_10.txt"
    orig_add_path6 = "C:/Users/11708/Desktop/cnki/test_text/orig_0.8_dis_15.txt"
    answer_path = "C:/Users/11708/Desktop/cnki/test_text/result.txt"
    # 获取命令行参数
    # args_list = get_args()
    # orig_path, orig_add_path, answer_path = args_list[0], args_list[1], args_list[2]
    # 读取文件并过滤标点符号
    file1, file2 = paper_check.file_handle(orig_path, orig_add_path2)
    # 进行内容分词
    string1, string2 = paper_check.segment(file1, file2)
    # 分词转化为向量，降低维度分析
    orig_feature, orig_add_feature = paper_check.vector_transform(string1, string2)
    # 计算向量夹角余弦值，得余弦相似度
    result = paper_check.calculate_cos_similarity(orig_feature, orig_add_feature)
    # 将结果保存到文件中
    print(result)
    paper_check.save_file(answer_path, result)


# 主函数，程序的入口
if __name__ == '__main__':
    paper_checked()