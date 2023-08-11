# [3.1] - 2023-08

- 合并了后端和前端仓库，优化了项目目录
- 优化了版本发布流程。
- Wiki 迁移至 Vitepress，地址：https://autobangumi.org

## Backend

### Features

- 新增 `RSS Engine` 模块，从现在起，AB 可以自主对 RSS 进行更新支持 `RSS` 订阅并且发送种子给下载器。
  - 现在支持多个聚合 RSS 订阅源，可以通过 `RSS Engine` 模块进行管理。
  - 支持下载去重功能，重复的订阅的种子不会被下载。
  - 增加手动刷新 API，可以手动刷新 RSS 订阅。
  - 新增 RSS 订阅管理 API。
- 新增 `Search Engine`模块，可以通过关键词搜索种子并解析成收集或者订阅任务。
  - 插件化的搜索引擎，可以通过插件的方式添加新的搜索目标，目前支持 `mikan` 和 `dmhy`。
- 新增 IPv6 监听支持，需要在环境变量中设置 `IPV6=1`。
- API 新增批量操作，可以批量管理规则和 RSS 订阅。

### Changes

- 数据库结构变更，更换为 `sqlmodel` 管理数据库。
- 新增版本管理，可以无缝更新软件数据。
- 调整 API 格式，更加统一。
- 增加 API 返回语言选项。
- 增加数据库 mock test。
- 优化代码。

### Bugfixes

- 修复了一些小问题。
- 增加了一些大问题。

## Frontend

### Features

- 增加 `i18n` 支持，目前支持 `zh-CN` 和 `en-US`。
- 增加 RSS 管理页面。
- 增加搜索顶栏。

### Changes

- 调整一些 UI 细节。