from xml.etree.ElementTree import Element, dump, SubElement, ElementTree, parse

blog = Element("blog", data="20151231")

subject = Element("subject")
subject.text = "Why python?"
blog.append(subject)

SubElement(blog, "author").text = "Eric"
SubElement(blog, "content").text = "Life is too short, You Need Python!"

ElementTree(blog).write("blog.xml")
