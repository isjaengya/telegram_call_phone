# telegram_call_phone

首先登录my.telegram.org, 点击 API development tools, 并在上面注册一个应用

![登录](/pic/my_telegram_login.png)
![验证码](/pic/telegram_code.png)
![应用的详细信息](/pic/my_telegram_apps_info.png)

找到自己的appid apphash之后替换代码里面的值, 把代码拷贝到docker里面, 初次需要登录, 之后直接python example.py 即可

查看需要拨打电话的用户名
![查看需要拨打电话的用户名](/pic/call_user_name.png)

初次运行需要登录, 生成一个session文件(如果没有session即可认为为初次登录)，以后运行使用这个session文件确认用户身份
初次运行界面
![初次运行界面](/pic/code_login.png)

输入完验证码之后telegram会提示该账号在某一个ip登录
![输入完验证码之后telegram会提示该账号在某一个ip登录](/pic/code_login_code.png)

出现语弹框
![出现语弹框](/pic/telegram_phone_call.png)

更换语音通话内容(对方接听之后听到的内容) (docker里面已经安装ffmpeg)
```
ffmpeg -i input.mp3 -f s16le -ac 1 -ar 48000 -acodec pcm_s16le input.raw  # encode
ffmpeg -f s16le -ac 1 -ar 48000 -acodec pcm_s16le -i output.raw output.mp3  # decode
```







