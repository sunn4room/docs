# 编写 Shell 脚本

## 变量

### Bash 变量处理

```shell
dummy="abc/def/ghi/jkl/mno"
echo ${#dummy} # 18
echo ${dummy:8} # ghi/jkl/mno
echo ${dummy:0-8} # /jkl/mno
echo ${dummy:8:3} # ghi
echo ${dummy#*/} # def/ghi/jkl/mno
echo ${dummy##*/} # mno
echo ${dummy%/*} # abc/def/ghi/jkl
echo ${dummy%%/*} # abc
```


