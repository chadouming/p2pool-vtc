from setuptools import setup

setup(name='p2pool-vtc',
      version='3.0.0',
      description='p2pool for Vertcoin',
      url='http://github.com/chadouming/p2pool-vtc',
      license='GPLv3',
      author = 'James Lovejoy',
      author_email = 'jameslovejoy1@gmail.com',
      packages=['p2pool','p2pool/bitcoin','p2pool/bitcoin/networks','p2pool/util','p2pool/networks'],
      install_requires=[
          'twisted',
          'argparse',
          'pyOpenSSL',
          'verthash'
      ],
      scripts=['run_p2pool.py'],
      include_package_data=True,
      zip_safe=False)
