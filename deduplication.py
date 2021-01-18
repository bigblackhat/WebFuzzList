# coding:utf-8



import sys
import os 
from time import sleep 
import linecache
import hashlib

_author = "jijue"
_version = "v1.11_[新春特别版]"

example="""     
author : %s
version : %s

example : 

# 字典重复数量查看：

    如果刚拿到一份字典，想知道有多少重复的条目，就可以使用该功能

python deduplication.py num [file]

# 两份字典去重：
    
    两份字典合并为一个list，然后去重写入一份新的字典文件中

python deduplication.py de [file1] [file2] 

# 单个字典去重

python deduplication.py set [file_path]

# 字典分割：
    
    类似于"admin:password"格式的字典
    如果想要分离成两份字典，可以用这个模式，指定用于分割的字符":"和文件名即可

python deduplication.py sp [str] [file]

# 指定目录 合并所有文件 并去重保存为一份文件

    如果拿到一份字典文件夹，里面的字典都是同一类型的，比如都是手机号码字典，或者都是php文件名的字典，觉得单个去重太费劲了就可以使用这个模式

python deduplication.py dicset [dir_path]
最后会在该目录下会生成一个名为 __The__One__File__.txt 的文件，所以如果该目录下之前已经有该文件名的文件，请提前修改，否则会被重制(我当然可以生成随机文件名，但我懒得写，就酱，下课)


# markdown 格式 简单表格生成：

    分两步：
    第一步，修改变量 mdxlsx 的值
    第二步，执行命令 python deduplication.py mdxlsx
    将会直接将符合markdown格式的表格内容打印出来


# burp intruder模块save文件提取功能：

    将文件中指定的部分内容提取出来用于进一步的攻击
    举例：
    \"Request	Payload	       Status	Error	Timeout	Length	Comment
     8445	867456899@qq.com   200	  false	false	1196	
    \"
    想要以length为参考，提取出所有length为1196的payload  
    python deduplication.py burp burp_save.txt 6 1196 2

python deduplication.py burp [filepath] [参考列位置] [参考内容] [提取内容位置(如果要提取多个字段请用","分隔)]   


# 字典文件加密功能：

    因为考虑到一些网站登陆时会对密码做一些简单的加密，比如md5(md5($pass))、md5($pass)等，所以有了这个功能  
    直接读取字典中的所有内容，加密生成新的文件(源文件不影响)  

python deduplication.py encry [filepath] [加密形式id]

    目前支持的加密形式有:
        1 : md5(md5($pass))
        2 : md5($pass)
""" % (_author,_version)



def deduplication(file1,file2):

    print "\n+-------------------------------+"

    print "字典文件 1 "+file1
    print "字典文件 2 "+file2

    if os.path.exists(file1) and os.path.exists(file2):
        ext=os.path.splitext(file1)[1]
        print "文件拓展名 "+ext

        print "\n"

        basefile1=os.path.basename(file1)
        basefile2=os.path.basename(file2)

        pathfile1=os.path.dirname(file1)

        # 相对路径下主文件也就是file1如果和本工具在同一个目录下
        # pathfile1的值就是空，如果按照else的处理经过字符拼接会直接保存到根目录，然后报错
        # IOError: [Errno 30] Read-only file system: '/test_ID_CARD.list'
        if pathfile1 == "":
            file1_2 = basefile1.split(".")[0]+"_"+basefile2.split(".")[0]+ext
        else :
            file1_2=pathfile1+"/"+basefile1.split(".")[0]+"_"+basefile2.split(".")[0]+ext
    else:
        exit("file1或file2路径不存在，请重试")


    with open(file1,"r") as f:
        list1=[i.strip() for i in f.readlines()]
        print "%s数量为%d条" % (basefile1,len(list1))
        list1=list(set(list1))
        print "%s去重后数量为%d条" % (basefile1,len(list1))

    print "\n"
    with open(file2,"r") as f:
        list2=[i.strip() for i in f.readlines()]
        print "%s数量为%d条" % (basefile2,len(list2))
        list2=list(set(list2))
        print "%s去重后数量为%d条" % (basefile2,len(list2))

    """ 
        num=0
        for i in list2:
            if not i in list1:
                list1.append(i)
                num+=1

        listnum=len(list1)
    """
    list3=set(list1+list2)
    num = len(list3) - len(list1)
    listnum = len(list3)

    print "\n去重完毕，新增%d条\n" % (num)
    # [list1.append(i) for i in list2 if not i in list1]
    # print list1
    with open(file1_2,"w") as f:
        for i in sorted(list3):
            f.write(i+"\n")

    print "排序完毕\n新字典文件保存为 "+file1_2

    print "共计%d条" % (listnum)

    print "\n+-------------------------------+\n"


