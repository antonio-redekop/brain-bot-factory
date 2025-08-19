# brain-bot-factory

world-class MES (Manufacturing Execution System) for production of Brain robots

## Background

**What is  `brain-bot-factory`?**

Developed based on world-class lean principles and manufacturing expertise, `brain-bot-factory` is a browser-based set of work instructions (markdown files) that standardizes the following areas of robot production:

    1. Assembly and Configuration
    2. Testing
    3. Quality

It employs the concept of "Visual Factory" which is a factory that uses visual cues and tools to convey information about production processes, statuses, and procedures, making everything clear at a glance and reducing ambiguity, mistakes, and mental fatigue. This approach, rooted in lean manufacturing principles, aims to improve efficiency, reduce waste, and enhance overall efficiency.

## Requirements 

```
O/S: Linux/Mac
Browser: Firefox, Chrome
Required Extensions: Markdown Viewer, Hover Zoom+
```

## Instructions

### Installing and Configuring Extensions

1.  Download and install `Markdown Viewer` extension from one of the following sources, depending on browser:
    - [Firefox Add-Ons](https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer-chrome/)
    - [Chrome Web Store](https://chromewebstore.google.com/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk?hl=en)
2.  In the browser's extension settings, Enable File Access for local file urls for this extension.
3.  In the extension, set the theme to `Github Dark` with `Wide` view selected.
4.  In the extension, navigate to `Content` tab and enable `toc` (table of contents) 
5.  Download and install `Hover Zoom+` extension from one of the following sources, depending on browser: 
    - [Firefox Add-Ons](https://addons.mozilla.org/en-US/firefox/addon/hover-zoom-plus/)
    - [Chrome Web Store](https://chromewebstore.google.com/detail/hover-zoom+/pccckmaobkjjboncdfnnofkonhgpceea?hl=en)
6.  In the browser's extension settings, enable File Access for local file urls for this extension.
7.  Restart all instances of the browser.

### Viewing Work Instructions

1. Clone the repository onto local machine.  The following directory structure will be cloned:
```
brain-bot-factory/
├── .gitignore
├── README.md
└── jaeger-p2/
    ├── img/
    ├── bom/
    ├── base.md
    └── tower.md
```
2. Navigate to the desired `.md` file and open with preferred browser.
3. Enjoy 
