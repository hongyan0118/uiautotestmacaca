
import os
import os.path
import re
import unittest

#shutil.copyfile("setting.ini", "../setting.ini")
casepaths = []

class CaseStrategy:
    def __init__(self):
        self.casepaths = []


    def createsuite(self):
        for parent, dirnames, filenames in os.walk('..'):

            for filename in filenames:
            # print "parent is:" + parent
            # print "filename is:" + filename
                path = os.path.join(parent, filename)
            # 正则判断是否为测试用例
                match = re.match('test_', filename)
                if match:
                    print (u"获取测试用例目录:%s" % parent)
                    casepaths.append(parent)
                    break

        testunit = unittest.TestSuite()
        # discover方法定义
        for casepath in casepaths:
            discover = unittest.defaultTestLoader.discover(
            casepath,
            pattern='test_*.py'
            )
            for test_suite in discover:
                for test_case in test_suite:
                    testunit.addTest(test_case)
            print (testunit)
        return testunit

if __name__ == '__main__':
    print ('debug info')
    for parent, dirnames, filenames in os.walk('..'):

        for filename in filenames:
            print (filename)
            # print "parent is:" + parent
            # print "filename is:" + filename
            path = os.path.join(parent, filename)
            # 正则判断是否为测试用例
            match = re.match('test_', filename)
            if match:
                print(u"获取测试用例目录:%s" % parent)
                casepaths.append(parent)
                break
    cs = CaseStrategy()
    cases = cs.createsuite()