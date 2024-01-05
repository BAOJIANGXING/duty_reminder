# DutyReminder

#### 介绍

主要用于值班人员微信提醒。

```bash
1、支持多组提醒
2、支持日志
```

#### 软件架构
软件使用python3编写。

#### 安装教程
1、修改配置

```bash
config.ini中修改配置，多组提醒[Personx]配置，以Personx开始，如Person1...Person10等
```
默认读取config.ini，可以使用-c 指定配置文件。

#### 使用说明
手动执行
  
可以根据需求使用解释器运行，或者使用dist中打包后的可执行文件运行
  
1、使用python3解释器运行
```bash
pip3 install -r requirements.txt 
python3 main.py
```

2、使用dist中可执行文件运行
```bash
chmod +x duty_reminder 
./duty_reminder
```

定时执行

例如： 每日早上6点提醒当天值班人员，晚上9点提醒明天值班人员。
```bash
crontab -e 
00 06,21 * * *  cd /data/scripts/duty_reminder/&&./duty_reminder
```


#### 参数
```bash
-v 查看版本信息
-c 指定配置文件
```