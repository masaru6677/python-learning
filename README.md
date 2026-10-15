# Python 学习仓库

学习 Python 的练习与项目。目标方向：AI 应用开发 / Agent。

## 项目

### 🎓 教务管理系统 (grade_manager.py)

命令行学生成绩管理程序。

**功能**
- 增删改查学生信息（姓名 + 三科成绩）
- 成绩合法性校验（0—150，非数字会提示重输）
- 班级统计：各科最高分 / 最低分 / 平均分，**并列名次全部列出**

**用到的知识**

字典嵌套、`match` 分支、自定义校验函数、`try/except ValueError`、`max` / `min` / `sum` / `len`

**运行**
```bash
   python grade_manager.py
```

### 📚 读书清单管理器 (book_manager.py)

命令行图书管理程序，数据保存在本地 JSON 文件。

**功能**
- 添加书籍（书名判空、判重，状态只能三选一）
- 删除、修改（作者 / 状态）
- 查看全部、按状态统计

**数据**

存在 books.json，用 UTF-8 编码，可以直接用记事本查看和编辑。

**用到的知识**

字典嵌套、while 循环、match 分支、函数拆分、文件读写、json 序列化、try/except 异常处理

**踩过的坑**
- in "想读" "在读" 会拼接成一个字符串，必须写成 in ("想读", "在读")
- json.dump 不加 ensure_ascii=False，中文会变成 \u4eba\u7c7b
- input() 拿到的输入必须 .strip()，否则用户多打一个空格就匹配不上

**运行**
```bash
   python book_manager.py
```

**练习**

day4_string_practice.py — 文本统计、邮箱与日期提取

notes/string_methods.md — 方法与踩坑清单