def split(splitstr,splitfile):
    if os.path.exists(splitfile):
        abspath=os.path.abspath(splitfile)
        path=os.path.dirname(splitfile)
        basefile=os.path.basename(splitfile).split(".")[0]
        ext=os.path.splitext(splitfile)[1]
    else:
        exit("file not exist")

    if os.access(abspath, os.W_OK)==True:
        pass
    else:
        print "you haven't write pri"
        exit(0)
    
    fl=path+"/"+basefile+"_l"+ext
    fr=path+"/"+basefile+"_r"+ext
    try:
        file_left_object=open(fl,"w+")
        file_right_object=open(fr,"w+")
  

        with open(splitfile,"r") as f:
            num=0
            for line in f.readlines():
                # line=line.strip().split("----")[0]
                file_left_object.write(line.strip().split(splitstr)[0]+"\n")
                file_right_object.write(line.strip().split(splitstr)[1]+"\n")
                num+=1
            print "共计分割%d条" % (num)
    except:
        print "新建文件失败"
        exit(0)
    finally:
        file_left_object.close()
        file_right_object.close()
        print "生成新文件%s和%s" % (fl,fr)

def set_file(file_name):
    with open(file_name,"r") as f:
        list = [i.strip() for i in f.readlines()]
        len1_list = len(list)
        print "源文件共计%d条" % (len1_list)
        list = set(list)
        len2_list = len(list)
        len_set = len1_list - len2_list
        print "其中%d条重复，经优化有%d条保留" % (len_set,len2_list)
    with open(file_name.split(".")[0] + "_seted.txt","w") as newf:
        for i in list:
            newf.write(i+"\n")
    print "新文件保存为%s" % (file_name.split(".")[0] + "_seted.txt")

def num_file(file_path):
    """ 
    接受一个参数  
    打印字典文件总量和重复量
    """
    with open(file_path,"r") as f:
        listfile = list(i.strip() for i in f.readlines())
        len_file = len(listfile)

        listset = set(listfile)
        len_set = len(listset)

        _len_ed = len_file - len_set

        print "源文件共计%d条" % (len_file)
        print "其中共有%d条重复" % (_len_ed)
        if _len_ed != 0:
            print "可以使用 python deduplication.py set [file_path] 去重"

def dicset(dic_path):
    if os.access(dic_path,os.F_OK) and os.access(dic_path,os.R_OK) and os.access(dic_path,os.W_OK):
        os.chdir(dic_path)
        print "\n移动至目录 %s 下\n" % (dic_path)
        sleep(0.5)
    else:
        print "指定路径 %s 没有访问或读写权限，请重新确认" % (dic_path)
        exit(0)
    lists = list()
    for i in os.listdir(os.getcwd()):
        print "处理文件 %s" % (i)
        with open(i,"r") as f:
            res = f.readlines()
            newres = [i.strip() for i in res]
            newres = set(newres)
            print "处理完毕，源文件 %d 条，去重后 %d 条" % (len(res),len(newres))
        lists += newres ;sleep(0.1)
    lists = set(lists)
    print "\n所有文件处理完毕，去重后共计 %d" % (len(lists))
    _the_one_file_ = "__The__One__File__.txt"
    with open(_the_one_file_,"w") as f:
        for i in lists:
            f.write(i+"\n")
        print "\n文件保存为 %s\n" % _the_one_file_



mdxlsx = """
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.0 (protocol 2.0)
80/tcp   open  http     Tengine httpd
443/tcp  open  ssl/http Tengine httpd
3306/tcp open  mysql    MySQL 5.7.31-log
8888/tcp open  http     Ajenti http control panel
"""



def gen_markdown_xlsx(string):
    """
    接受一个多行字符串，然后将其修改为符合markdown的表格格式的字符串  
    然后打印到屏幕上  

    参数string就在上面，直接修改就好了
    """
    lis = string.strip().split("\n")
    title_len = len(lis[0].split(" "))
    title = lis[0].split(" ")
    xlsx_new = str()
    for i in title:
        xlsx_new += "|" + i
    xlsx_new += "|\n"
    xlsx_new += "|-"*title_len + "|\n"
    for i in lis[1:]:
        for o in i.split(" "):
            xlsx_new += "|%s" % (o)
        xlsx_new += "|\n"
    print xlsx_new


