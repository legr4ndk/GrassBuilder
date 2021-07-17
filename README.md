# GrassBuilder 生草机
## 简介
本程序可以实现在各大网站都很有名的梗：把xx用翻译软件翻译20遍。

本程序需要可靠的网络连接，python库需要`time`, `requests`, `hashlib`, `urllib`, `random`, `json`

本软件依靠百度翻译。你只需要运行main.py然后输入你要用来生草的文本（语言不限），然后它就会在28种语言间随机互相翻译20次，再把最后结果翻译成中文。

真的很草（

## 怎么使用

你只要去申请一个免费的[百度翻译API](https://api.fanyi.baidu.com/product/11) （真的很方便）然后把你得到的Appid和密钥填在源代码里就行了。

输出大约是这样的：
```
WELCOME TO GRASS BUILDER
WHAT GRASS DO YOU WANT TO GET
美的，掌握核心科技。
YOU MIGHT HAVE TO WAIT 20s TO GET YOUR GRASS
THIS TIME'S QUERY: Midea, ovládni základní technologii.
THIS TIME'S QUERY: Midea, κατέχεις τη βασική τεχνολογία.
THIS TIME'S QUERY: Beau, tu as la technologie de base.
THIS TIME'S QUERY: Бо, у тебя есть основные технологии.
THIS TIME'S QUERY: Bo, cậu có kỹ năng cơ bản.
THIS TIME'S QUERY: Bo, máš základní schopnosti.
THIS TIME'S QUERY: 波，你有基本嘅散手。
THIS TIME'S QUERY: Bo, tu as les mains libres de base.
THIS TIME'S QUERY: Bo, máš základní funkci bez rukou.
THIS TIME'S QUERY: Bo, du hast eine grundlegende Funktion ohne Hände.
THIS TIME'S QUERY: Bo, sul on põhiülesanne ilma käteta.
THIS TIME'S QUERY: Μπο, έχεις την κύρια αποστολή χωρίς τα χέρια σου.
THIS TIME'S QUERY: Bo, du har huvuduppdraget utan dina händer.
THIS TIME'S QUERY: Bo, tu peux accomplir la tâche principale sans tes mains.
THIS TIME'S QUERY: Bo, você Pode terminar a tarefa principal SEM as mãos.
THIS TIME'S QUERY: Бо, можеш да свършиш основната задача без ръце.
THIS TIME'S QUERY: 波，唔使你手就可以完成主要任务。
THIS TIME'S QUERY: Помаши, пожалуйста, чтобы ваша рука могла выполнить главную задачу.
THIS TIME'S QUERY: 挥手，唔该畀你只手，主要完成任务。
THIS TIME'S QUERY: Vilkuta, älä auta, lähinnä suorittamaan tehtävä loppuun.
THIS IS YOUR GRASS: 
挥挥手，不帮忙，主要完成任务。
```

### have fun
