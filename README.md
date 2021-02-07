# **HTTPS 证书检查脚本使用说明**

## **一、** **功能说明**

该脚本可以通过输入节点VIP（支持一次输入多个VIP）自动检查该节点所有SLB设备的指定域名证书是否正常。

## **二、** **准备工作**

1. 安装python依赖包

   ```pip install -r requirements.txt```

2. 更新vip.yaml文件（更新周期视情况而定，不需要太频繁）

   需要登录117.128.7.227执行如下命令：

   ```salt '*' network.ip_addrs lo --out-file=/tmp/vip.yaml --out=yaml```

## **三、** **使用方法**

1. 将main.py 34行hostname变量修改为测试域名

![img](file:////Users/yuzhenliang/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image001.png)

2. 将main.py 35行port变量修改为测试端口

![img](file:////Users/yuzhenliang/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.png)

3. 将main.py 36行 desired_SN变量修改为期望的证书序列号

![img](file:////Users/yuzhenliang/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image003.png)

序列号获取方法如下：

> 1. 修改hosts文件，将测试域名强制解析至证书正确节点；

> 2. 使用浏览器打开测试域名的一个资源，依图示点击；

![img](file:////Users/yuzhenliang/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.png)> 

> 3. 依图示步骤，查看证书，获取序列号。

![img](file:////Users/yuzhenliang/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image005.png)>

4. 运行main.py，按照提示输入节点VIP。如下所示：

![img](file:////Users/yuzhenliang/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.png)