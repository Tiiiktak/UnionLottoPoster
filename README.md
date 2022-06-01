# UnionLottoPoster 彩票海报绘制

- 爬取福彩彩票中奖信息(双色球、快乐8、福彩3D、七乐彩)
- 使用模板绘制彩票海报

<img alt="poster" src="doc/lotto_poster.jpg" width="200"/>

## Demo

使用 Gradio 简单实现: `UnionLottoPoster/demo_gradio`

![gradio demo](doc/gradio_demo.png)

## 结构

``` 
UnionLottoPoster
  ├─ README.md
  ├─ config.yml
  ├─ lotto_poster
  │  ├─ crawler     // 爬虫
  │  │  ├─ crawler.py  
  │  │  ├─ base.py     // 基类，其余爬虫类从此派生
  │  │  └─ cwl_official.py // 福彩官网(cwl.gov.cn)
  │  ├─ drawer      // 绘制
  │  │  └─ poster_drawer.py
  │  ├─ util        // 工具
  │  │  ├─ cfg.py   // 配置文件
  │  │  ├─ code_info_format.py // 中奖信息格式
  │  │  └─ exception.py        // 异常
  │  └─ app        // fastapi backend
  ├─ demo_gradio
  │  └─ demo.py    
  └─ doc
```

