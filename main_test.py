# -*- coding:utf-8 -*-
from ThirdDay02.mytestcase.run_plan import MyTestPlan

class Main:
    def __init__(self,dumppath,udid,tpfile,tcfile,tpsheet,tcsheet):
        self.mtp = MyTestPlan(dumppath,udid,tpfile,tcfile,tpsheet,tcsheet)

    def run(self):
        self.mtp.run_testplan()
        self.mtp.get_report()

if __name__ == '__main__':
    dumppath = r'./appcommon/window_dump.xml'
    udid = '127.0.0.1:62001'
    tpfile = r'./mytestdata/testplan.xlsx'
    tcfile = r'./mytestdata/testdata.xlsx'
    tpsheet = 'Sheet1'
    tcsheet = 'Sheet1'
    m = Main(dumppath,udid,tpfile,tcfile,tpsheet,tcsheet)
    m.run()
