# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythonDebian(PythonPackage):
	"""Modules to read and manipulate many file formats related to Debian packages and repositories"""
	
	homepage = "https://salsa.debian.org/python-debian-team/python-debian"
	pypi = "python-debian/python_debian-1.0.1-py3-none-any.whl" 

	version("0.1.13", sha256="620dfa4ce886b6ccf081d821aec14b8da1c0b111d8c8a59c5057032945c482ff")
	version("0.1.16", sha256="69e2673b33bb8c281031860234dce4aec2ae2a6dfa4ce0adc9f52318121dd38f")
	version("0.1.21", sha256="1e6447da1fcc2d7654d4d26e1e7cfc7086824ab010985ddef234c01d5255744a")
	version("0.1.21-nmu2", sha256="2c2cfeef00ea77bd6cff8591c1bc768d2d0099f064e61af634e4da9998623e69")
	version("0.1.23", sha256="d07a0fd581f36d35eab5d95517fb0fd8bf044d8ddff39052b18349cbed576ea4")
	version("0.1.28", sha256="1e4441548598b8dfd2b61bc36db64bfa5a7b93a65ae04641d3e998fe3b702544")
	version("0.1.30", sha256="57c3a9b090cb06916ca44cbbe808db3aea809c11b9ade8a32f2e4b90223a2f55")
	version("0.1.31", sha256="21465ccb8a4cb2942f15e74b6c9b92caff5188365e22ab4a0dcc778b90f28479")
	version("0.1.32-py2.7", sha256="e04236a3c450fbaeb827d41a91acd3d76fe963106eb8457c9139e66988003ffc", expand=False, url="https://files.pythonhosted.org/packages/d4/5c/5ab46d0908194d7103f474c1f16d0897917e4d743b30b2646e421bd6272d/python_debian-0.1.32-py2-none-any.whl")
	version("0.1.32-py3.6", sha256="c755d34ff4767b4357290e76df7baa5add365c4ceaefcc96fd96af71bd1e691b", expand=False, url="https://files.pythonhosted.org/packages/22/80/842401926947938551b4e1114729c60513f76021dfc9da81876f1c037ade/python_debian-0.1.32-py3-none-any.whl")
	version("0.1.33-py2", sha256="4d0ea7d47a6e035125c18a666aad3910207b571eaba28deff67dbad581b7dee6", expand=False, url="https://files.pythonhosted.org/packages/72/bf/3b9d427268e2195aa35b44e0550a385c07a217a75db3d05c1d4130a435bd/python_debian-0.1.33-py2-none-any.whl")
	version("0.1.33", sha256="3eaf8d71e95e3afae9581b544b293952136bdc5f3a0514bc7e75edac78eb598f", expand=False, url="https://files.pythonhosted.org/packages/f5/7a/5b1bcb2e247e8c1cd615cfb4796a09fe6fe5b87e643b64562401ce709d2c/python_debian-0.1.33-py3-none-any.whl")
	version("0.1.34-py2", sha256="9336ce85af476577eb59a01f9a4b65abe13b63bb43f448d51f9c4f4a83c7ee49", expand=False, url="https://files.pythonhosted.org/packages/89/d2/db1948b464dbaab6d4a07caff9649df2817588f58423d4ec32a19407cfe3/python_debian-0.1.34-py2-none-any.whl")
	version("0.1.34", sha256="1e241f05d322f4bf6c9e89819ec4ee0dfe52f4fbb7a60e86dcae1df028dba46e", expand=False, url="https://files.pythonhosted.org/packages/ee/62/aa8541e8ef0ccd5ab1dcc0221a8e3cb41c6e99a55c0bfd5cad454a609188/python_debian-0.1.34-py3-none-any.whl")
	version("0.1.35-py2", sha256="a5d47a93f796c9ed7ffd1f299fde9661ab418bc511f601e198a87644aec6899d", expand=False, url="https://files.pythonhosted.org/packages/e1/50/4e7820e6f33a2d37d9f38f7536f549f0676a906bcbdd8cc8edb2e264b293/python_debian-0.1.35-py2-none-any.whl")
	version("0.1.35", sha256="d7d7cc91cf4489b4a403a05babea7116639556b41b409b5c41e6552d826054af", expand=False, url="https://files.pythonhosted.org/packages/f7/de/99f748743e7ced2f649ad3402e790bf039edf717ff521995f35d76bae6c7/python_debian-0.1.35-py3-none-any.whl")
	version("0.1.36-py2", sha256="de84efec1a581e28240de6e71b0a83180f3390eb436d0cd891c848aeb28a2518", expand=False, url="https://files.pythonhosted.org/packages/ed/18/efc2f96555d351cd1504f68119921fb1482de7b3c973c4ff4ecaa23e0877/python_debian-0.1.36-py2-none-any.whl")
	version("0.1.36", sha256="075ab2d3a948d1a3a8833bb5838a8b59a06c3f41b80c0e2905cd00ef6f848e41", expand=False, url="https://files.pythonhosted.org/packages/87/49/a34a602141db50b101a25d1f256b33cfb7b406bafd0f00e071a5f7424c92/python_debian-0.1.36-py3-none-any.whl")
	version("0.1.37", sha256="847890c158ae77f3d09bc6da10ae6cb4f2c2a5fb6d874528c6e076417d5fd333", expand=False, url="https://files.pythonhosted.org/packages/df/16/73231f1220277b90930bed6480bee079c62cab982c64a38df4f4460ffbea/python_debian-0.1.37-py3-none-any.whl")
	version("0.1.38", sha256="a1f89336d7675a56cdd92fa90cd8c00b9178dabcc6d3e08a397e80eca2b855f3", expand=False, url="https://files.pythonhosted.org/packages/4d/a4/4baa4acf0cb626fc4e4542001dbfb0d0821fd1429d3cdd8b28dbca77e8b8/python_debian-0.1.38-py3-none-any.whl")
	version("0.1.39", sha256="338951c25091ad88cf23a7621c2e15e5212efa66bc364d3e236a0e25aec935d2", expand=False, url="https://files.pythonhosted.org/packages/b2/11/31111df3b1c4832e8d171d20e64c77aebab9922700b007d3f479742f5cf6/python_debian-0.1.39-py3-none-any.whl")
	version("0.1.40", sha256="55d33ff6d78be995aba5a14a82d83aae8a8f5bb9a36712796dac179cc68fab0c", expand=False, url="https://files.pythonhosted.org/packages/8e/e7/76511f73344cea6e7a9d7f431bd0dcfda5871157713ecded06d58a59eb1b/python_debian-0.1.40-py3-none-any.whl")
	version("0.1.42", sha256="3945dc4f9cbc0b56985e806c8c6934657a63e91d48a850b2ccde287c5a873fd4", expand=False, url="https://files.pythonhosted.org/packages/c4/22/26bc493c5f7e9bf1eedfe7d67c8fcb1d7ec39f2c6366c6649fbde97a73eb/python_debian-0.1.42-py3-none-any.whl")
	version("0.1.43", sha256="0cc0e09434c019d8f6380d1ce965de2a1e51b454f0b2fb86469486556594cbfc", expand=False, url="https://files.pythonhosted.org/packages/75/33/e3ecf48b7d5673a567aeb3a719f03c005dd6066bcbec52d522f424cacbc7/python_debian-0.1.43-py3-none-any.whl")
	version("0.1.44", sha256="11bd6f01c46da57982bdd66dd595e2d240feb32a85de3fd37c452102fd0337ab", expand=False, url="https://files.pythonhosted.org/packages/15/5f/900c3fe35e94cf93aafbc7a8fbaf88bc010c11187e47d415376e064ae3f6/python_debian-0.1.44-py3-none-any.whl")
	version("0.1.47", sha256="3209ba3602bfe429e695c00d64e00d695dc93c26cfa9b53ff3656469bc3fa5b5", expand=False, url="https://files.pythonhosted.org/packages/0f/79/5394a7dd19409d588476e848eadf45488d5fdcacb09cc5c5c788249f88dc/python_debian-0.1.47-py3-none-any.whl")
	version("0.1.48", sha256="00edb2c95a9e28e17067c055d17a66e90abf9d7c80cfda93095e7193e5ae58c3", expand=False, url="https://files.pythonhosted.org/packages/f2/a1/33b6e9f6d46911226b502dcf519020566bda97abeb1a643f96d1776f9e72/python_debian-0.1.48-py3-none-any.whl")
	version("0.1.49", sha256="880f3bc52e31599f2a9b432bd7691844286825087fccdcf2f6ffd5cd79a26f9f", expand=False, url="https://files.pythonhosted.org/packages/9c/37/6e38e7aafa55c1257f63ca9f575e8e3cf2560c896c5202a16c9f33ee7657/python_debian-0.1.49-py3-none-any.whl")
	version("1.0.0", sha256="80cbcf04ed23e36033d37f651ea0f19eb08c1af6d3b75d09ceeae35fca04ae1a", expand=False, url="https://files.pythonhosted.org/packages/6c/eb/5b54844c115dc012166a822284decab274a7fa68c9c01387f95eb23d8dde/python_debian-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="8f137c230c1d9279c2ac892b35915068b2aca090c9fd3da5671ff87af32af12c", expand=False, url="https://files.pythonhosted.org/packages/ba/15/e8096189b18dda72e4923622abc10b021ecff723b397e22eff29fb86637b/python_debian-1.0.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-charset-normalizer", type=("build", "run"))
	depends_on("python@2..7", when="@0.1.32-py2.7", type=("build", "run"))
	depends_on("python@3..6", when="@0.1.32-py3.6", type=("build", "run"))
	depends_on("python@2", when="@0.1.33-py2", type=("build", "run"))
	depends_on("python@2", when="@0.1.34-py2", type=("build", "run"))
	depends_on("python@2", when="@0.1.35-py2", type=("build", "run"))
	depends_on("python@2", when="@0.1.36-py2", type=("build", "run"))

# {'chardet': ['0.1.32-py2.7', '0.1.32-py3.6', '0.1.33-py2', '0.1.33', '0.1.34-py2', '0.1.34', '0.1.35-py2', '0.1.35', '0.1.36-py2', '0.1.36', '0.1.37', '0.1.38', '0.1.39', '0.1.40', '0.1.42', '0.1.43', '0.1.44', '0.1.47', '0.1.48', '0.1.49'], 'six': ['0.1.32-py2.7', '0.1.32-py3.6', '0.1.33-py2', '0.1.33', '0.1.34-py2', '0.1.34', '0.1.35-py2', '0.1.35', '0.1.36-py2', '0.1.36', '0.1.37', '0.1.38', '0.1.39', '0.1.40'], 'charset-normalizer': ['1.0.0', '1.0.1'], "pytest;extra=='test'": ['1.0.0', '1.0.1'], "pytest-cov;extra=='test'": ['1.0.0', '1.0.1']}