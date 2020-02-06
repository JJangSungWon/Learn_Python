from xml.etree.ElementTree import Element, dump, SubElement, ElementTree, parse

note = Element("note") # Element 이용해 태그, 텍스트 값 추가 가능하다.
# note = Element("note", date="20120104")와 같이 Element 생성 시 직접 attribute 추가 가능하다.
to = Element("to")
to.text = "Tove"

note.append(to)

# SubElement
SubElement(note, "from").text = "Jani"

# remove
dummy = Element("dummy")
note.insert(1, dummy)
#dump(note)
note.remove(dummy)

# add attribute
note.attrib["date"] = "20120104"

# 정렬된 형태의 xml
def indent(elem, level=0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

indent(note)

# write
ElementTree(note).write("note.xml")

# parsing
tree = parse("note.xml")
note = tree.getroot()

# read attribute value
print(note.get("date"))
print(note.get("foo", "default")) # 첫 번째 인자에 해당되는 attribute value가 없을 경우 두 번째 값을 리턴한다.
print(note.keys()) # 모든 attribute key value를 list로 return 한다.
print(note.items()) # 모든 attribute key, value쌍을 return 한다.

# xml tage 접근
from_tag = note.find("from") # note 태그 하위에 from과 일치하는 첫 번째 태그를 찾아서 리턴한다.
from_tags = note.findall("from") # note 태그 하위에 from과 일치하는 모든 태그를 리스트로 리턴한다.
from_text = note.findtext("from") # note 태그 하위에 from과 일치하는 첫 번째 태그의 텍스트 값을 리턴한다.

# 특정 태그의 하위 element 순차적으로 처리
childs = note.getiterator()
childs = note.getiterator("from")
childs = note.getchildren()
for parent in tree.getiterator():
    for child in parent:
        pass

dump(note)

