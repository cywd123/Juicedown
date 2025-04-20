import vdf
import os

os.system("cls")
os.system("title JuiceDown - by 凉拌乌贼娘")
os.system("color 0A")
print("""
     _       _          ____                      
    | |_   _(_) ___ ___|  _ \  _____      ___ __  
 _  | | | | | |/ __/ _ \ | | |/ _ \ \ /\ / / '_ \ 
| |_| | |_| | | (_|  __/ |_| | (_) \ V  V /| | | |
 \___/ \__,_|_|\___\___|____/ \___/ \_/\_/ |_| |_|
""")
      
      
print("""
作者：@凉拌乌贼娘
版本：1.0
说明：JuiceDown是一个用于下载Steam游戏的工具，支持通过 WebVPN，运用多线程技术提升下载速度，实现校内免流量高速下载。
      """)
print("说明：")
print("1.请先登录WebVPN并访问：http://juiceright-github-io-s.webvpn.stu.edu.cn:8118/post/lGBTFf1szi/ 进行获得twfid")
print("2.twfid是webvpn的临时令牌，有效期较短，过期后需要重新获取")
print("3.程序支持断点续传，下载关闭请按Ctrl+C，直接关闭程序可能会导致无法保存下载进度")
print("4.如果报错，请清除缓存：删除除了CDN.cfg、dl.exe、免流下载.exe、提取下载清单.exe的所有文件")
print("\n")
print("已知BUG：")
print("1. 下载进度卡在99% ： 请按Ctrl+C关闭程序，然后重新下载（直接关闭程序可能会导致无法保存下载进度）")
print("2. 因直接关闭程序导致下载报错的，请参见第4条说明")
print("3. 下载速骤降：SteamCDN服务器有容量限制，此时请等待一段时间后再下载")
print("\n")
print("本程序仅供学习交流使用，请勿用于商业用途，否则后果自负。WebVPN为学校服务，且用且珍惜。")
print("\n")

print("请认真阅读说明后再使用本程序\n")
os.system("pause")
os.system("cls")
id=input("请输入游戏appid：")
twfid=input("请输入twfid：")

threads=input("请输入线程数(最大128)：")
# threads最大为128
# thread转化为int
threads=int(threads)
if threads>128 or threads=="":
    threads=128
    print("线程数最大为128，已自动设置为128")
# %%
threads=str(threads)
print("下载关闭请按Ctrl+C再退出，直接关闭程序可能会导致Bug")
print("--------------------------")
all_dic={}
def addappid(depot_id,no="none", key="none"):
    if key !="none":
        tmpid=depot_id
        tmpkey=key
        tmp={"DecryptionKey":tmpkey}
        all_dic.update({tmpid:tmp})


# %%
readlines = open(id+"/"+id+".lua", "r").readlines()
for readline in readlines:
    try:
        exec(readline)
    except Exception as e:
        #print(e)
        pass

all_dic={"depots":all_dic}

# %%
with open(id+'/config.vdf', 'w') as file:
    file.write(vdf.dumps(all_dic))
comands = 'dl.exe -l ERROR -r 100 -t '+threads+' -id '+twfid

# 逐行读取CDN.txt
with open("CDN.cfg", "r") as file:
    for line in file:
        # 去掉行尾的换行符
        line = line.strip()
        # 执行命令
        comands=comands+' --server "'+line+'"'
comands=comands+' app --app-path ./'+id
        
os.system(comands)
os.system("pause")