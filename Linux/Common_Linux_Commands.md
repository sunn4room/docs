# 常用 Linux 命令

## awk

```shell
awk 'pattern{ cmmands }' FILE # 默认以任意数量空格为分隔符
awk -F , 'pattern{ commands }' FILE # 自定义分隔符
awk 'BEGIN{ commands } pattern{ commands } END{ commands }' FILE

awk '$2 > 90 {print($1)}' FILE
awk '{printf("%-8s", $1)}'
```

> 友情链接：[AWK程序设计语言](https://awk.readthedocs.io/en/latest/index.html)

## cut

```shell
cut -c 3-5 # 截取
cut -b 3-5 # 以字节为单位
cut -c 3- # 截取直到末尾
cut -c -5 # 从头截取
cut -f 1,3-5 # 以制表符为间隔，截取1、3、4、5域
cut -d ' ' -f 1,3-5 # 以空格为间隔（不识别任意数量空格）
```

## grep

```shell
grep 'regex' FILE/DIR # 搜正则
grep -i 'regex' FILE/DIR # 忽略大小写
grep -v 'regex' FILE/DIR # 反转
grep -r 'regex' DIR # 递归子目录
grep -n 'regex' FILE/DIR # 显示行号
```

> 友情链接：[GNU Grep](https://www.gnu.org/software/grep/manual/grep.html)

## sed

```shell
sed 'expr' FILE # expr: range+action+content
sed 'expr; expr; ...' FILE
sed -i 'expr' FILE # 不打印直接保存
sed -n 'expr' FILE # 只打印修改过的行

sed '2p' FILE # 答应第二行，通常和-n配合使用
sed '$p' FILE # 打印最后一行
sed '2,$p' FILE # 打印第二行到最后一行
sed '/xxx/p' FILE # 打印匹配行
sed '2,/xxx/p' FILE # 打印第二行到匹配行
sed '2axxx' FILE # 第二行后添加新行
sed '2ixxx' FILE # 第二行前添加新行
sed '2cxxx' FILE # 修改第二行
sed '2d' FILE # 删除第二行
sed 's/xxx/yyy/' # 替换所有
sed 's/xxx/yyy/1' # 只替换第一个
```

> 友情链接：[GNU Sed](https://www.gnu.org/software/sed/manual/sed.html)
