# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAtomworks(PythonPackage):
	"""A research-oriented data toolkit for training biomolecular deep-learning foundation models"""
	
	homepage = "https://rosettacommons.github.io/atomworks/latest/index.html"
	pypi = "atomworks/atomworks-2.2.1-py3-none-any.whl" 

	version("1.0.0", sha256="b912b5dfed75d00f612115eaea8bac8f296f9dbec9f41aa29227aafce4cc32ec", expand=False, url="https://files.pythonhosted.org/packages/5b/24/f96ae6ed35da664132f264ebbcfb550d7fc78b778d45b7bc3963da3dc9e8/atomworks-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="44dacb4b2faa7257cd21358f140e94b2b2b3b73441bace39e2b3a5c9658a92c2", expand=False, url="https://files.pythonhosted.org/packages/20/14/255a19691d13d7d53363468a8c6e6c13a12a72b7b2991c4e5356f2fc86fe/atomworks-1.0.1-py3-none-any.whl")
	version("1.0.2", sha256="0e524dbad8d522e7d79409481e5d3f55813f16c6cfc84940a4d89230ec9ea27d", expand=False, url="https://files.pythonhosted.org/packages/a7/44/444077a79bfc86c0bf8768981081bbf7dfb3fecaf88c1263ce3bf224484d/atomworks-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="bf99259950f0b13be151310214d6d0ce6e6539b449d67a0569a0eef79bf3f9a5", expand=False, url="https://files.pythonhosted.org/packages/dd/31/dbb878dc15acd7bb3205e8ec09a0fdbac9c6a80d74a4a1c7dd2979048bbd/atomworks-1.0.3-py3-none-any.whl")
	version("1.1.0", sha256="afca4d750cee1d2f2ec46be3efef8d7564b2741f0e3f4075e24f19d7c22eba71", expand=False, url="https://files.pythonhosted.org/packages/40/06/27f1775c31e1f49faee097c258a68403290a30c0d52122da3c448b3023e6/atomworks-1.1.0-py3-none-any.whl")
	version("2.0.0", sha256="016c64fffb67b26a8874922ca5112f5ee63a2bb4af1a176a115ef4570fa5046b", expand=False, url="https://files.pythonhosted.org/packages/02/86/ab3a0743b5c3ee5167e2cc4cead7e4cf967162f72f77dd0ef0c7e2fd148b/atomworks-2.0.0-py3-none-any.whl")
	version("2.0.1", sha256="fc8cd55b4c2b913de410968396efda53c2923dc3f6eb7955ff2fb92aa638a019", expand=False, url="https://files.pythonhosted.org/packages/d2/25/d57a1b4de2d89a0cfab0e099b657f4c89dc56fc21514c35d4b0f7cefbad1/atomworks-2.0.1-py3-none-any.whl")
	version("2.1.0", sha256="c23dadcafc0811f31af2822a901b30942b17bcf98644c2712f0fd1300df34041", expand=False, url="https://files.pythonhosted.org/packages/83/5a/92b20637052943b00bd3774419099c44266728fa8bd8443aa974a6f6c2cf/atomworks-2.1.0-py3-none-any.whl")
	version("2.1.1", sha256="7c9cece48829ff28ce294f0cc66fdfe36396888a629e85bb01bb7480ede4c4fd", expand=False, url="https://files.pythonhosted.org/packages/48/f3/764d4ad4bbf0a50087c680ce833ced37e888bfdcd02fc9aab2094c52b48a/atomworks-2.1.1-py3-none-any.whl")
	version("2.1.2", sha256="5863022c775b4638584e9f9bfa9734e514d5d5a222c10cc0f13afe0a500e899d", expand=False, url="https://files.pythonhosted.org/packages/9f/04/489533deec3a5ca68f5e35ffc0c96645dfeaf30e89d58ec5e00693351a1a/atomworks-2.1.2-py3-none-any.whl")
	version("2.2.0", sha256="f20ae4d80b51c36f98f29894a219b584dbb65ac806d440959e0345b3e87df1f0", expand=False, url="https://files.pythonhosted.org/packages/4a/a5/5d36fee0b1b0cd3c9d61490080d1e1f6816e35258b48be1aa8d1a63b5c5b/atomworks-2.2.0-py3-none-any.whl")
	version("2.2.1", sha256="57adfa82d4f10e0dd648eb8c8d7ae5cba0278321812009b5cf62cbaf566da3cd", expand=False, url="https://files.pythonhosted.org/packages/01/62/c54f176aca587a9218300749a87e789903711f759a3c8db149200d74ab96/atomworks-2.2.1-py3-none-any.whl")

	depends_on("python@3.11:", type=("build", "run"))
	depends_on("py-biotite", type=("build", "run"))
	depends_on("py-cython", type=("build", "run"))
	depends_on("py-cytoolz", type=("build", "run"))
	depends_on("py-hydride", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-py3dmol", type=("build", "run"))
	depends_on("py-pyarrow", type=("build", "run"))
	depends_on("py-pymol-remote", type=("build", "run"))
	depends_on("py-rdkit", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-typer", type=("build", "run"))
	depends_on("py-zstandard", type=("build", "run"))

