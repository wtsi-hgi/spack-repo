# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythonIrodsclient(PythonPackage):
	"""A python API for iRODS"""
	
	homepage = "https://github.com/irods/python-irodsclient"
	pypi = "python-irodsclient/python_irodsclient-2.0.1-py2.py3-none-any.whl" 

	version("0.3.1", sha256="0963101b7c7d34e1d1026888c92ee0aaf26cdc7704f066a26c59c4f62b0c0580", expand=False, url="https://files.pythonhosted.org/packages/5d/46/7e94adb496fee3990696b31795bee49c1d81e70bd8edc17984a4a61907c2/python_irodsclient-0.3.1-py2-none-any.whl")
	version("0.4.0", sha256="c349ab40d94e44534a332504b8224a783ecf8d0a8bb390ffffb304f4ebacb7c0", expand=False, url="https://files.pythonhosted.org/packages/5d/11/f2944c3f907d188ec2221930f4afc7bb0077e023ef60b0899d6a3f578bd4/python_irodsclient-0.4.0-py2-none-any.whl")
	version("0.5.0rc1", sha256="20494846b0dc620637d2ea633e58847c6688e29aca8fdf7ef2cf05baf06e3f6a", expand=False, url="https://files.pythonhosted.org/packages/3c/f9/a1851903f9a8a54558bb9bc172dcb796e175a01fd62cfc2fdce2f8222952/python_irodsclient-0.5.0rc1-py2-none-any.whl")
	version("0.6.0", sha256="042a1df5953a33e4bc0ff720f54333e0513c10006f39e1e8c8718a4c6c916e03", expand=False, url="https://files.pythonhosted.org/packages/6a/dd/8863d5a98ec5d96629fc6779832dbd5f383fdf589fd3332be519ca94b287/python_irodsclient-0.6.0-py2.py3-none-any.whl")
	version("0.7.0", sha256="5e43a28c23223f5c37669f24dfb042adf7a078d0f92b48d2d04f13325d5f311b", expand=False, url="https://files.pythonhosted.org/packages/cc/b3/9c6e9a66aba187699246f143880f8be35f5e9368d44a022a0cb88c54919b/python_irodsclient-0.7.0-py2.py3-none-any.whl")
	version("0.7.0rc1", sha256="1044b22cfe32de51365bd5435ce261cdfb144fb5718bf86314b0d87f3e9a2ac9", expand=False, url="https://files.pythonhosted.org/packages/2a/58/58a1d21fbcae234bd51368600cf5ce9ef56c4e5d358d927b41f9e1e78d0d/python_irodsclient-0.7.0rc1-py2.py3-none-any.whl")
	version("0.7.0rc2", sha256="52a6226071d160f96f8c3f0337d8fa972f170ca816574b0e948435cf49cf3c8d", expand=False, url="https://files.pythonhosted.org/packages/8d/53/1e69b848b50d90cafc9a2fc2f9db35d97cef3a20571e8fadbd9a3b538802/python_irodsclient-0.7.0rc2-py2.py3-none-any.whl")
	version("0.8.0", sha256="ecd6dd2a6b08ee469538412d52bb70211c32c3553c4c309e93ad3af2f4786e8a", expand=False, url="https://files.pythonhosted.org/packages/b9/d9/1a0e85b6962be65aff904b88001c38d1cc12be61e7f75ae32955467defd3/python_irodsclient-0.8.0-py2.py3-none-any.whl")
	version("0.8.1", sha256="509b2e22e5d1a552ae3d59d519b6ddf8544ee5280051990fe44b2e6d41d7650f", expand=False, url="https://files.pythonhosted.org/packages/03/6f/3b0950c9ab26a1d05e357b7be2e45795d105f9a0b3af538aa6155a36c13b/python_irodsclient-0.8.1-py2.py3-none-any.whl")
	version("0.8.2", sha256="69e1e3f19e29a6554c517753c04e48c0d4725281c9a03dad9b7c749129b8834f", expand=False, url="https://files.pythonhosted.org/packages/80/02/5abc8dba9c1654e3a53ac9cda288c5d580bbdcf5cd62e1493314e75661b4/python_irodsclient-0.8.2-py2.py3-none-any.whl")
	version("0.8.3", sha256="0dafb23efcf824bcab9f213b3ebf9ab9eaf9c409057f040ae8743928a01e2a3a", expand=False, url="https://files.pythonhosted.org/packages/fd/27/34bcd60821ae64f83162cbb4150d68c85bb0403ef2f8682141465d79a490/python_irodsclient-0.8.3-py2.py3-none-any.whl")
	version("0.8.4", sha256="00445b43f7f052a17009886988e32d06e7c61842f0c90b5b4d1d1116c32e46f2", expand=False, url="https://files.pythonhosted.org/packages/8d/a2/bf0bac08d9438549816b5efecfbc9f499dd10db86615b195eab3ac729ae9/python_irodsclient-0.8.4-py2.py3-none-any.whl")
	version("0.8.5", sha256="974c57b46f99281787844f9e4824534c460fcaad1eb2fa1b01adbb9ecc2d6897", expand=False, url="https://files.pythonhosted.org/packages/45/60/68be54f22f59aa51b052be468a18b48d7faed6290514c91690709576dbbd/python_irodsclient-0.8.5-py2.py3-none-any.whl")
	version("0.8.6", sha256="24e87eb04ce422b01a3f0e0bab2c116ef9d99e6fe643a8ad9bdde67927806876", expand=False, url="https://files.pythonhosted.org/packages/90/b0/498508e150769f9a014b19cebc941366541adc7cc4548002498672b5134e/python_irodsclient-0.8.6-py2.py3-none-any.whl")
	version("0.9.0", sha256="a44440ff68c7b901c5db8cf560959a253cedb089e4c9fa90dd20c2bb530511d6", expand=False, url="https://files.pythonhosted.org/packages/22/4b/b777137b6cdd20ea5182f85e4d6a263cfd40c981e5157c16d4ce1e915761/python_irodsclient-0.9.0-py2.py3-none-any.whl")
	version("1.0.0", sha256="9e2c727232857645ee8cd9175aa304793a32644a7748c79e0229dd33d787864a", expand=False, url="https://files.pythonhosted.org/packages/cd/b5/1212e29439634378e810ad5e9ba5202862aba038624f8bc679217ce01923/python_irodsclient-1.0.0-py2.py3-none-any.whl")
	version("1.1.0", sha256="1ea1f6b6b5aa78768be5caf6393ce834c5ab3bec372fefd1f66abe2a7eb1e89c", expand=False, url="https://files.pythonhosted.org/packages/b2/fd/521571e216cdc5110fd34b69583a866f75e2f3c353dbd4d449820941ce19/python_irodsclient-1.1.0-py2.py3-none-any.whl")
	version("1.1.1", sha256="a7f45738ee870defe141b39c0474b76e2ff1b3b459e537276d36a077595073e4", expand=False, url="https://files.pythonhosted.org/packages/ca/20/f5e3669579d605ff7e6205d078b080c62d720e250d38c22c037d080cbdf2/python_irodsclient-1.1.1-py2.py3-none-any.whl")
	version("1.1.2", sha256="beb5e43db1dc662fd4c906189abe6db94e72e14a6cb95445c4e1d17453b0e22f", expand=False, url="https://files.pythonhosted.org/packages/88/38/fe3100e2ccfb5d3aab52863ba6d43354d2ebc13e203d75bde8949f7ab3e0/python_irodsclient-1.1.2-py2.py3-none-any.whl")
	version("1.1.3", sha256="c093d4dd3f980a78145f6c882acc0cd296fbce110d9f0c7f42852d624e3385fe", expand=False, url="https://files.pythonhosted.org/packages/70/74/6d9e9fb9e59cead45a32eb702d8492aa19d0dcf3d89573b5cb8393e22882/python_irodsclient-1.1.3-py2.py3-none-any.whl")
	version("1.1.4", sha256="6f6a9f75608ccbd71eb1756b7e6b42e0ba6c71ebc7aa3a19a69c71be016fe82a", expand=False, url="https://files.pythonhosted.org/packages/3f/6c/4c845b797d13773fa98ca2267b5c050d447c57d47ad24e2c1c03f5f8f671/python_irodsclient-1.1.4-py2.py3-none-any.whl")
	version("1.1.5", sha256="4665d9ef6837054f3526a8fc183f89cd14a26865d24c38de2a111c6920cdb510", expand=False, url="https://files.pythonhosted.org/packages/ad/cd/592c4df3f9772dbb6d8dcbaa388554e21d3db059ad4660bfb3dc705e9dab/python_irodsclient-1.1.5-py2.py3-none-any.whl")
	version("1.1.6", sha256="6bfb179932f0ef22ac4ef11d23d155ca1bde1c820f804cd1938a6ac05057f055", expand=False, url="https://files.pythonhosted.org/packages/c3/73/f52f383e3751be833ddf8ad56e45009d9b4a7e37e7363163970c0bd122a5/python_irodsclient-1.1.6-py2.py3-none-any.whl")
	version("1.1.7", sha256="7def1c09a88398f2d1f081f49a91c0ce3631e7020bed6339ca059714a9a91451", expand=False, url="https://files.pythonhosted.org/packages/f0/34/32484747a1e448ef16368bc18bea2e166eca55ba09289a18d29d435b6af8/python_irodsclient-1.1.7-py2.py3-none-any.whl")
	version("1.1.8", sha256="6e8aaec63acf335194ede5f1e7e8e0790079c1be34d059a7d7998c64ffbe3455", expand=False, url="https://files.pythonhosted.org/packages/83/b2/bd7fc36926ad7cf8a6fcb390902479c6fd18620b4360a377f402d2c8a8da/python_irodsclient-1.1.8-py2.py3-none-any.whl")
	version("1.1.9", sha256="64f6843191ba5e20b83b7cf7ba41e4d2478051cbfc8093c04d8d2ec85cba7938", expand=False, url="https://files.pythonhosted.org/packages/d1/1a/4513c15d80a887dfec3a823f29a89565712750684b15c9e185cd04fe8604/python_irodsclient-1.1.9-py2.py3-none-any.whl")
	version("2.0.0", sha256="693ebc0c2ab4489ab57a15a08899884be2ff6883bbbebd35f9a1e735bf01e6be", expand=False, url="https://files.pythonhosted.org/packages/82/7d/f1a190e8080892f4d0b95f66c115496f68877c4c07e24082a43b0abc4414/python_irodsclient-2.0.0-py2.py3-none-any.whl")
	version("2.0.1", sha256="5c1da14d6f9d0137ddd49b3ff2be951a0f77d649df70336898f0d3bf215553ad", expand=False, url="https://files.pythonhosted.org/packages/33/bb/d6adec2e95c5cb3b14ae159b43e0a99e8d3991739dc75829f5337fad5645/python_irodsclient-2.0.1-py2.py3-none-any.whl")

	depends_on("py-six", type=("build", "run"))
	depends_on("py-defusedxml", type=("build", "run"))
	depends_on("py-prettytable", type=("build", "run"))

