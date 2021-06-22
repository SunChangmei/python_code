'''
parser.add_argument('-c', '--client-install', action='store_true', help='Install OpenSSL on client machine')
parser.add_argument('-s', '--server-install', action='store_true',
                    help='Install Nginx, OpenSSL, QAT Engine and QAT driver software package on server machine')
parser.add_argument('-cfg', '--system-configuration', action='store_true',
                    help='Print out server machine configuration, CPU speed, memory capacity, Nginx, OpenSSL, QAT Engine and QAT driver software version etc')
parser.add_argument('-uc', '--client-uninstall', action='store_true', help='Uninstall OpenSSL from client machine')
parser.add_argument('-us', '--server-uninstall', action='store_true',
                    help='Uninstall Nginx, OpenSSL, QAT Engine and QAT driver software package from server machine')
parser.add_argument('-r', '--run-openssl-speed-test-on-server= rsa2048/ecdsap256/ecdhp256', action='store_true',
                    help='Run OpenSSL speed rsa2048/ecdsap256/ecdhp256 test on server machine')
parser.add_argument('-type', '--install-type=baremetal/guest/linux-container/docker', action='store_true',
                    help='nstall Nginx, OpenSSL, QAT Engine and QAT driver software stack on bare metal/virtualization/Linux-container/docker machine')
'''

class Test(object):

    def client_install(self):
        print('client install ---- ')


    def server_install(self):
        print("server install -----")


import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--client-install', action='store_true', help='Install OpenSSL on client machine')
parser.add_argument('-s', '--server-install', action='store_true',
                    help='Install Nginx, OpenSSL, QAT Engine and QAT driver software package on server machine')

args = parser.parse_args()
print(args)
test = Test()
if args.client_install:
    test.client_install()
if args.server_install:
    test.server_install()

