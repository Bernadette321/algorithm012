
# 学习笔记
### 泛型递归

想象盗梦空间

+ 向下进入到不同梦境中; 向上又回到原来一层 --> "归去来兮"
+ 通过声音同步回到上一层 --> 用参数来进行函数不同层之间的传递变量
+ ...

##### 代码模板

```
template: 
1.terminator递归终结条件 
2.process处理当前层逻辑
3.drill down下探到下一层
4.reverse states清理当前层
```

##### 思维要点

```
1. 不要人肉递归
2. 最近重复子问题
3. 数学归纳法
```

### 分治,回溯

是特殊的递归

##### 分治代码模板

```
template: 
1.terminator, 
2.process(split your big problem) 看如何把这个大问题分成子问题
3.drill down(调用函数去做subproblems), merge(subresult) 
4.reverse states
```

与泛型递归的不同点: 这些子结果要再进行一次**组合**

**回溯模板**使用泛型递归模板
