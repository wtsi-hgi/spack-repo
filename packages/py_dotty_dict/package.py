# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDottyDict(PythonPackage):
	"""Dictionary wrapper for quick access to deeply nested keys."""
	
	homepage = "http://dotty-dict.readthedocs.io"
	pypi = "dotty-dict/dotty_dict-1.3.1-py3-none-any.whl" 

	version("0.1.1", sha256="ad0f60072417e32a45736083e098d1162ebeea762c6adc5f0963640a87e85130", expand=False, url="https://files.pythonhosted.org/packages/b9/ec/49cedba03c1fd9ae5e3c8bdfac73d98e0208df29cd466fc7b0738f003ae9/dotty_dict-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="66b06a94d01ad080f4698eb49e4ab2f26f33d025d9dfc3f8e3f58746b2acfa71", expand=False, url="https://files.pythonhosted.org/packages/d3/d3/4828feea639306024e33f7c0f338eef5d51a451a66705f5b3cb27308dcd9/dotty_dict-0.1.2-py2.py3-none-any.whl")
	version("0.1.7", sha256="77520ddce5eeb2c0d9c41cde6f9fda690f3372d784e152ce49ec4c27a4cdcc2a", expand=False, url="https://files.pythonhosted.org/packages/2d/14/dd6f753f53fba9da89fc2512e521972036361c411a69b3a10fb9ac347d02/dotty_dict-0.1.7-py2.py3-none-any.whl")
	version("0.1.8", sha256="d8b78c06def1e4f810b40a5f789e48ca16f4eac7666e6d7596dcfe3f82e7576c", expand=False, url="https://files.pythonhosted.org/packages/23/3a/161acefb1650fb386ed06fb9328779b2adf7f1f774306c3a911c03d881d7/dotty_dict-0.1.8-py2.py3-none-any.whl")
	version("0.1.9", sha256="877bd27728761d8913dddb6cba20122b9025f284bc0d7b45070827ae85924adb", expand=False, url="https://files.pythonhosted.org/packages/27/01/c5e14a775ca0c9a6f7818c313aa02b4c5a146e6c6f85842ce627dc920f7a/dotty_dict-0.1.9-py2.py3-none-any.whl")
	version("1.0.0", sha256="1d3f33fb718d453ec51c59154b46ad294393a000b221e6b16282ec9c7cd44de7")
	version("1.0.1", sha256="aad735bc1c52c733b008357d01bd87ca0d1eead93c5fbd6c4e2a8018076c56f0")
	version("1.0.2", sha256="eeff2b42e9af79144e302b9c068f2700099162f4e3a65671be5ea828ae449869")
	version("1.1.0", sha256="bfe2ca59e8d1831b35cb4b591aaae9d4679b347f281676187cf6b31cf4523fc4")
	version("1.1.1", sha256="2d290a86bad0e7eb1cc5e748bcbb6ddf30597e2fb64613c5eca745a9b263ab91")
	version("1.1.2", sha256="2e11232771d41e37896119c4f4b2c24b177117d53ac25f65e6019038177c415b")
	version("1.2.0", sha256="92d561e7cb27d8abcfa3fa252a5ef954e562146edb5e1caba9beafe8b97c25c3")
	version("1.2.1", sha256="0b6f1ebc26a442f4cb1f963dbda7f5a56a5993a7c1311b1feca77e0bfcc1a13b")
	version("1.3.0", sha256="eb0035a3629ecd84397a68f1f42f1e94abd1c34577a19cd3eacad331ee7cbaf0")
	version("1.3.1", sha256="5022d234d9922f13aa711b4950372a06a6d64cb6d6db9ba43d0ba133ebfce31f", expand=False, url="https://files.pythonhosted.org/packages/1a/91/e0d457ee03ec33d79ee2cd8d212debb1bc21dfb99728ae35efdb5832dc22/dotty_dict-1.3.1-py3-none-any.whl")

	depends_on("python@3.5:4.0", type=("build", "run"))
