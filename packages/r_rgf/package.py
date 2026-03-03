# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgf(RPackage):
	"""Regularized Greedy Forest

	Regularized Greedy Forest wrapper of the 'Regularized Greedy Forest' <https://github.com/RGF-team/rgf/tree/master/python-package> 'python' package, which also includes a Multi-core implementation (FastRGF) <https://github.com/RGF-team/rgf/tree/master/FastRGF>.
	"""
	
	homepage = "https://github.com/RGF-team/rgf/tree/master/R-package"
	cran = "RGF" 

	version("1.1.1", md5="68bbc532b395966db6aa61a72ba74e72")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("python@3.7:", type=("build", "link", "run"))
	depends_on("py-scikit-learn@0.18.0:", type=("build", "link", "run"))
	depends_on("py-scipy", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
