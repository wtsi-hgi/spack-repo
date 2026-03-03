# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyM2r2(PythonPackage):
	"""Markdown and reStructuredText in a single file."""
	
	homepage = "https://github.com/crossnox/m2r2"
	pypi = "m2r2/m2r2-0.3.3.post2-py3-none-any.whl" 

	version("0.2.3", sha256="0b75cea4f184714e7705bd5fbbad70988141c4ca6028bafd0e396547b07626cc", expand=False, url="https://files.pythonhosted.org/packages/08/60/e4f3183ced18d8bbd63532aa5f1f5c384b4aef8d4553f89b233124f58535/m2r2-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="dcf98e196f5213b60a241431625e9301777a584d1bfb5139c7080b2a15356019", expand=False, url="https://files.pythonhosted.org/packages/a4/70/fa39097ee60dbef0318d5475cb0766bfecfd5fac4ff3aa791d50d588f695/m2r2-0.2.4-py3-none-any.whl")
	version("0.2.5", sha256="2fe7e03c41e1d2052b9cf3e76359bbfe64960b8fee9d69dfc1fc6e35ccff01e7", expand=False, url="https://files.pythonhosted.org/packages/b4/b1/b26f53614f1f6efd9ec4729990c49b483983284346e517216b13643b7bcf/m2r2-0.2.5-py3-none-any.whl")
	version("0.2.6", sha256="fcaa04878f889e53f0629792d517348d64d4e5af81a9b9317d8b42eec09b28ec", expand=False, url="https://files.pythonhosted.org/packages/a6/7d/f10c6c640f62f6512dd001a25c99d0b394d0044b1b4ee7f277f4981a866b/m2r2-0.2.6-py3-none-any.whl")
	version("0.2.7", sha256="a1b87b00f4d5163a3616253fca4c045f8351818cd803ba2e24af8897442a0eae", expand=False, url="https://files.pythonhosted.org/packages/b2/22/5268f645e0a9d287c384526aebdc7626bce15b98d3942a2535341c4d3f74/m2r2-0.2.7-py3-none-any.whl")
	version("0.2.8", sha256="613934a5d02999574c0256407e6a0e71f8c436f2d2757d6e43d52d2faf8dff1c", expand=False, url="https://files.pythonhosted.org/packages/a5/81/a2297400492757eaba0c6fe2cf77b582c7b15eb4fcfd769ba64c6d19a3df/m2r2-0.2.8-py3-none-any.whl")
	version("0.3.0", sha256="f7ace700bb4a7f8b710a57da84ff6b96a5a9629c8cef442c2e85500bc21cbf16", expand=False, url="https://files.pythonhosted.org/packages/6e/c0/d1ad1302260d8407934cb2aad65d411903df08f499333dee1865e4678804/m2r2-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="c2b62b8dec16f82d9e4d8aecf58830a87835ca90441716fc571e573e32c7d829", expand=False, url="https://files.pythonhosted.org/packages/36/0b/6bb31ff9101100e78bddb36ebbb5ed13790add34d400fe5a705f6dd4de49/m2r2-0.3.1-py3-none-any.whl")
	version("0.3.2", sha256="d3684086b61b4bebe2307f15189495360f05a123c9bda2a66462649b7ca236aa", expand=False, url="https://files.pythonhosted.org/packages/85/e8/37dc688537d59cea15e7b4ca10cdbdd0fa7b81da055e8f6ce91eed6c493f/m2r2-0.3.2-py3-none-any.whl")
	version("0.3.3.post2", sha256="86157721eb6eabcd54d4eea7195890cc58fa6188b8d0abea633383cfbb5e11e3", expand=False, url="https://files.pythonhosted.org/packages/57/57/164112275965de407680ac176f96434d02329539438324c0ab8084df0343/m2r2-0.3.3.post2-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-docutils", type=("build", "run"))
	depends_on("py-mistune", type=("build", "run"))

# {'mistune': ['0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.3.0', '0.3.1'], 'docutils': ['0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.2.7', '0.2.8', '0.3.0', '0.3.1', '0.3.2'], 'mistune(==0.8.4)': ['0.3.2', '0.3.3.post2'], 'docutils(>=0.19)': ['0.3.3.post2']}