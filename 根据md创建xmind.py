import os
import re
def main():
    cwd = os.getcwd()
    filename = '17JWTAPI文档.md'
    md2xmind(cwd, filename)


class 一级:
    def 是否是二级(self,line):
        return re.match(r'^\s*##\s') is not None

    def __init__(self,lines):
        self.lines=lines
        self.title=lines[0]
        self.notes=[]
        self.二级s=[]
        self.二级index=[]

        for i,line in enumerate(lines):
            if self.是否是二级(line):
                self.二级index.append(i)
        # 如果没有二级
        if len(self.二级index)==0:
            self.notes.append(lines[1:])
            return

        # 将开头到第一个二级添加到notes
        self.notes.append(lines[1:self.二级index[0]])
        # 将二级index分割
        for i in range(len(self.二级index)):
            # 如果是最后一个
            if i == len(self.二级index) - 1:
                # self.二级s.append(lines[self.二级index[i]:])
                self.二级s.append(二级(lines[self.二级index[i]:]))

            else:
                # self.二级s.append(lines[self.二级index[i]:self.二级index[i + 1]])
                self.二级s.append(二级(lines[self.二级index[i]:self.二级index[i + 1]]))



class 二级:
    def 是否是子主题(self,line):
        return re.match(r'^\s*-\s') is not None

    def __init__(self,lines):
        self.lines=lines
        self.title=lines[0]
        self.notes=[]
        self.子主题s=[]
        self.子主题index=[]
        for i,line in enumerate(lines):
            if self.是否是子主题(line):
                self.子主题index.append(i)
        # 如果没有二级
        if len(self.子主题index)==0:
            self.notes.append(lines[1:])
            return

        # 将开头到第一个二级添加到notes
        self.notes.append(lines[1:self.子主题index[0]])
        # 将二级index分割
        for i in range(len(self.子主题index)):
            # 如果是最后一个
            if i == len(self.子主题index) - 1:
                # self.子主题s.append(lines[self.子主题index[i]:])
                self.子主题s.append(子主题(lines[self.子主题index[i]:]))
            else:
                # self.子主题s.append(lines[self.子主题index[i]:self.子主题index[i + 1]])
                self.子主题s.append(子主题(lines[self.子主题index[i]:self.子主题index[i + 1]]))


class 子主题:
    def __init__(self,lines):
        self.lines=lines
        self.notes=[]
        self.title=lines[0]
        self.子主题s=[]
        self.子主题index=[]
        for i,line in enumerate(lines):
            if self.是否是子主题(line):
                self.子主题index.append(i)
        # 如果没有二级
        if len(self.子主题index)==0:
            self.notes.append(lines[1:])
            return
        # 将开头到第一个二级添加到notes
        self.notes.append(lines[1:self.子主题index[0]])
        # 将二级index分割
        for i in range(len(self.子主题index)):
            # 如果是最后一个
            if i == len(self.子主题index) - 1:
                # self.子主题s.append(lines[self.子主题index[i]:])
                self.子主题s.append(子主题(lines[self.子主题index[i]:]))
            else:
                # self.子主题s.append(lines[self.子主题index[i]:self.子主题index[i + 1]])
                self.子主题s.append(子主题(lines[self.子主题index[i]:self.子主题index[i + 1]]))
    def 是否是子主题(self,line):
        return re.match(r'^\s*-\s') is not None






def md2xmind(dir,filename):
    with open(dir+'/'+filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    yiji=一级(lines)


    # 生成xmind























