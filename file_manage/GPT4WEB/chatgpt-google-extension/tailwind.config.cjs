/** @type {import('tailwindcss').Config} */
module.exports = {
  corePlugins: {
    preflight: false,
  },
  content: ['./src/**/*.tsx'],
  theme: {
    extend: {},
  },
  plugins: [],
}
/*
这是一个Tailwind CSS的配置文件。它配置了一些插件和主题，并指定了要在哪些文件中应用这些配置。

在这个配置中，禁用了preflight插件，这意味着不会自动引入任何重置样式。只有在需要时，你自己手动编写样式。

content属性指定了要应用这些配置的文件，这里是"./src/**、/*.tsx"，表示应用到所有以.tsx结尾的文件。

theme属性可以用来扩展或覆盖默认的主题样式。

plugins属性可以用来添加额外的插件。

所以，这个配置文件告诉Tailwind CSS如何处理样式和插件，以及在哪些文件中应用这些配置。
 */