# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyClickLog(PythonPackage):
	"""Logging integration for Click"""
	
	homepage = "https://github.com/click-contrib/click-log"
	pypi = "click-log/click_log-0.4.0-py2.py3-none-any.whl" 

	version("0.1.1", sha256="86e068f2eaf2f5dac553fe6bbefa5ab39b36f906dcd7d0cd5a6da65116d6bdec", expand=False, url="https://files.pythonhosted.org/packages/32/ec/215dc3a98e450c6e2b5afd48f4cf1ef71b097acc9a0fe5dc8d6b4b38383c/click_log-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="f64ec818b5e4978a802ad470b7854798b1db10fb08422ea7de2601001189fc2a", expand=False, url="https://files.pythonhosted.org/packages/f1/d4/90c0ae2781968b474756274a7912a0d648b8faa07ae2d78cc85dd255f646/click_log-0.1.2-py2.py3-none-any.whl")
	version("0.1.3", sha256="821a014bee386b6aceeafcbdaf8702c58b429838d26a51aac4f23c56a4d564d8", expand=False, url="https://files.pythonhosted.org/packages/7d/4f/9144272b73616dd65376f7b9f07cb79bbc66c0445caf6532df14c4129a49/click_log-0.1.3-py2.py3-none-any.whl")
	version("0.1.4", sha256="420695bf6f76a2edac514dca02e09fc4604a5e475f527f8a28033d9074c770a7", expand=False, url="https://files.pythonhosted.org/packages/e3/b4/94bae2a74d347ff5b87d0877b5a02650c68b828ecd7c6091e53343a4016c/click_log-0.1.4-py2.py3-none-any.whl")
	version("0.1.5", sha256="4d92ce2f3ceddf68f9b73787599c9bca31503a26adff89dcf0e5bd552d68a717", expand=False, url="https://files.pythonhosted.org/packages/51/c5/929e6f00f5f035fcd65ec6d961a6e50a738c68cabf9fb2220a9a33a7b2ba/click_log-0.1.5-py2.py3-none-any.whl")
	version("0.1.6", sha256="7be0d850a511e9bcca0864f3ab2674ef1c14122b49fdb68a524ced5e7d2a27a3", expand=False, url="https://files.pythonhosted.org/packages/4c/66/ddad88d6b5bf5846f3adb82eb5eec33f71110e2179c9b1d4a6b3fbeab767/click_log-0.1.6-py2.py3-none-any.whl")
	version("0.1.7", sha256="a7444666932f57785b70755f2c731e452e626c9cc960d53ed4df6b0485cbe6c2", expand=False, url="https://files.pythonhosted.org/packages/f7/67/4bb06f026dfcc037a979c14350577d5aca532585919002e9c392d1e7f07f/click_log-0.1.7-py2.py3-none-any.whl")
	version("0.1.8", sha256="002ca50ae0abec8affa2a4abb41fda6eb0a3cbc61bfae41e52f6d5607d3a45ff", expand=False, url="https://files.pythonhosted.org/packages/44/7f/836705a872576c6c4e1efc87793f77ce2d2dae5651b68bfb1d690a781279/click_log-0.1.8-py2.py3-none-any.whl")
	version("0.2.0", sha256="05a8bb912db06672d06d303038341bd79aaf75cd5f2f0f8e4ef72c4600ee6ab7", expand=False, url="https://files.pythonhosted.org/packages/ed/91/0cdb5d9590e503e97b7a2eaa939f7b4aaaa67b93c859011ea2d7aa63bb87/click_log-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="27d354caa8cd83190d396a857f5dca062cf74109cff8951c241518ad9ad8de4e", expand=False, url="https://files.pythonhosted.org/packages/17/d9/d6f908f6b6a075b023ac248bcb2767e12758a93c7f336636f99356f1bd98/click_log-0.2.1-py2.py3-none-any.whl")
	version("0.3.0", sha256="10542cfa6d69024be9b20d2abd17dd8f689bc3b03702d6fe1b1a97686875aa8f", expand=False, url="https://files.pythonhosted.org/packages/84/9e/7f8cf574f679a39be898e2a491fe43a39b1ccb5b4f2db0a14fb2b91b2ae3/click_log-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="68ee4e04fa687c954bb2717373baf45ddc60ea330f0654661df4d08243984e1a", expand=False, url="https://files.pythonhosted.org/packages/24/d8/31e745902d02d25e840aec11ecaecf84d66a209873451e4daba0f9abd8d8/click_log-0.3.1-py2.py3-none-any.whl")
	version("0.3.2", sha256="eee14dc37cdf3072158570f00406572f9e03e414accdccfccd4c538df9ae322c", expand=False, url="https://files.pythonhosted.org/packages/38/52/a9dbb622f40ceeb09df141d855062cc9fbb38011f0ad8caee0cd840f399c/click_log-0.3.2-py2.py3-none-any.whl")
	version("0.4.0", sha256="a43e394b528d52112af599f2fc9e4b7cf3c15f94e53581f74fa6867e68c91756", expand=False, url="https://files.pythonhosted.org/packages/ae/5a/4f025bc751087833686892e17e7564828e409c43b632878afeae554870cd/click_log-0.4.0-py2.py3-none-any.whl")


# {'click': ['0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0']}