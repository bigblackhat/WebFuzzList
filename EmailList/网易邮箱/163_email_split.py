# coding:utf-8
""" 
这个脚本是用来把撞库文件里面的账号和密码分离出来的，因为考虑到只需要账号或密码的场景
 """
//分别是用于存储账号和密码的文件
fe=open("163_email.txt","w")
fp=open("163_pass.txt","w")

with open("网易邮箱撞库.txt","r") as f:
    for line in f.readlines():
        # line=line.strip().split("----")[0]
        fe.write(line.strip().split("----")[0]+"\n")
        fp.write(line.strip().split("----")[1]+"\n")

f.close()
fe.close()
fp.close()
