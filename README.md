# superset-development
- remote server login development on top of superset
- blog that show how things come: https://www.jianshu.com/p/063ccb8e2a75
- This was based on superset version: 0.26.2, in the newer version
- you can prepare and start this login snippets by running https://github.com/yamyamyuo/superset-development/blob/master/sbin/start_conf_script.sh
- if you are all set, you will jump to this page once superset server is up.

<img
  src="https://github.com/yamyamyuo/superset-development/blob/master/Screen%20Shot%202018-10-25%20at%202.01.49%20PM.png"
  alt="login page"
  width="500"
/>



## Superset集成JPT 账号 发布步骤
```
# 1. 新增环境变量，SUPERSET_ROOT_DIR 根据实际环境调整
vi ~/.bashrc 
export SUPERSET_ROOT_DIR=/usr/local/lib/python3.6/site-packages
export SUPERSET_CONFIG_PATH="$SUPERSET_ROOT_DIR/conf/superset_config.py"
export PYTHONPATH=$SUPERSET_ROOT_DIR


# 2. 替换security/remote_server_api.py 中 server_url = "http://192.168.101.130" 替换真实JPT环境地址

# 3. 把conf, security 目录和文件复制到 SUPERSET_ROOT_DIR 目录下

# 4. 在 $SUPERSET_ROOT_DIR/superset/templates/appbuilder/general 目录下新建 security 目录并复制login_my.html 文件

# 5. 重启服务

```