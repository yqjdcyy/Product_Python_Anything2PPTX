

# Pre-Condition
- System
    - windows 10
- Java
    - java 1.8

# Switch
## Help
- `python launcher.py -h`
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

## CONFIG
- `python launcher.py -t 0`
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

## PDF2PPTX
- `python launcher.py -t 1 --src="D:\work\git\yao\python\Utils_Python_Anything2PPTX\resource\sliders.pdf"`

## IMAGES2PPTX
- `python launcher.py -t 2 --src="D:\work\git\yao\python\Utils_Python_Anything2PPTX\resource" -o`

## PDF2IMAGES
- `python launcher.py -t 3 --src="D:\work\git\yao\python\Utils_Python_Anything2PPTX\resource\sliders.pdf"`


# Reference
- PDF2Images
    - [yqjdcyy/Utils_Work - PDFBox](https://github.com/yqjdcyy/Utils_Work/tree/master/Convetor/PDF/PDFBox)
- Images2PPTX
    - [yqjdcyy/Utils_CSharp_AnythingToPPTX](https://github.com/yqjdcyy/Utils_CSharp_AnythingToPPTX)