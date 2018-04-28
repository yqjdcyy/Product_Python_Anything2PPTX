# Pre-Condition
- System
    - windows 10
- Java
    - java 1.8

# TODO
- Command
    - ~~日志~~
    - ~~参数化请求~~
    - ~~相对转换实现~~
    - ~~Shell 调用~~
    - ~~整体联调~~
- Interface
    - ~~界面设计& 实现~~
    - ~~按钮绑定~~
    - 整体联调
        - ~~主体功能~~
        - ~~打开目录时，路径异常~~
        - ~~是否打开文件夹按钮无效~~

# Feature
## Command
### Help
- `python command.py -h`
    ```
    -h|--help       帮助文档
    -t|--type       请求服务类型                
            1:      PDF2PPTX
            2:      IMAGES2PPTX                
            3:      PDF2IMAGES
    -s|--src        请求转换资源文件路径        
    -d|--dest       请求转换资源转换后保存路径
    -p|--dpi        PDF转换参数：指定转换图片 DPI 值        
    -e|--extension  PDF转换参数：指定转换图片扩展名        
    -o|--open       是否于转换后打开相应目录
    ```

### CONFIG
- `python command.py -t 0`
    ```
    {
        "type": ReqType.CONFIG,
        "src": ,
        "dest": ,
        "dpi": 96,
        "extension": jpeg,
        "open": True
    }
    ```

### PDF2PPTX
- `python command.py -t 1 --src="D:\work\git\yao\python\Utils_Python_Anything2PPTX\resource\sliders.pdf"`

### IMAGES2PPTX
- `python command.py -t 2 --src="D:\work\git\yao\python\Utils_Python_Anything2PPTX\resource" -o`

### PDF2IMAGES
- `python command.py -t 3 --src="D:\work\git\yao\python\Utils_Python_Anything2PPTX\resource\sliders.pdf"`

## Interface
- visual interface for `Command`
- ![homepage](/resource/homepage.png)


# Reference
## Project
- PDF2Images
    - [yqjdcyy/Utils_Work - PDFBox](https://github.com/yqjdcyy/Utils_Work/tree/master/Convetor/PDF/PDFBox)
- Images2PPTX
    - [yqjdcyy/Utils_CSharp_AnythingToPPTX](https://github.com/yqjdcyy/Utils_CSharp_AnythingToPPTX)

## Other
- [Python 异常处理](http://www.runoob.com/python/python-exceptions.html)    
- [Python rindex()方法](http://www.runoob.com/python/att-string-rindex.html)    
- [python项目中不同文件夹py源文件之间如何相互调用--Python import中相对路径的问题](https://blog.csdn.net/helloxiaozhe/article/details/76578096)