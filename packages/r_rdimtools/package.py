# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdimtools(RPackage):
	"""Dimension Reduction and Estimation Methods

	We provide linear and nonlinear dimension reduction techniques.
	Intrinsic dimension estimation methods for exploratory analysis are also provided.
	For more details on the package, see the paper by You and Shung (2022) <doi:10.1016/j.simpa.2022.100414>.
	"""
	
	homepage = "https://www.kisungyou.com/Rdimtools/"
	cran = "Rdimtools" 

	version("1.1.2", md5="dcb67b66070ef170c40778b285af6502")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-admm", type=("build", "run"))
	depends_on("r-cvxr@1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppde", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-maotai", type=("build", "run"))
	depends_on("r-mclustcomp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
