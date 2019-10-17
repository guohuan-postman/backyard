#coding=utf-8
import HTMLTestRunner
import logging
import unittest
import time
from config import globalparam
from common import sendmail
from common import delete_zhiding_file

def run():
    logging.basicConfig(level=logging.INFO)
    test_dir = './cases'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
    '''
    for test_suite in suite:
        print(test_suite)
    '''
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname, 'wb') as f:

        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='闪电快车backyard报告',
            description='闪电快车backyard报告'
        )
        runner.run(suite)
    time.sleep(3)
    '''
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()
    '''

    #发送邮件时，记得打开这里。调试关闭的
    # sendmail.send_email('guoyuhuan8602@dingtalk.com,2639339651@qq.com,liuyongle@yaopin.onaliyun.com,'
    #                     'zanjichao@yaopin.onaliyun.com,zhangxiaohui@yaopin.onaliyun.com,mengdan1178@dingtalk.com,'
    #                     'zhengchuanming8629@dingtalk.com,henan5620@dingtalk.com,yanbo@yaopin.onaliyun.com,'
    #                     'meizile@huatangjt.com,wuyan@yaopin.onaliyun.com,','C:/Users/Administrator/Desktop/seleniumUI/report/testreport/')

    #发送邮件报告

    sendmail.send_email('2639339651@qq.com,1162695734@qq.com','C:/Users/flash/Desktop/backyard/report/testreport/')
    time.sleep(3)
    #正式发送邮件时打开，这是删除report下的报告的
    # currDir = './report/testreport'
    # delete_zhiding_file.removeFile(currDir,'.html')





if __name__=='__main__':
    run()
    logging.basicConfig(level=logging.debug())
    #for i in range(3):
        #run()


