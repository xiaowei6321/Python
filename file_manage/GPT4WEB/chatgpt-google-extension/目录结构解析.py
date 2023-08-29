import os

# 获取当前脚本所在目录
path=os.path.dirname(os.path.realpath(__file__))
#print(path)
#print(__file__)

# 返回指定目录下的所有文件和目录名
dirs = os.listdir(path)
#print(dirs)

import openai
openai.api_key="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"
text=', '.join(dirs)
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-0613',
    messages=[{
        "role": "system",
        "content": f"用猫娘语气简要说明[{text}]"
    }]
)

print(response.choices[0].message.content)

'''
这个仓库是一个由Tailwind CSS实现的静态网页模板。下面是仓库的目录结构：

- `.eslintrc.json`：ESLint配置文件，用于规范JavaScript代码。
- `.git`：Git版本控制信息，用于记录各个版本的代码修改历史。
- `.github`：Github配置文件夹，包含CI/CD、自动化流程等相关配置。
- `.gitignore`：指定哪些文件或目录不会被Git跟踪。
- `.husky`：Git钩子配置文件夹，用于在代码提交或其他操作前执行相关命令。
- `.prettierignore`：指定哪些文件或目录不会被Prettier格式化。
- `.prettierrc`：Prettier配置文件，用于格式化代码风格。
- `build.mjs`：构建脚本文件，用于将源代码打包为可发布的静态网页。
- `LICENSE`：开源许可证文件，规定了代码的使用权限和限制。
- `package-lock.json`：记录项目依赖包的精确版本号和依赖关系。
- `package.json`：项目元数据文件，包含开发脚本、依赖包、作者等信息。
- `README.md`：项目说明文档，介绍了项目的功能、使用方式等信息。
- `screenshots`：存放项目截图的文件夹。
- `src`：存放源代码的文件夹。
- `tailwind.config.cjs`：Tailwind CSS配置文件，用于自定义配置主题和样式。
- `tsconfig.json`：TypeScript配置文件，用于配置TypeScript项目的编译选项。
- `添加js注释.py`：Python脚本文件，用于向源代码添加注释。
- `目录结构解析.py`：Python脚本文件，用于解析并输出项目的目录结构。

希望这些信息可以帮助你快速了解这个仓库！

Process finished with exit code 0

'''