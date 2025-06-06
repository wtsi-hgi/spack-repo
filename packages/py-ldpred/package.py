# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLdpred(PythonPackage):
	"""A Python package that adjusts GWAS summary statistics for the effects of linkage disequilibrium (LD)"""
	
	homepage = "https://github.com/ldpred"
	pypi = "ldpred/LDpred-1.0.9-py3-none-any.whl" 

	version("0.9.0", sha256="fc43d80ae3fca190febde60085c338510f3e3abdf03533e85f8a2dbc03c62bb2", expand=False, url="https://files.pythonhosted.org/packages/84/61/5cb5bd9382ca61ded04aa7ca4c4946509b9d71ed8f5ffe001d5390d50f38/LDpred-0.9.0-py2.py3-none-any.whl")
	version("0.9.01", sha256="b1b9f8c8e939dc691fec951001a465a797fff4d1796072769ddd9018c6f2618c", expand=False, url="https://files.pythonhosted.org/packages/81/be/674d40397ef9ff46fa79508901f0b4a156e44aec083103403e06921c43a2/LDpred-0.9.01-py2.py3-none-any.whl")
	version("0.9.02", sha256="c7f5465dd1dc350196b20a5da1334758d17e4cb3c914436d8ba6a64f51ab9853", expand=False, url="https://files.pythonhosted.org/packages/5f/45/de415577024f2330a2c83f23a5bbf8750fc7d0c169a60e9a1d4d1e1b18fb/LDpred-0.9.02-py2.py3-none-any.whl")
	version("0.9.03", sha256="08e9de08c3c0071af85d10ea0d0b62af9a047b25b49786902aed3adf0f088308", expand=False, url="https://files.pythonhosted.org/packages/39/33/fdcfdd7f6b38dc933734250c9c7d749df8febc469453aeb2e64d286bb0db/LDpred-0.9.03-py2.py3-none-any.whl")
	version("0.9.04", sha256="6a8d9afc570df9a361c98887de070e540099dbc69c04d98a66c64cb518aab26c", expand=False, url="https://files.pythonhosted.org/packages/34/1f/374eb0c5f9cc24db39e890f5167fb0c4c578b2caf4f95894bd07588a2bf0/LDpred-0.9.04-py2.py3-none-any.whl")
	version("0.9.05", sha256="91bc7e968f93832918700b38c57cc2dea4c289a81f4fbaf4a734537b694325e7", expand=False, url="https://files.pythonhosted.org/packages/a2/27/0e4f9b57309b2eaef0cc1f38c52f7d2effc6ce9b92c2123061197cd0557c/LDpred-0.9.05-py2.py3-none-any.whl")
	version("0.9.06", sha256="9ab3f2cb9f5124d42e4653c84f4fd0e2d6771dabfa7b1e3bbd18fe8b883541fd", expand=False, url="https://files.pythonhosted.org/packages/96/ac/36f7f3f6bd40aec8fea2068218f20fb09fcdda1861fdacd519f50d341f1b/LDpred-0.9.06-py2.py3-none-any.whl")
	version("0.9.07", sha256="def2ccef5777b54afc4cfeaa768d31f5a99dbc3c7dd419d1d82405454e650467", expand=False, url="https://files.pythonhosted.org/packages/ae/ee/6fd61bb6f1c533a55b28e33704e8b6792c6db0618f06cb3de9ab6455241a/LDpred-0.9.07-py2.py3-none-any.whl")
	version("0.9.08", sha256="9dc67fe5d48706f2ae1eea1635319ccc05805bd72a51241c1a7df457f801d79f", expand=False, url="https://files.pythonhosted.org/packages/cb/ae/ed9f5e5f15496ee2566ef11d4ecb96279da8466a93c507ff93b6c40349c9/LDpred-0.9.08-py2.py3-none-any.whl")
	version("0.9.09", sha256="903079c935f9c6ae8ebce4260349f0fc6831d0fed295bbda0fe780f7eb4106f1", expand=False, url="https://files.pythonhosted.org/packages/85/4b/2e42d9181d9d06f060efa36b7053ac54f761132f093b0f29d1492711be3b/LDpred-0.9.09-py2.py3-none-any.whl")
	version("1.0.0-py2", sha256="6384d00a0f1abefe29367da415e2232917af1599d9119f70bfb64f1eb5d2a25c", expand=False, url="https://files.pythonhosted.org/packages/d9/cc/8005283df6034520aaefbb5ffc0d463adc30baeca09fade6ea2edd2e0ae4/LDpred-1.0.0-py2-none-any.whl")
	version("1.0.0", sha256="57ca356095853fd477a395fabd590906bf6118cc2e70eaa23a9f554b2a525dbd", expand=False, url="https://files.pythonhosted.org/packages/28/cc/2a1d44faef1d51790a162a973fd0638612f3d6e807588a2505ea8af13985/LDpred-1.0.0-py3-none-any.whl")
	version("1.0.10-py2", sha256="bc4077d262e2ddca51d6d37c0a1a326181b01d9bc0079ba2a06bbd9f102f0ae4", expand=False, url="https://files.pythonhosted.org/packages/13/53/41a4d4d9931e935264bc7de533d6edb8470c7af549bcb709c8de487faea2/LDpred-1.0.10-py2-none-any.whl")
	version("1.0.10", sha256="43025e477f8878789c102e7e0aef0555802db71b6cd48868d33d9a5fc1c4c17b", expand=False, url="https://files.pythonhosted.org/packages/fa/75/9347837d597164d6d34ef6213bbdc2fd3382f5916f55ddded46b162d796a/LDpred-1.0.10-py3-none-any.whl")
	version("1.0.11-py2", sha256="b1ceeeb828613e76ae73dda490229b1337ccf688963804c4bcb86328d9771db8", expand=False, url="https://files.pythonhosted.org/packages/6e/8b/0563be8dfcd23619b9f1a80ddeaef3f2a453e55391d42100d5cf4811f049/LDpred-1.0.11-py2-none-any.whl")
	version("1.0.11", sha256="1adff28d0fe01792f01f1bd41bc7dd3b0057279c621613fb7bf4a5ba103b89db", expand=False, url="https://files.pythonhosted.org/packages/6f/9f/0f9f47441e5f8c08fd04d0122f973db3b9630de34a14e3c04fabe768969f/LDpred-1.0.11-py3-none-any.whl")
	version("1.0.2", sha256="29904547d347bb342d7e8030ddcf757ae0d067acedfd970f757e65e1a5f89bdf", expand=False, url="https://files.pythonhosted.org/packages/60/b9/3b0ce25a09d757e6cf14bb936c23275ae06e43fc3aa3a38c028068ad4c67/LDpred-1.0.2-py3-none-any.whl")
	version("1.0.3-py2", sha256="aba7073613bcf4cdd2940092ea90a7e8d3575369e59c7aaaf69b6752017c4b92", expand=False, url="https://files.pythonhosted.org/packages/d0/82/7efc40fe2e82aa3e3dcb020747ae946c3ee1fc7816d97fc4c93fadd4c5b4/LDpred-1.0.3-py2-none-any.whl")
	version("1.0.4-py2", sha256="55252288989e9cb652f335e61e2338c86fd2c1e38de2d63dd4bfe62dec9d74c7", expand=False, url="https://files.pythonhosted.org/packages/e6/7e/cb29987ec12da6e27afe754f802e88074a6c2745fcbac03db2497cb1cbbe/LDpred-1.0.4-py2-none-any.whl")
	version("1.0.4", sha256="8100742632127d06917b7840465c2a9913ecbda17e49972a070e55e37742bfb7", expand=False, url="https://files.pythonhosted.org/packages/99/9d/736100addfc95d8e9eb36972baf1b76a821340b5f83b8b930c80e621a88d/LDpred-1.0.4-py3-none-any.whl")
	version("1.0.5", sha256="d537831d04d45d79a7050f9b5788519b39d5223452fe3e5d7b9669c15111f65a", expand=False, url="https://files.pythonhosted.org/packages/60/87/4d064297ebaa480ce7d9676720b2b32c78b6fded017996e4e849e364765c/LDpred-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="fd3a0a62b80dedd0cc707e295a99a92cd814c45e6a8356be15729593bd09b622", expand=False, url="https://files.pythonhosted.org/packages/b9/a1/427d7199a0961dc83e023d40cea0bf1295030c7ec4a0b77b60d99a42df0b/LDpred-1.0.6-py3-none-any.whl")
	version("1.0.7", sha256="c3bc199656aeb32819916ab6cd24c2b3f14d4e1a54e10566188eb5e8dd1d4e77", expand=False, url="https://files.pythonhosted.org/packages/f7/e4/83daa4dc0a8eccffafcda28417fb4ad5b887d68e6fce9dfb277860ed7f16/LDpred-1.0.7-py3-none-any.whl")
	version("1.0.8-py2", sha256="f23ec532f8a502f1b871339c60b122d0555f3c359e2ac3e05eca47e4eed4dbdc", expand=False, url="https://files.pythonhosted.org/packages/4c/2b/638268268763ce3b1c9982705eef242c86fd4dbb9b95d7f00a07839d128a/LDpred-1.0.8-py2-none-any.whl")
	version("1.0.8", sha256="94ac726a89e78c048bedfe86e0887443c233baca8ea31cb59e39ccb0f3249e2a", expand=False, url="https://files.pythonhosted.org/packages/a3/0f/e3f26cb34c851673fb29650c84bd12bc1be06d5147c26c261e1c0ab5a218/LDpred-1.0.8-py3-none-any.whl")
	version("1.0.9-py2", sha256="e975e8d45e58af485b9547e402ab03f44d5b52776b2dbed9e38e024fce398315", expand=False, url="https://files.pythonhosted.org/packages/c6/b2/138c89d1e000de99678a5ed7e920695b808c1f6eab7affe28124ab4f8972/LDpred-1.0.9-py2-none-any.whl")
	version("1.0.9", sha256="05bfde624dbd76e4bbe994a7ae642bd82ce4aa477c8aa18cbf70e75c0cf55f54", expand=False, url="https://files.pythonhosted.org/packages/44/6d/c7af357735e269d0a7eeaeea2ce237ce0bc05aa8aafea4d2859a5955a827/LDpred-1.0.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-plinkio", type=("build", "run"))
	depends_on("python@2", when="@1.0.0-py2", type=("build", "run"))
	depends_on("python@2", when="@1.0.10-py2", type=("build", "run"))
	depends_on("python@2", when="@1.0.11-py2", type=("build", "run"))
	depends_on("python@2", when="@1.0.3-py2", type=("build", "run"))
	depends_on("python@2", when="@1.0.4-py2", type=("build", "run"))
	depends_on("python@2", when="@1.0.8-py2", type=("build", "run"))
	depends_on("python@2", when="@1.0.9-py2", type=("build", "run"))

# {'h5py': ['0.9.0', '0.9.01', '0.9.02', '0.9.03', '0.9.04', '0.9.05', '0.9.06', '0.9.07', '0.9.08', '0.9.09', '1.0.0-py2', '1.0.0', '1.0.10-py2', '1.0.10', '1.0.11-py2', '1.0.11', '1.0.2', '1.0.3-py2', '1.0.4-py2', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8-py2', '1.0.8', '1.0.9-py2', '1.0.9'], 'plinkio': ['0.9.0', '0.9.01', '0.9.02', '0.9.03', '0.9.04', '0.9.05', '0.9.06', '0.9.07', '0.9.08', '0.9.09', '1.0.0-py2', '1.0.0', '1.0.10-py2', '1.0.10', '1.0.11-py2', '1.0.11', '1.0.2', '1.0.3-py2', '1.0.4-py2', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8-py2', '1.0.8', '1.0.9-py2', '1.0.9'], 'scipy': ['0.9.0', '0.9.01', '0.9.02', '0.9.03', '0.9.04', '0.9.05', '0.9.06', '0.9.07', '0.9.08', '0.9.09', '1.0.0-py2', '1.0.0', '1.0.10-py2', '1.0.10', '1.0.11-py2', '1.0.11', '1.0.2', '1.0.3-py2', '1.0.4-py2', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8-py2', '1.0.8', '1.0.9-py2', '1.0.9']}