# {'PrettyTable(>=0.7)': ['0.3.1'], 'PrettyTable(>=0.7.2)': ['0.4.0', '0.5.0rc1', '0.6.0', '0.7.0', '0.7.0rc1', '0.7.0rc2', '0.8.0', '0.8.1', '0.8.2', '0.8.3', '0.8.4', '0.8.5', '0.8.6', '0.9.0', '1.0.0', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5', '1.1.6', '1.1.7', '1.1.8', '1.1.9', '2.0.0', '2.0.1'], 'six(>=1.10.0)': ['0.7.0', '0.7.0rc1', '0.7.0rc2', '0.8.0', '0.8.1', '0.8.2', '0.8.3', '0.8.4', '0.8.5', '0.8.6', '0.9.0', '1.0.0', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5', '1.1.6', '1.1.7', '1.1.8', '1.1.9', '2.0.0', '2.0.1'], 'xmlrunner(>=1.7.7)': ['0.7.0', '0.7.0rc1', '0.7.0rc2', '0.8.0', '0.8.1', '0.8.2', '0.8.3', '0.8.4', '0.8.5', '0.8.6', '0.9.0', '1.0.0'], 'futures;python_version=="2.7"': ['0.9.0', '1.0.0', '1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5', '1.1.6', '1.1.7', '1.1.8', '1.1.9', '2.0.0', '2.0.1'], 'defusedxml': ['1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5', '1.1.6', '1.1.7', '1.1.8', '1.1.9', '2.0.0', '2.0.1'], "unittest-xml-reporting;extra=='tests'": ['1.1.0', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5', '1.1.6', '1.1.7', '1.1.8', '1.1.9', '2.0.0', '2.0.1']}