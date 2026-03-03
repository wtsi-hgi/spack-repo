# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlake8Docstrings(PythonPackage):
	"""Extension for flake8 which uses pydocstyle to check docstrings"""
	
	homepage = "https://github.com/pycqa/flake8-docstrings"
	pypi = "flake8-docstrings/flake8_docstrings-1.7.0-py2.py3-none-any.whl" 

	version("0.1.0", sha256="89a182b811ee655bc17571eff2c96c4896bd88f21fabca053246f6799cd5b1f9")
	version("0.1.1", sha256="3337d505d564ebfe01ea375454b35c6e2c7716c0e8cf0c6d19ceb730933c1be4")
	version("0.1.2", sha256="03ed201557fd1729e0fa502aed8004a07acf0771cf738920bd052c771e68fb4d")
	version("0.1.3", sha256="cb46836af4705633498159535e7af35edd35eeaaa70ebebed33f98ad3663b295")
	version("0.1.4", sha256="f2569b682735811e1592b539f1fcc141f3ae44f3c9e3a9401542537959887b68")
	version("0.2.0", sha256="b8a8a00ed5f4bb4fe194c0a79e4ec621f93f46a54f41ad3d79611d5a6f69b565")
	version("0.2.1", sha256="8ad609c5cc0c348134570571050abc2ed19fa52c28a8c1ff74def09450e6108a")
	version("0.2.1.post1-py2", sha256="bc4db23dbe1e6519b97663269e359c6c7d2b9d67b0ce30567067bbe0fcbd2fed", expand=False, url="https://files.pythonhosted.org/packages/eb/f1/795c0f158579a0b4983e5633ceed37d9be188019ab8bb44cdfdc8d27f955/flake8_docstrings-0.2.1.post1-py2-none-any.whl")
	version("0.2.2-py2", sha256="5c21001b8803e4e7a3968a568151025e90218078b3c2ee61b88a2e861d781278", expand=False, url="https://files.pythonhosted.org/packages/25/eb/fc0466b2538f9699aab2aeae01faa0320e7a134751a148a10cfaf7d2677a/flake8_docstrings-0.2.2-py2-none-any.whl")
	version("0.2.3", sha256="ce461881cd7337e44fbdd996245f5db92c79e81b382e58b3a91fa9b00f547fa1", expand=False, url="https://files.pythonhosted.org/packages/88/cb/586db5d39a5cef082f8c4cdc65631ff2c91f45cfda920ef0f710626dd94a/flake8_docstrings-0.2.3-py2.py3-none-any.whl")
	version("0.2.4", sha256="1857aa046ffadb51577c42e97aedf9763a353ab2a1cc288ed4a7dd0b94373f2f", expand=False, url="https://files.pythonhosted.org/packages/79/9c/f80b2934b436e9986251a6a75c9b88fcafdccbe4c35b72ad6c7e5ec140b9/flake8_docstrings-0.2.4-py2.py3-none-any.whl")
	version("0.2.5", sha256="df8d9db44180d1b3976014cc983366ac70260c57f240bb81add71c73da7433a1", expand=False, url="https://files.pythonhosted.org/packages/1a/f8/0e56a1468e618feff7c3300439e8ae109a778d353a351d85afdb1bc6160b/flake8_docstrings-0.2.5-py2.py3-none-any.whl")
	version("0.2.6", sha256="5c2321ae6dd858e1880827ed9b93e209c533c4d1283570936b0286756a115d6a", expand=False, url="https://files.pythonhosted.org/packages/ec/b5/8f7797731090cf251407253255afa21f50a4964828d4b541c7841d8b4ce5/flake8_docstrings-0.2.6-py2.py3-none-any.whl")
	version("0.2.7", sha256="e4befc698b63ad758d6cdea39aece2df3c5615baed22f479c7194c0e6e5773b1", expand=False, url="https://files.pythonhosted.org/packages/16/9d/2a8f7ad1b3b4098600b8d9230dfb5ee478c0750630b8927d0a3cfc414778/flake8_docstrings-0.2.7-py2.py3-none-any.whl")
	version("0.2.8", sha256="6c64e271a70f39989fa95dbaca808b411b35dea6b8ca86fd1860ecadbeb8d816", expand=False, url="https://files.pythonhosted.org/packages/f3/54/363fd4c54a9f35fadca9112834cf4c1678c5bed0fce74dfdcd98ffd278d3/flake8_docstrings-0.2.8-py2.py3-none-any.whl")
	version("1.0.1", sha256="9f01c637dd71453589c12f022186a2a9179f92e6621fd2e75f0197a90a862888", expand=False, url="https://files.pythonhosted.org/packages/e1/9c/a607d3e244781c708cb984a359505decd4ca5e8e4ac772f333cd3c34dc9d/flake8_docstrings-1.0.1-py2.py3-none-any.whl")
	version("1.0.2", sha256="3a8235b55cb28fe13f20023fccc8e51992a3b834927334e33ae1f1c426d76e21", expand=False, url="https://files.pythonhosted.org/packages/fc/66/bbe457e8226c33d7a88e3627b34efc6a0e0aeb57fd67953ea7dbfcf9efa7/flake8_docstrings-1.0.2-py2.py3-none-any.whl")
	version("1.0.3", sha256="566ec212a471f4fb04ab01898b412813c6c6ed1f23218c2182559b6ce8ba9533", expand=False, url="https://files.pythonhosted.org/packages/23/d7/553eb22219ec6a348b6ad73eb91bb17fb727a17dd24f0ff751ca0b9ea47e/flake8_docstrings-1.0.3-py2.py3-none-any.whl")
	version("1.1.0", sha256="62992d5b452e940837ad42905baf09efcd6199813f8657391893414be8db463a", expand=False, url="https://files.pythonhosted.org/packages/ba/0f/0f052d9cc8250dfc026b2a3a11e6ff8d1435ddb2bed40b6ba72f381dadc5/flake8_docstrings-1.1.0-py2.py3-none-any.whl")
	version("1.2.0", sha256="2a4e5b6ad55771fd33725f917e177a968b93719d12948089d43e7b561a5fd2bb", expand=False, url="https://files.pythonhosted.org/packages/8d/be/91992c317dcab51706418636e13387bb21a610f5b62dfe6bc54d59bc72b3/flake8_docstrings-1.2.0-py2.py3-none-any.whl")
	version("1.3.0", sha256="8436396b5ecad51a122a2c99ba26e5b4e623bf6e913b0fea0cb6c2c4050f91eb", expand=False, url="https://files.pythonhosted.org/packages/4e/ab/927dada116644e776c2668175d35545786f8a5120a9bdbfaaba2aab71687/flake8_docstrings-1.3.0-py2.py3-none-any.whl")
	version("1.3.1", sha256="3ad372b641f4c8e70c7465f067aed4ff8bf1e9347fce14f9eb71ed816db36257", expand=False, url="https://files.pythonhosted.org/packages/e0/74/d4e05e94704b8970b5c714350d7da10ee62ab40077b7498c53a3d888b212/flake8_docstrings-1.3.1-py2.py3-none-any.whl")
	version("1.4.0", sha256="1666dd069c9c457ee57e80af3c1a6b37b00cc1801c6fde88e455131bb2e186cd", expand=False, url="https://files.pythonhosted.org/packages/9f/67/01b706429d17acdbe299ec1a077bd38f4323334a9485b85b8b8534a46c61/flake8_docstrings-1.4.0-py2.py3-none-any.whl")
	version("1.5.0", sha256="a256ba91bc52307bef1de59e2a009c3cf61c3d0952dbe035d6ff7208940c2edc", expand=False, url="https://files.pythonhosted.org/packages/d3/28/131f81bd93071b29e8c5ce9cfd5d58793a4071537e6d9f58bebe6b185039/flake8_docstrings-1.5.0-py2.py3-none-any.whl")
	version("1.6.0", sha256="99cac583d6c7e32dd28bbfbef120a7c0d1b6dde4adb5a9fd441c4227a6534bde", expand=False, url="https://files.pythonhosted.org/packages/8b/ad/35dc9b3585ddbab617679b97487450f873e582408843c07fe97f524463c2/flake8_docstrings-1.6.0-py2.py3-none-any.whl")
	version("1.7.0", sha256="51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75", expand=False, url="https://files.pythonhosted.org/packages/3f/7d/76a278fa43250441ed9300c344f889c7fb1817080c8fb8996b840bf421c2/flake8_docstrings-1.7.0-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-flake8", type=("build", "run"))
	depends_on("py-pydocstyle", type=("build", "run"))
	depends_on("python@2", when="@0.2.1.post1-py2", type=("build", "run"))
	depends_on("python@2", when="@0.2.2-py2", type=("build", "run"))

# {'flake8': ['0.2.1.post1-py2', '0.2.2-py2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '1.0.1', '1.0.2', '1.0.3', '1.1.0', '1.2.0', '1.3.0', '1.3.1'], 'pep257': ['0.2.1.post1-py2', '0.2.2-py2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8'], 'pydocstyle': ['1.0.1', '1.0.2', '1.0.3'], 'flake8-polyfill': ['1.0.3', '1.1.0', '1.2.0', '1.3.0', '1.3.1'], 'pydocstyle(>=2.0)': ['1.1.0', '1.2.0'], 'pydocstyle(>=2.1)': ['1.3.0', '1.3.1', '1.4.0', '1.5.0', '1.6.0', '1.7.0'], 'flake8(>=3)': ['1.4.0', '1.5.0', '1.6.0', '1.7.0']}