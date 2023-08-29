Maven 是一种流行的 Java 项目管理和构建工具，它基于项目对象模型 (POM) 概念。以下是一些 Maven 的基础知识。

1. **安装 Maven**

   Maven 是一个 Java 程序，所以你需要首先安装 Java。然后你可以从 Maven 官网下载最新版的 Maven，解压后将其加入环境变量 PATH。在命令行中运行 `mvn -v`，如果正确安装，会显示 Maven 的版本信息。

2. **理解 Maven 项目结构**

   Maven 项目有一个标准的目录结构。主要的目录和文件包括：

   - `src/main/java`: 主要的 Java 代码放在这里
   - `src/main/resources`: 应用的资源文件，如配置文件，放在这里
   - `src/test/java`: 测试代码放在这里
   - `pom.xml`: Maven 的配置文件，定义了项目的基本信息和依赖

3. **理解 POM (Project Object Model)**

   `pom.xml` 文件是 Maven 项目的核心。它包括项目的基本信息（如组织ID，项目ID，版本号等）和项目的依赖。Maven 使用这个文件来解析项目的构建和依赖。

4. **Maven 依赖管理**

   Maven 可以自动处理项目的依赖。你只需要在 `pom.xml` 中添加你需要的依赖，Maven 会自动从中央仓库下载依赖和它们的子依赖。例如：

   ```xml
   <dependencies>
      <dependency>
         <groupId>junit</groupId>
         <artifactId>junit</artifactId>
         <version>4.12</version>
         <scope>test</scope>
      </dependency>
   </dependencies>
   ```

5. **Maven 生命周期和插件**

   Maven 的构建过程是由生命周期定义的，主要有三个生命周期：clean、default、site。每个生命周期都由一系列阶段（phase）组成。例如，default 生命周期包括了 compile、test、package、install 等阶段。

   插件是 Maven 的功能扩展，Maven 大部分功能都是通过插件实现的。插件一般绑定在生命周期的某个阶段，当执行到该阶段时，会执行插件的功能。

6. **使用 Maven 构建项目**

   Maven 提供了一些命令来执行生命周期的阶段。常用的命令包括：

   - `mvn clean`: 清理项目，删除 target 目录
   - `mvn compile`: 编译项目的主代码
   - `mvn test`: 运行测试
   - `mvn package`: 打包项目，例如生成 jar 或 war 文件
   - `mvn install`: 安装项目到本地仓库，供其他项目依赖
   - `mvn deploy`: 部署项目到远程仓库，供其他人使用


中央仓库 (Central Repository) 是 Maven 的默认仓库，它包含了大量的开源 Java 项目。你可以在 [http://search.maven.org/](http://search.maven.org/) 搜索你需要的依赖。

Could not find artifact org.springframework.boot:spring-boot-devtools:pom:unknown in central (https://repo.maven.apache.org/maven2) 