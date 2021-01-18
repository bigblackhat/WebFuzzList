# WebFuzzList
该项目用于收集Web安全测试中常用的fuzz字典

本项目参考并收集了许多Github以及安全圈内的大佬的字典或项目，在此鸣谢，后续将会陆续完善底部的鸣谢清单

<br>

本人目前定期每天梳理一点，有兴趣可以先star关注一下，等到项目基本完成将会在readme上告知

<br>

另外我还制作了一款字典去重工具--```deduplication.py```，有兴趣自取

<br>

* 2020-12-12 webdiclist目录文件去重完毕，去重脚本deduplocation.py进行了bug修复，支持千万级大字典

* 2020-12-14 整理了国人姓名字典，包含全拼和首字母简写，big是little和middle优化后结合的。另外新添加了脚本deduplication.py的单个字典去重功能，过程中发现随着功能添加有代码重复现象，预计短期内会做一些小的调整和优化(因为这几天在读jexboss的源码，加上去重脚本本身的量级还没到需要大改的地步)

* 2020-12-15 UserNameList目录文件去重整理完毕，deduplication.py脚本新增重复数量查看功能，检查了一遍ParamList目录，文件内容都很nice，没有重复项

* 2020-12-16 SaiDict 全部处理完毕，后续会将其他字典加入项目

* 2020-12-16 因为一些特殊原因之前的库删掉了，重建该项目，下一步会将kali自带字典纳入本项目，敬请期待

* 2020-12-18 去重脚本新增针对整个文件夹内所有文件合并去重功能，详情见脚本的help

* 2021-1-3 更新了一下去重脚本，修复了一个de模式下file1与脚本处于同一个目录会导致保存失败的bug，新增了top100的密码字典，并会逐步完善每个目录下的readme文件，方便于对不同字典的用途的定位，之后应该会添加一个新的功能--将burp intruder模块的扫描结果摘要处理。然后将脚本中的一些变量和函数规范整合一下，作为2021新春特别版发布。

~~TODO 去重脚本添加对指定目录中所有文件进行合并去重整合为一份文件的功能，de参数更适合精细处理，但拿到一个大字典文件夹时，如果一个一个的去重太累人了~~

* 2021-1-11 更新脚本，添加了burp的intruder模块save结果的摘要功能

* 2021-1-12 更新脚本，修复了对文件column的判断错误导致摘要导出文件内容为空的bug(坑边闲话，最近三刷权游，外面冰雪漫天，家中刷剧火锅，就很nice，权8真是一坨屎，毁掉了我喜欢的所有人^_^)

* 2021-1-18 更新脚本，新增encrypt模块，处于一些网站在将密码传递给后端时会将密码进行简单加密，比如sha256、md5、md5(md5)等，这个模块就是将已有的密码文件通过指定模式进行加密生成新的文件。当然了有的网站会通过请求新的url获取某token随机值作为salt来加密（或者是其他的法子，自己看js源码去吧哈哈哈）不在本工具考虑范围中，因为每次salt都是随机的嘛，这需要自行写脚本。目前只做了md5和md5(md5)两种，因为我最近日站刚好碰上了这两种，就写了，后面遇到别的再填吧  

TODO 添加字典分割功能，也是在自己爆破的时候突发奇想的(偶遇某小破站，只要连接数量过多就会报429错误，所以个人觉得如果将大字典分段测试或许会好一点，当时需要容忍漫长的等待)，目前想法还不成熟，理由也不充分，先放这儿吧，等时机成熟就添加这个功能

TODO 把kali字典尽快处理完
TODO nikto官网提供的默认字典

<!-- 
## ParamList

<br>

### Arjun
https://github.com/s0md3v/Arjun


<br>
<br>
<br>

## SubDomainList

|字典||
|-|-|
|main.txt|从subDomainsBrute,layer等工具中提取出来合并去重，再和自己生成的部分字典合并|
|||


<br>
<br>

## WebDicList

### phpFilePath

### aspFilePath

### jspFilePath

### vulPath



<br>
<br>
<br>

## XssPayloadList


<br>
<br>


## UserNameList
<br>
<br>

## PassWordList


### RW_Password
https://github.com/r35tart/RW_Password



### WifiPassList
猪猪侠师傅的wifi_top2000_passwd.txt

### MiddleList  

<br>
<br>
<br>
<br> -->

# 致敬鸣谢

以下没有排名先后，仅根据我整理项目时的时间顺序依次向下排列  

|项目地址|
|-|
|[Stardustsky/SaiDict](https://github.com/Stardustsky/SaiDict)|
|[TheKingOfDuck/fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)|
|[Stardustsky/SaiDict](https://github.com/Stardustsky/SaiDict)|
|[tennc/fuzzdb](https://github.com/tennc/fuzzdb)|
|[Default Passwords | CIRT.net](https://cirt.net/passwords?criteria=tomcat)|
