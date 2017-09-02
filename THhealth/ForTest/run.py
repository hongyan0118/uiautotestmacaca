#-*- coding: utf-8 -*-

import os
import sys

from macaca import WebDriver

sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
from Public.Log import Log
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage

from THhealth.PageObject.THhealthHomePage import THhealthHomePage
from THhealth.PageObject.WizardPage import skip_wizard_to_home
from THhealth.PageObject.PermissionRequestPopupPage import PermissionRequestPopupPage
from THhealth.PageObject.HealthNewsPage import HealthNewsPage
from THhealth.PageObject.THhealthDiscoverPage import THhealthDiscoverPage
from THhealth.PageObject.THhealthConsulationPage import THhealthConsulationPage
from THhealth.PageObject.THhealthMyPage import THhealthMyPage
from THhealth.PageObject.THhealthRecordPage import THhealthRecordPage



class Run(BasePage):
    def run(self):

        #skip_wizard_to_home()
        #homepage = THhealthHomePage()
        #homepage.click_discover()
        #discover_page = THhealthDiscoverPage()
        #self.driver.assertTrue(discover_page.wait_page())
        #discover_page.click_tuhuanlife()
        width = self.driver \
            .get_window_size()['width']
        height = self.driver \
            .get_window_size()['height']
        i = 1
        while (i <= 3):
            self.driver \
                .touch('drag', {
                'fromX': width * 0.8,
                'fromY': height * 0.2,
                'toX': width * 0.05,
                'toY': height * 0.2,
                'steps': 5
            })
            self.driver.save_screenshot('banner'+str(i)+'.jpg')
            i = i + 1




def init():
    port = int(sys.argv[1])
    udid = sys.argv[2]
    report_path = str(sys.argv[3])
    session = sys.argv[4]

    server_url = {
                'hostname': '127.0.0.1',
                'port': port,
    }

    log = Log()
    log.set_logger(udid, report_path + '\\' + 'client.log')

    driver = WebDriver('', server_url)
    driver.attach(session)

    # set cls.path, it must be call before operate on any page
    path = ReportPath()
    path.set_path(report_path)

    # set cls.driver, it must be call before operate on any page
    base_page = BasePage()
    base_page.set_driver(driver)


if __name__ == '__main__':
    init()

    Run().run()