def burp(filenamepath,grepnum,grepstr,thenum):
    """
    burp处理主函数，主要负责将用户提供的提取参数交给burp_split函数处理，然后汇总进一个列表里  
    全部写进list文件里  
    """
    thestr_list = thenum.strip().split(",")
    sum_list = []
    for i in thestr_list:
        thestr = burp_split(filenamepath,grepnum,grepstr,i)
        sum_list.append(thestr)
    len_len = len(sum_list[0])
    sums = ""
    for i in range(len_len) :
        for f in range(len(sum_list)):
            sums += sum_list[f][i] + " "
        sums += "\n"
    with open(filenamepath+".list","w") as f:
        f.write(sums)

def burp_split(filenamepath,grepnum,grepstr,thenum):
    """
    burp处理核心函数，只负责从save文件中提取单个column内容
    """
    line_num = gen_column(filenamepath)
    grep_num = int(grepnum)
    the_num = int(thenum)
    with open(filenamepath,"r") as f:
        lines = [i.strip() for i in f.readlines()]
    thenum_pay = []
    for i in lines:
        con = i.strip().split()
        if len(con) != line_num:
            continue
        if con[grep_num-1] != grepstr:
            continue
        thenum_pay.append(con[the_num-1])
    return thenum_pay


def gen_column(filename):
    """
    获取文件中关键信息的列数  
    接受filename一个参数  
    return int : column
    """
    line_cache = linecache.getlines(filename)[4:9]
    linecache.clearcache()
    column_num = []
    for i in line_cache:
        line_i = i.strip().split()
        column_num.append(len(line_i))
    column_numadd = 0
    for i in column_num:
        column_numadd += int(i)
    # print column_numadd;print len(column_num)
    column = column_numadd/len(column_num)
    return column
# print gen_column("burp_user.txt")
# burp("burp_user.txt",8,"true","2,3")
# gen_column("phph1.txt")

# burp_split("phph1.txt",6,6,1263,2)

def _encrypt_md5_md5(one_string):
    """
    md5(md5($pass))方式加密
    """
    _md5 = hashlib.md5(one_string).hexdigest()
    _md5_md5 = hashlib.md5(_md5).hexdigest()
    return _md5_md5

def _encrypt_md5(one_string):
    """
    md5($pass)方式加密
    """
    _md5 = hashlib.md5(one_string).hexdigest()
    return _md5


# 加密列表
# 新的加密方式添加时做三步
# 第一，写加密函数
# 第二，添加函数名至下方字典
# 第三，将新增加密方式写进help
encrypt_list = {"1":"_encrypt_md5_md5","2":"_encrypt_md5"}


# print _encrypt_md5_md5("1")
def encrypt_core(filepath,enc_id):
    """
    enc_id : 类似于hashcat的使用方式，后续一定会继续增加不同的加密方式的  
    filepath : 很好理解了  
    直接生成与加密方式同名的list文件  
    """
    enc_fun = encrypt_list[str(enc_id)]
    with open(filepath,"r") as f:
        _list = [i.strip() for i in f.readlines()]
        _encry_list = []
        for i in _list:
            _encry_list.append(eval(enc_fun)(i))
    encry_filepath = filepath + "." + enc_fun + ".list"
    with open(encry_filepath,"w") as f:
        for i in _encry_list:
            f.write(i+"\n")
    print "加密文件 %s 已生成完毕" % (encry_filepath)
    # return eval(enc_fun)("1")

# encrypt_core("PassWordList/top100.txt",1)

if len(sys.argv)>1:
    if sys.argv[1] == "de" :
        deduplication(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "sp" :
        split(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "set" :
        set_file(sys.argv[2])
    elif sys.argv[1] == "num" :
        num_file(sys.argv[2])
    elif sys.argv[1] == "mdxlsx":
        gen_markdown_xlsx(mdxlsx)
    elif sys.argv[1] == "dicset":
        dicset(sys.argv[2])
    elif sys.argv[1] == "burp":
        burp(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    elif sys.argv[1] == "encry":
        encrypt_core(sys.argv[2],sys.argv[3])
    else:
        print example
        exit(0)
else:
    print example
    exit(0)