import archiver from 'archiver'
import autoprefixer from 'autoprefixer'
import * as dotenv from 'dotenv'
import esbuild from 'esbuild'
import postcssPlugin from 'esbuild-style-plugin'
import fs from 'fs-extra'
import process from 'node:process'
import tailwindcss from 'tailwindcss'

dotenv.config()

const outdir = 'build'

async function deleteOldDir() {
  await fs.remove(outdir)
}

async function runEsbuild() {
  await esbuild.build({
    entryPoints: [
      'src/content-script/index.tsx',
      'src/background/index.ts',
      'src/options/index.tsx',
      'src/popup/index.tsx',
    ],
    bundle: true,
    outdir: outdir,
    treeShaking: true,
    minify: true,
    legalComments: 'none',
    define: {
      'process.env.NODE_ENV': '"production"',
      'process.env.AXIOM_TOKEN': JSON.stringify(process.env.AXIOM_TOKEN || 'UNDEFINED'),
    },
    jsxFactory: 'h',
    jsxFragment: 'Fragment',
    jsx: 'automatic',
    loader: {
      '.png': 'dataurl',
    },
    plugins: [
      postcssPlugin({
        postcss: {
          plugins: [tailwindcss, autoprefixer],
        },
      }),
    ],
  })
}

async function zipFolder(dir) {
  const output = fs.createWriteStream(`${dir}.zip`)
  const archive = archiver('zip', {
    zlib: { level: 9 },
  })
  archive.pipe(output)
  archive.directory(dir, false)
  await archive.finalize()
}

async function copyFiles(entryPoints, targetDir) {
  await fs.ensureDir(targetDir)
  await Promise.all(
    entryPoints.map(async (entryPoint) => {
      await fs.copy(entryPoint.src, `${targetDir}/${entryPoint.dst}`)
    }),
  )
}

async function build() {
  await deleteOldDir()
  await runEsbuild()

  const commonFiles = [
    { src: 'build/content-script/index.js', dst: 'content-script.js' },
    { src: 'build/content-script/index.css', dst: 'content-script.css' },
    { src: 'build/background/index.js', dst: 'background.js' },
    { src: 'build/options/index.js', dst: 'options.js' },
    { src: 'build/options/index.css', dst: 'options.css' },
    { src: 'src/options/index.html', dst: 'options.html' },
    { src: 'build/popup/index.js', dst: 'popup.js' },
    { src: 'build/popup/index.css', dst: 'popup.css' },
    { src: 'src/popup/index.html', dst: 'popup.html' },
    { src: 'src/logo.png', dst: 'logo.png' },
    { src: 'src/_locales', dst: '_locales' },
  ]

  // chromium
  await copyFiles(
    [...commonFiles, { src: 'src/manifest.json', dst: 'manifest.json' }],
    `./${outdir}/chromium`,
  )

  await zipFolder(`./${outdir}/chromium`)

  // firefox
  await copyFiles(
    [...commonFiles, { src: 'src/manifest.v2.json', dst: 'manifest.json' }],
    `./${outdir}/firefox`,
  )

  await zipFolder(`./${outdir}/firefox`)

  console.log('Build success.')
}

build()

/*
该代码使用的是ES6模块的语法，可以在支持ES6模块的环境中运行。它使用了一些第三方库和插件来进行文件打包和处理。

- archiver: 用于创建压缩文件
- autoprefixer: 用于自动添加CSS浏览器前缀
- dotenv: 用于读取环境变量
- esbuild: 用于打包和压缩JavaScript文件
- fs-extra: 对Node.js内置的fs模块进行扩展，提供了更多便捷的文件操作方法
- process: Node.js内置的process模块，用于获取环境变量
- tailwindcss: CSS框架，用于快速构建用户界面

代码中的主要功能是进行项目的构建和打包，具体步骤如下：
1. 删除之前构建的目录
2. 使用esbuild将源代码进行打包，输出到指定的目录中
3. 将打包后的文件进行压缩，生成zip文件
4. 复制一些通用文件到目标目录中
5. 对目标目录进行打包，生成zip文件

这段代码主要用于将Web浏览器扩展（Chrome和Firefox）的源代码进行打包和压缩，生成可发布的扩展文件。
 */