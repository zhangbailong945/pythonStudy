from xml.dom.minidom import parse
import xml.dom.minidom

#使用minidom解析器打开test.xml
DomTree=xml.dom.minidom.parse("test.xml")
collection=DomTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root Element:%s"% collection.getAttribute("shelf"))

#在集合中获取所有电影
movies=collection.getElementsByTagName("movie")

#打印每部电影的详细信息
for movie in movies:
    print("********movie*******")
    if movie.hasAttribute("title"):
        print("title:%s"% movie.getAttribute("title"))
    
    type=movie.getElementsByTagName('type')[0]
    print("type:%s"% type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print("format:%s"% format.childNodes[0].data)
    year = movie.getElementsByTagName('year')[0]
    print("year:%s" % year.childNodes[0].data)
    rating=movie.getElementsByTagName('rating')[0]
    print("rating:%s"% rating.childNodes[0].data)
    description=movie.getElementsByTagName('description')[0]
    print("description:%s"% description.childNodes[0].data)
