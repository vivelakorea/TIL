from collections import namedtuple

MyStruct = namedtuple("MyStruct", "field1 field2 field3")

m = MyStruct("foo", "bar", "baz")
