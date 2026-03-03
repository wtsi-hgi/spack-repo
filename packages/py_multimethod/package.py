# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMultimethod(PythonPackage):
	"""Multiple argument dispatching."""
	
	homepage = "https://github.com/coady/multimethod"
	pypi = "multimethod/multimethod-2.0rc2-py3-none-any.whl" 

	version("0.4", sha256="30848df6a30cd904559430bfd001e97a385f4642d2bde1ca2ebf61c9582682ba")
	version("0.5", sha256="2ddba71265cb51dfd3d078b86b2bf57d47426ccf810bd2a695dfcce75526083d")
	version("0.6-py2.7", sha256="d6e57443e877b9c565eff107de760029e78c7432286cbad155ae1ec0b918f1dd", expand=False, url="https://files.pythonhosted.org/packages/ff/f6/ac4366395cd56dd562503c795da6fc4ab72a4d23007418c1d5263f1f3193/multimethod-0.6-py2.py3-none-any.whl")
	version("0.7", sha256="0c0efff31315fd5f9716e68c6b94955187462ae0a5861a7494f51dc63081c052", expand=False, url="https://files.pythonhosted.org/packages/29/e8/8c1c31b246a1434d7860936a49dd2e7e74f6fb5f169b6e288308b3f37adf/multimethod-0.7-py2.py3-none-any.whl")
	version("0.7.1", sha256="726cd6a07f68c5e0fdb504983ccb6cf9ce10cea58cad67195cc99ea84169f941", expand=False, url="https://files.pythonhosted.org/packages/9f/cc/c27b64aebe905be8ea57841a04c67e8fcc528e41568ff5b4aab146b18a3d/multimethod-0.7.1-py2.py3-none-any.whl")
	version("1.0", sha256="5f20db508dfb95aa2b135299a436a68342ccfc2c275b6636b6306de435c01d66", expand=False, url="https://files.pythonhosted.org/packages/d0/98/4c9a1fe8c0383e944efcb0e9b157ea253f49ec691f310c484b1a8b8585d5/multimethod-1.0-py2.py3-none-any.whl")
	version("1.1", sha256="f15271ebd98ac5d4bd1bc7445d0b71d134d4642d62f253711774733943d499ef", expand=False, url="https://files.pythonhosted.org/packages/4f/9c/c321effe4a47e92b3a7fcd72f1375300d2b38138ec77b4f5afd84b8e0755/multimethod-1.1-py2.py3-none-any.whl")
	version("1.10", sha256="afd84da9c3d0445c84f827e4d63ad42d17c6d29b122427c6dee9032ac2d2a0d4", expand=False, url="https://files.pythonhosted.org/packages/7f/bd/750245e47e7f307d9f94d4fa84727f4ed9956005dfa671d58be1d531a0f6/multimethod-1.10-py3-none-any.whl")
	version("1.11", sha256="e57253f5b6d530b10696843e693c11f0dadbe299a327bd71cdf3edd0019a3853", expand=False, url="https://files.pythonhosted.org/packages/b6/71/42263a6b7555ec36799b39095b93e6097da61e2c184edb8bed5924493682/multimethod-1.11-py3-none-any.whl")
	version("1.11.1", sha256="939703e1667725169722269f3bb6d078ce414526a16475028ea3eb3b8a5fc4ef", expand=False, url="https://files.pythonhosted.org/packages/59/ee/4ad7cf6e8c0218d7b0f0b1ccb4795a9cf7724fe79717e22849cfa69ea0ad/multimethod-1.11.1-py3-none-any.whl")
	version("1.11.2", sha256="cb338f09395c0ee87d36c7691cdd794d13d8864358082cf1205f812edd5ce05a", expand=False, url="https://files.pythonhosted.org/packages/a0/96/47dc456936530adb1360aba7300f2da2e1d277fb361e025db3926653e189/multimethod-1.11.2-py3-none-any.whl")
	version("1.12", sha256="fd0c473c43558908d97cc06e4d68e8f69202f167db46f7b4e4058893e7dbdf60", expand=False, url="https://files.pythonhosted.org/packages/af/98/cff14d53a2f2f67d7fe8a4e235a383ee71aba6a1da12aeea24b325d0c72a/multimethod-1.12-py3-none-any.whl")
	version("1.2", sha256="80b434bb049c2ae7f9dda29a0d20da97deb20a174353721fb91a312c63ef267d", expand=False, url="https://files.pythonhosted.org/packages/95/ab/f6ab079fafa46eabc33be775be5b349aa1fc195537310b0f531932df1bc7/multimethod-1.2-py2.py3-none-any.whl")
	version("1.3", sha256="6928d577bbf4fbd3475b8fb13cfcad9d46885d32806f6be0b52da89a30116043", expand=False, url="https://files.pythonhosted.org/packages/47/01/c0570b8bcac36c752b4c458d74fabc707fa078c464f25b1c1f0fcd247c9a/multimethod-1.3-py2.py3-none-any.whl")
	version("1.4", sha256="2746500793c64cbd84a6ccda0043f4b58af3fcf8d6cd44b2232d5b9455b31d73", expand=False, url="https://files.pythonhosted.org/packages/7a/d0/ce5ad0392aa12645b7ad91a5983d6b625b704b021d9cd48c587630c1a9ac/multimethod-1.4-py2.py3-none-any.whl")
	version("1.5", sha256="889bcc8feb34181fbfa70f78e92f4c1927f0361e5decef0d2770b6ed7984c41c", expand=False, url="https://files.pythonhosted.org/packages/13/4e/899c33da18671c2cf47f0d43b232fc220d465e37e90d7a151c261779416b/multimethod-1.5-py3-none-any.whl")
	version("1.6", sha256="24cf77b560266869d489c150d36d9242d66d4adc360df4548d09ee976c735d1e", expand=False, url="https://files.pythonhosted.org/packages/5b/94/bfe9a0f68152118e805bdada61eb1259cd703f9d4bab747495aacce7af1d/multimethod-1.6-py3-none-any.whl")
	version("1.7", sha256="c9ed3841ddb5ca314ad12ca88d64e4a75d283e98f16622b580bb90fe72f79231", expand=False, url="https://files.pythonhosted.org/packages/e7/c7/5bf64fed1c1c8a39214ba6331ed62219faf760a7e26acf914f6a6a53936a/multimethod-1.7-py3-none-any.whl")
	version("1.8", sha256="ebff0b254d9373b587a99fdd5c238fc0e76861b802704a56d9a71d78aa7d097f", expand=False, url="https://files.pythonhosted.org/packages/c4/ec/37cea832bed328a022c6381e7e6cfa8bdb1d0dc1ec69470ff81433f2ad91/multimethod-1.8-py3-none-any.whl")
	version("1.9", sha256="59cb8ffec7449bd5557993c8d84e788fe04aca9c94b3b181ba8429ab954c24df", expand=False, url="https://files.pythonhosted.org/packages/f2/77/8c31f7c97aa6ae78a8843b43aeb0e4e301e2b23e04f237f0c4a16f531b72/multimethod-1.9-py3-none-any.whl")
	version("1.9.1", sha256="52f8f1f2b9d5a4c7adfdcc114dbeeebe3245a4420801e8807e26522a79fb6bc2", expand=False, url="https://files.pythonhosted.org/packages/21/91/01ec16d3d0cadb499b83e6f6435c63e43f3c122c146d82a4eb9575169817/multimethod-1.9.1-py3-none-any.whl")
	version("2.0", sha256="45aa231dc9dbb7f980c0f2ad8179e2c2b72a8cd5c7d7534337be66dde29d35be", expand=False, url="https://files.pythonhosted.org/packages/84/42/a285fc4b89b3a249538954779cd4082a85bf35dc7d0a9c93e48e146e3dc7/multimethod-2.0-py3-none-any.whl")
	version("2.0rc1", sha256="85f4ad13301a2445e868842493975525d8c4270b737db70729422e5902fe847a", expand=False, url="https://files.pythonhosted.org/packages/e5/e0/9908bd826ecf10ab39e3c76415b41db03d0444b2b4e4682a69db57a3b1c9/multimethod-2.0rc1-py3-none-any.whl")
	version("2.0rc2", sha256="462ee2365decfe80f8da15ebb4f9611fbfe53487e93895759fa037d25da68f9a", expand=False, url="https://files.pythonhosted.org/packages/08/cf/5d998ce32a5c6b7a3b2c8e87121639a36fa9e1931971d8ec73bbc3f91738/multimethod-2.0rc2-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("python@2..7", when="@0.6-py2.7", type=("build", "run"))

# {"m2r;extra=='docs'": ['1.0', '1.1', '1.2', '1.3'], "nbsphinx;extra=='docs'": ['1.0', '1.1', '1.2', '1.3', '1.4'], "jupyter;extra=='docs'": ['1.0', '1.1', '1.2', '1.3', '1.4'], "recommonmark;extra=='docs'": ['1.4'], "sphinx;extra=='docs'": ['1.4']}