# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySimpleWebsocket(PythonPackage):
	"""Simple WebSocket server and client for Python"""
	
	homepage = "https://github.com/miguelgrinberg/simple-websocket"
	pypi = "simple-websocket/simple_websocket-1.1.0-py3-none-any.whl" 

	version("0.0.1", sha256="0ef81339012d87543ba99af0af462ccb5a17f44779841b53c962d273b636b282", expand=False, url="https://files.pythonhosted.org/packages/e8/d5/499369191c25fd64e9ddb2f96e7b5db8181da1966fd6c2583ef323979c39/simple_websocket-0.0.1-py3-none-any.whl")
	version("0.1.0", sha256="af8ec55f8421a9cdc7495f96b8ad78aa6dd2d206dfa6a4761cd17885c057fc08", expand=False, url="https://files.pythonhosted.org/packages/a2/a5/b81e660ce57512d6a72ddd359b80d9730e1329a905f83cab6c23d176057a/simple_websocket-0.1.0-py3-none-any.whl")
	version("0.10.0", sha256="fc1bc56c393a187e7268f8ab99da1a8e8da9b5dfb7769a2f3b8dada00067745b", expand=False, url="https://files.pythonhosted.org/packages/61/be/26306666c771f86304c0fc814530ddeabb324ff74ca39d95a638609e8d8d/simple_websocket-0.10.0-py3-none-any.whl")
	version("0.10.1", sha256="62c36bacfd75cc867927bb39d91951342a7234bdfe20f41dd969a3b8bb1413b7", expand=False, url="https://files.pythonhosted.org/packages/f6/00/6583d44c59b765c01a14e69260d90c3ca489a47ac8ffc9f1ddf81f1d25f5/simple_websocket-0.10.1-py3-none-any.whl")
	version("0.2.0", sha256="8bd276cee865e52040ae07624f5fce65f102fedea4814d102f809f9d1625015a", expand=False, url="https://files.pythonhosted.org/packages/68/d6/7e4f5f3ffcd687aae1fd154b05e035a287b6b5e3724e197ea9007f836e9c/simple_websocket-0.2.0-py3-none-any.whl")
	version("0.3.0", sha256="20015b3ca1b192c77bba575a8b23b6a7e227548a8d35022592b63a6aab10cdd4", expand=False, url="https://files.pythonhosted.org/packages/c4/8e/016712b30d832ac510aee2b1a502dc04f3c6c0de38667f59d0f49c12ea22/simple_websocket-0.3.0-py3-none-any.whl")
	version("0.4.0", sha256="6553fcf8c1b5fbb5ef36f64c0399c6909d077d5064286caadd0f64d78c9df10a", expand=False, url="https://files.pythonhosted.org/packages/4d/8b/688bda9f619174e9b3b8c2a0f851b529681bfc1fb65e4786ae3bee12b78d/simple_websocket-0.4.0-py3-none-any.whl")
	version("0.5.0", sha256="01ea584f5685f7d21f207b9cadbc31234c078bedf18b56a924cabeb784057708", expand=False, url="https://files.pythonhosted.org/packages/57/51/df7fe0b328ea5d8ebc2eef1beafde79ec54e51421159282c9a3b144118d5/simple_websocket-0.5.0-py3-none-any.whl")
	version("0.5.1", sha256="9c3fa5ba5c444504a21b18e964970e4f2a549de3605b3eca245bca986c827979", expand=False, url="https://files.pythonhosted.org/packages/f5/95/c4fc0e10b70621dae820026c9835b3accade7c05efd6937b21a2f2336004/simple_websocket-0.5.1-py3-none-any.whl")
	version("0.5.2", sha256="da5f22e7efb9b86bab7e3801345c0aaab90748bb54737736f5a209c46e88b6f9", expand=False, url="https://files.pythonhosted.org/packages/8b/7f/aa1b0e9df0fb3959658c6aa3767fc32080c90c19514197783d81c7c858a9/simple_websocket-0.5.2-py3-none-any.whl")
	version("0.6.0", sha256="5b841fb37eb3e2bc1c90adeef8c7a0e3829a0c32026dfcbe439c569cd100be55", expand=False, url="https://files.pythonhosted.org/packages/69/06/821658ef224a603c4dc339eb13f6ff2624b4533e5eb819ec9f495847cc31/simple_websocket-0.6.0-py3-none-any.whl")
	version("0.7.0", sha256="1538840f74c76d4edabdd1141ff909a4b310020cfe4613294824102fa3865537", expand=False, url="https://files.pythonhosted.org/packages/88/4a/319e319134024da1c37fdcdee7e6abd6750afefb9a404c633ba27cdb1f0f/simple_websocket-0.7.0-py3-none-any.whl")
	version("0.8.0", sha256="fe812eb97f3748b6bdf89470f3cc60f4c6f92cc8935e43df8634a1aed56813a6", expand=False, url="https://files.pythonhosted.org/packages/70/a7/9705cf6af43b07d1a50960828c1037b5250b7922c2486bddbb286e66e0c7/simple_websocket-0.8.0-py3-none-any.whl")
	version("0.8.1", sha256="bab2f34151d8b9abb1ea6d911e5edc8232fc203b6f814d179db0ba3f93e4e026", expand=False, url="https://files.pythonhosted.org/packages/6e/0e/ca7d86474c4edd4118090c13fa611a458f5048d3bf065846df56158e930d/simple_websocket-0.8.1-py3-none-any.whl")
	version("0.9.0", sha256="c0acee94c7428319bf299657169807a5e3fdce7be8e1fb03724e0aba378db2fe", expand=False, url="https://files.pythonhosted.org/packages/a3/78/d8d15733b768559ff2df63debd6a138f2aaca3763716f99caca2f0953143/simple_websocket-0.9.0-py3-none-any.whl")
	version("1.0.0", sha256="1d5bf585e415eaa2083e2bcf02a3ecf91f9712e7b3e6b9fa0b461ad04e0837bc", expand=False, url="https://files.pythonhosted.org/packages/6d/ea/288a8ac1d9551354488ff60c0ac6a76acc3b6b60f0460ac1944c75e240da/simple_websocket-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="4af6069630a38ed6c561010f0e11a5bc0d4ca569b36306eb257cd9a192497c8c", expand=False, url="https://files.pythonhosted.org/packages/52/59/0782e51887ac6b07ffd1570e0364cf901ebc36345fea669969d2084baebb/simple_websocket-1.1.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-wsproto", type=("build", "run"))

# {'wsproto': ['0.0.1', '0.1.0', '0.10.0', '0.10.1', '0.2.0', '0.3.0', '0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.7.0', '0.8.0', '0.8.1', '0.9.0', '1.0.0', '1.1.0'], "sphinx;extra=='docs'": ['1.0.0', '1.1.0'], "tox;extra=='dev'": ['1.1.0'], "flake8;extra=='dev'": ['1.1.0'], "pytest;extra=='dev'": ['1.1.0'], "pytest-cov;extra=='dev'": ['1.1.0']}