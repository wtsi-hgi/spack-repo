# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEnum34(PythonPackage):
	"""Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4"""
	
	homepage = "https://bitbucket.org/stoneleaf/enum34"
	pypi = "enum34/enum34-1.1.9-py3-none-any.whl" 

	version("0.9", sha256="e4ea8c4e1b66c1c13f9ce342312f1c78fb8c7a28c7533f32a6df902a660927a6")
	version("0.9.1", sha256="48ec8e5e9b04481e89323818b48c797be05119c8726c2dd154d8eb32bcca9997")
	version("0.9.11", sha256="bbbfe3f5bd981bf59b41861550222b021c088f3580ed573c6262534654bb5e1b")
	version("0.9.12", sha256="ceb990c2c67d1f51c652828be5a4454f516109c67c6fe7493fa05ecc688837c0")
	version("0.9.13", sha256="da3331aae6aab862eb08f4fb481aef63c04f28de7e5501639e681511df165b0d")
	version("0.9.14", sha256="ed76884d723fb5e4dd68b7204c507a04f944fee5e25fd14374660bf87dd98b74")
	version("0.9.15", sha256="05e033fd46d8f9809d5f1a014e743b8ddc3b9e739c5de394bdd25b231b0ed0b6")
	version("0.9.16", sha256="9fd8f65c278e7f1423bea65fedefd93aef1be60353a1c28ea58683a9cfed1fb6")
	version("0.9.17", sha256="00a3e1a3c4c78fe43a1c6982792f2a2076bc072f70a387d480314ec26523fabd")
	version("0.9.18", sha256="099e6f584169876cd7305aaf57fdcc541a4802184fd71988606cea360ea5d06f")
	version("0.9.19", sha256="b6b9f3da58ff8de7a94df71df52e614db111805e8a81d9cbea9f73a37fc3253c")
	version("0.9.20", sha256="3e78854c02f901a2df45bd7f9ab6a84de4ac70740f4f69a5e3413308b19fb906")
	version("0.9.21", sha256="5589918b0366a5b8f6c615a50f75bf0c09ba428a7cd4f147a7df536472f24e64")
	version("0.9.22", sha256="6cb3edeb46768793d46290301dc4a0abbf2cf5cf3437017c4569a8aa734f42f9")
	version("0.9.23", sha256="2a0951adbb02465b727d768dc2a3d94249fc91d5df6b3338c285d7636b46dc21")
	version("1.0", sha256="35b14cfc9d45aaeae0b1b6092eb8597a53c84c8143002b6e9cc43043f9f7d47d")
	version("1.0.1", sha256="574813801def588d254fc788726446e956aa860a030ad4f9327195268b50fdd2")
	version("1.0.2", sha256="76323030e6b47e2c0e2b15c43aa00931566bf002868ca29e3c312f70fb7f4317")
	version("1.0.3", sha256="f89ab33ab767674806824b6f36637170d968285a76ef301cb2a33e4eb8060dde")
	version("1.0.4", sha256="7583d80aca2a2b2a8a411f141c4d744de06a6bc43a32253f6b81d14d48f6c90e")
	version("1.1.0", sha256="9e4c1fe67c2cc884d747724eebcb94822b1c2d16411ff15eb0686d9b302ae377")
	version("1.1.1", sha256="4d33459c33254e1badcfdb47a340a801cd80466e46fbe35d25d308bf148dad70")
	version("1.1.10-py2", sha256="a98a201d6de3f2ab3db284e70a33b0f896fbf35f8086594e8c9e74b909058d53", expand=False, url="https://files.pythonhosted.org/packages/6f/2c/a9386903ece2ea85e9807e0e062174dc26fdce8b05f216d00491be29fad5/enum34-1.1.10-py2-none-any.whl")
	version("1.1.10", sha256="c3858660960c984d6ab0ebad691265180da2b43f07e061c0f8dca9ef3cffd328", expand=False, url="https://files.pythonhosted.org/packages/63/f6/ccb1c83687756aeabbf3ca0f213508fcfb03883ff200d201b3a4c60cedcc/enum34-1.1.10-py3-none-any.whl")
	version("1.1.2", sha256="35907defb0f992b75ab7788f65fedc1cf20ffa22688e0e6f6f12afc06b3ea501")
	version("1.1.3-py3.5", sha256="994fe36b8fa494e37e60d3edefbd11c08dc2f884e26e35e71527f7e984890810", expand=False, url="https://files.pythonhosted.org/packages/03/ef/643b63a6b93d77d2806744b983c67a45d7267c37dca34cc1a32695b95b99/enum34-1.1.3-py2.py3-none-any.whl")
	version("1.1.4-py3.5", sha256="fb882434f2ae319f454b6b5d07bfac73104a16c1fcdbb30c3cef70df216610e9", expand=False, url="https://files.pythonhosted.org/packages/30/3c/7b6debc06c8f6bbfa20104fa31aeaae4a425e45c51f3522d87e35dcfc910/enum34-1.1.4-py2.py3-none-any.whl")
	version("1.1.5-py3.5", sha256="01a4abc326ead6c92169ab8c6f6af3cff9706a6a047c8738168f7a50b8def231", expand=False, url="https://files.pythonhosted.org/packages/a6/4b/d2614fef376fcc5d0de1e86d1758c75ef79eda345ecfa07e0d16676706c3/enum34-1.1.5-py2.py3-none-any.whl")
	version("1.1.6-py2", sha256="6bd0f6ad48ec2aa117d3d141940d484deccda84d4fcd884f5c3d93c23ecd8c79", expand=False, url="https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl")
	version("1.1.6", sha256="644837f692e5f550741432dd3f223bbb9852018674981b1664e5dc339387588a", expand=False, url="https://files.pythonhosted.org/packages/af/42/cb9355df32c69b553e72a2e28daee25d1611d2c0d9c272aa1d34204205b2/enum34-1.1.6-py3-none-any.whl")
	version("1.1.8-py2", sha256="075e6c23fbf537eaf379ebe17dbcb65a4f2d2ecd03ac5a3ac534c313afbdfa33", expand=False, url="https://files.pythonhosted.org/packages/f0/43/55233ddb2e5f8fc6288147155faac30c404f039a7177c662044148da0989/enum34-1.1.8-py2-none-any.whl")
	version("1.1.8", sha256="cffbadfe6cd17ea2408adb8bb21b12bd30dd0d15de90af44e1dd4b60435993e2", expand=False, url="https://files.pythonhosted.org/packages/28/6e/ff8465d953994e0df78d636ac7ed76b10e52e9777f947124f8f2951cbb5d/enum34-1.1.8-py3-none-any.whl")
	version("1.1.9-py2", sha256="98df1f1937840b7d8012fea7f0b36392a3e6fd8a2f429c48a3ff4b1aad907f3f", expand=False, url="https://files.pythonhosted.org/packages/bf/04/c2ab08074863e385ba27068f2da9df5e61e732664b0f932d396bbf46015b/enum34-1.1.9-py2-none-any.whl")
	version("1.1.9", sha256="708aabfb3d5898f99674c390d360d59efdd08547019763622365f19e84a7fef4", expand=False, url="https://files.pythonhosted.org/packages/df/6e/46a0304561a07bda942c4283b67228d5b87d1ebd1189c866ede4b4cd6a0a/enum34-1.1.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@2", when="@1.1.10-py2", type=("build", "run"))
	depends_on("python@3..5", when="@1.1.3-py3.5", type=("build", "run"))
	depends_on("python@3..5", when="@1.1.4-py3.5", type=("build", "run"))
	depends_on("python@3..5", when="@1.1.5-py3.5", type=("build", "run"))
	depends_on("python@2", when="@1.1.6-py2", type=("build", "run"))
	depends_on("python@2", when="@1.1.8-py2", type=("build", "run"))
	depends_on("python@2", when="@1.1.9-py2", type=("build", "run"))
