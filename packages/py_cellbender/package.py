
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCellbender(PythonPackage):
	"""A software package for eliminating technical artifacts from high-throughput single-cell RNA sequencing (scRNA-seq) data"""
	
	homepage = "http://github.com/broadinstitute/CellBender"
	pypi = "cellbender/cellbender-0.3.0-py3-none-any.whl" 

	version("0.1.0", sha256="eb9245b30651234968747f417bfe53dea633ddee9d79ba51bbbbe105e052697c", expand=False, url="https://files.pythonhosted.org/packages/5f/3d/aab013edac06e52220757d2c0135a6704bf49b437f4ba233ce556e8c9ef3/cellbender-0.1.0-1-py3-none-any.whl")
	version("0.2.0", sha256="7875d897b21ade146868eab2a5e1dc1ef0c87d59c517c891a67b56b07932450c", expand=False, url="https://files.pythonhosted.org/packages/26/3a/06f6f978d9e124ead57fe6b7ca1abc4370160301bb1cd240f5db3e5adf83/cellbender-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="fea893e3eba1a82966c8b0ea35bc4a75e977f51026254a1d4563cbdbaf502fa5", expand=False, url="https://files.pythonhosted.org/packages/1c/60/124a8f0ac21854ec099f11043f5af5a87d26b2ca1889f5228899b6226c88/cellbender-0.2.1-py3-none-any.whl")
	version("0.3.0", sha256="dfcf0e0650993ab6ad9f49d67d849af10a4f8073ad333233844666c8c1f2912c", expand=False, url="https://files.pythonhosted.org/packages/33/72/52f6968926b7eafb84f4a312701199adeeb194da3233aff7215cd28481f8/cellbender-0.3.0-py3-none-any.whl")

	depends_on("py-psutil", type=("build", "run"))
	depends_on("py-nbconvert", type=("build", "run"))
	depends_on("py-notebook", type=("build", "run"))
	depends_on("py-jupyter-contrib-nbextensions", type=("build", "run"))
	depends_on("py-jupyter", type=("build", "run"))
	depends_on("py-ipython", type=("build", "run"))
	depends_on("py-loompy", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))
	depends_on("py-pyro-ppl", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-tables", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
