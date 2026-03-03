# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMplScatterDensity(PythonPackage):
	"""Matplotlib helpers to make density scatter plots"""
	
	homepage = "https://github.com/astrofrog/mpl-scatter-density"
	pypi = "mpl-scatter-density/mpl-scatter-density-0.7.tar.gz" 

	version("0.1", sha256="25f1e012afe504ca1b451b166bdbde5e966c4fd7447c4c68a062ad2107a82fa9", expand=False, url="https://files.pythonhosted.org/packages/06/7b/2ef38ed6eba80762800e5865922fb5923416d5d406a1c21d39d96988c598/mpl_scatter_density-0.1-py2.py3-none-any.whl")
	version("0.2", sha256="24ae7c027d07b879244d75b9d2866c8f18208ff65ddf02abdd7ee9a93d67184d", expand=False, url="https://files.pythonhosted.org/packages/ed/fe/a51deebeef29db13aa34f2d9d4b0370a1985d2dc35e713a7e6c36d4d5b81/mpl_scatter_density-0.2-py2.py3-none-any.whl")
	version("0.3", sha256="43b9e1dceea65d61088140e8ad839976cfad521695350a30ac19a09d3c5af705", expand=False, url="https://files.pythonhosted.org/packages/c0/c0/286c45fab93bb0e29a5c21259fa67f54ac402347f343f62816ae5e8659bb/mpl_scatter_density-0.3-py2.py3-none-any.whl")
	version("0.4", sha256="c1c7103c683676a14ca74d1a0b8b924fb20a7359e0ce433dd4c1a3f8636bcce3", expand=False, url="https://files.pythonhosted.org/packages/86/fd/b552bb556fc0e02197e85746ac389fc3b845216dacb8a213ed6f06fc9021/mpl_scatter_density-0.4-py2.py3-none-any.whl")
	version("0.5", sha256="6265c864a0d395d3f9379a4715163da2a45a438992a4fe3cebbf48274575109a", expand=False, url="https://files.pythonhosted.org/packages/18/5d/c5450a66cb7789b0b9c569b152d24ae2b533e7386566859e7f44daebf024/mpl_scatter_density-0.5-py2.py3-none-any.whl")
	version("0.6", sha256="8c4685e66d861da2e5a9a998f27f643d4cb5f916bbaee6550398a6b8484355e9", expand=False, url="https://files.pythonhosted.org/packages/aa/01/1059e40bc71f6db8381dc5cb4135feb48d5fceff7d3b0152aa045e7c6f40/mpl_scatter_density-0.6-py2.py3-none-any.whl")
	version("0.7", sha256="721b4efeafcbc0ba4a5c1ecd8f401dc2d1aa6a372445c5b49e1da34e70a95ead", expand=False, url="https://files.pythonhosted.org/packages/0a/39/6f602600a06bebbdd3c0e8c1e272d103302cff3d17e8f4fbbb3ed01e309a/mpl_scatter_density-0.7-py3-none-any.whl")

	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-fast-histogram", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
