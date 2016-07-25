### 扩充
考虑到对特定网站的限频，我对httproxy进行扩充

```
[main]
host = localhost
port = 8011
logfile = /Users/ambv/.httproxy/log
pidfile = /Users/ambv/.httproxy/pid
daemon = yes
verbose = yes

[allowed-clients]
localhost
192.168.0.1

[limit-frequency]
news.baidu.com = 100

```
目前的限制是以分钟计数, 如上面所示的例子
使用该代理节点对news.baidu.com的访问频次限制是每分钟100次
