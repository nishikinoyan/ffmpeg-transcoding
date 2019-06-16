import os
import subprocess
import time

if __name__ == '__main__':
    '''
    cat /etc/issue
    Ubuntu 18.10 \n \l

    \S
    Kernel \r on an \m
    '''
    path = os.path.abspath(os.curdir)
    print(path)
    cmd = subprocess.getstatusoutput('cat /etc/issue')[1]
    if 'Ubuntu' in cmd:
        print('Ubuntu系统')
        time.sleep(1)
        os.system('cd ' + path)
        os.system(
        '''
        apt-get install epel-release -y
        apt-get install rpm -y
        apt-get update -y
        apt-get install autoconf automake bzip2 cmake freetype-devel gcc gcc-c++ git libtool make mercurial pkgconfig zlib-devel cmake hg numactl numactl-devel freetype freetype-devel freetype-demos -y
        rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
        rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
        apt-get install -y ffmpeg
        '''
        )
    if 'Kernel' in cmd:
        print('Centos系统')
        time.sleep(1)
        os.system('cd ' + path)
        os.system(
        '''
        yum install epel-release -y
        yum update -y
        yum install autoconf automake bzip2 cmake freetype-devel gcc gcc-c++ git libtool make mercurial pkgconfig zlib-devel cmake hg numactl numactl-devel freetype freetype-devel freetype-demos -y
        rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
        rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
        yum install -y ffmpeg
        '''
        )