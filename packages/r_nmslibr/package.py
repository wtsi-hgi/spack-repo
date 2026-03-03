# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmslibr(RPackage):
	"""Non Metric Space (Approximate) Library

	A Non-Metric Space Library ('NMSLIB' <https://github.com/nmslib/nmslib>) wrapper, which according to the authors "is an efficient cross-platform similarity search library and a toolkit for evaluation of similarity search methods. The goal of the 'NMSLIB' <https://github.com/nmslib/nmslib> Library is to create an effective and comprehensive toolkit for searching in generic non-metric spaces. Being comprehensive is important, because no single method is likely to be sufficient in all cases. Also note that exact solutions are hardly efficient in high dimensions and/or non-metric spaces. Hence, the main focus is on approximate methods". The wrapper also includes Approximate Kernel k-Nearest-Neighbor functions based on the 'NMSLIB' <https://github.com/nmslib/nmslib> 'Python' Library.
	"""
	
	homepage = "https://github.com/mlampros/nmslibR"
	cran = "nmslibR" 

	version("1.0.7", md5="a436dce9c53062310ea979fdfca8cd0b")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-kernelknn", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("py-scipy", type=("build", "link", "run"))
