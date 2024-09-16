# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyclibrary(PythonPackage):
	"""C binding automation"""
	
	homepage = "http://github.com/MatthieuDartiailh/pyclibrary"
	pypi = "pyclibrary/pyclibrary-0.2.2-py3-none-any.whl" 

	version("0.1.0", sha256="fb022dc9a74fe930bc5eecc63df3881eec98fb7bd203a536e7e865e531532789", expand=False, url="https://files.pythonhosted.org/packages/99/b6/cd47b8977fadfa214bdcdff5bde72f7d4f0f905b7f0efecade46bd8c09ef/pyclibrary-0.1.0-py2.py3-none-any.whl")
	version("0.1.1", sha256="288e33899bcbbefc78de17714b347f0eb42577c227cd724ca37b601fdd3d2379", expand=False, url="https://files.pythonhosted.org/packages/2e/5a/2d6ba68df05c9449da6980ded4e5032331025db87b7eafbcd22dc355e615/pyclibrary-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="4ddd48cb9c8bfe4f438b2b3a17aac5d688989cb816c376729ae44884308d405a", expand=False, url="https://files.pythonhosted.org/packages/9f/06/7d3b83a5c08d80a78cdbbe2d36a96a5607375e1e7f710b99a34272e57f48/pyclibrary-0.1.2-py2.py3-none-any.whl")
	version("0.1.3", sha256="0bb290501629f3306b27c81889b9da3aee7daf0edf41ce28f2e2233c08c9ab50", expand=False, url="https://files.pythonhosted.org/packages/2d/00/647cf2fe02e9118204c722b45a7c7cd3436c78a8a2416878c9f7279b1c5e/pyclibrary-0.1.3-py2.py3-none-any.whl")
	version("0.1.4", sha256="4c91e0075ed7ddabb7c0852c17a7402a59c84d8925740ea7c25d092ef20060d0")
	version("0.1.5", sha256="fba59753402d638a22bae298bde2bff74460f38ab3cb356fc18b9b6da2ce27e5", expand=False, url="https://files.pythonhosted.org/packages/6c/7f/4631edf47fc0d0436a7373d187bd6823cc40421c8fd90c7c3e62df531e04/pyclibrary-0.1.5-py2.py3-none-any.whl")
	version("0.1.6", sha256="4797c3cae42d1163080d02f9693ade6bb04ec1ed6d957cbcd2f2c0cb21db296b", expand=False, url="https://files.pythonhosted.org/packages/2a/40/163b9b984c164b44aff475058c66a0a517a2d1a553b5a20e80b2b4a3bac5/pyclibrary-0.1.6-py2.py3-none-any.whl")
	version("0.1.7", sha256="2152d9979be22b6846a20c540fc5d3200e228d20aba0a9ef11418517f259dafa", expand=False, url="https://files.pythonhosted.org/packages/3a/53/1d90769b85038d51ea2f10572ad3304e2d679506de09811b39d0e41f30ba/pyclibrary-0.1.7-py2.py3-none-any.whl")
	version("0.2.0", sha256="d829d3cb19d736c988a66017db751da09f6b4e2ca3ce3f8492010a29f0ccb757", expand=False, url="https://files.pythonhosted.org/packages/23/a4/810282bbd912695129de47a0ffb43a984f4d470ed1092d49c53f9679dc7f/pyclibrary-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="17d3de0c1934eefcb3b5df630d07fac2a22ac6580aa79aa2c12446dbbd88fc34", expand=False, url="https://files.pythonhosted.org/packages/10/96/853ab7e0958a44bd8f4cdc9485469707a6c834639f3249c59d393922a47d/pyclibrary-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="b35796f5b8d2acfc5a6169e8cbba6fa78daf7536e4c07d895e60f959901e5be8", expand=False, url="https://files.pythonhosted.org/packages/f9/a5/2e1f2f138e14353e70101fb70d5c430b685b46a8ac9e010123cfb12ed4f7/pyclibrary-0.2.2-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-pyparsing", type=("build", "run"))
	depends_on("py-future", type=("build", "run"))

# {'future': ['0.1.0', '0.1.5', '0.1.6', '0.1.7'], 'future\r': ['0.1.1', '0.1.2', '0.1.3'], 'pyparsing(<3,>=2.3.1)': ['0.1.7', '0.2.0'], 'pyparsing(<4,>=2.3.1)': ['0.2.1'], 'pyparsing<4,>=2.3.1': ['0.2.2']}