# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastsf(RPackage):
	"""Fast Structural Filtering

	An implementation of the fast structural filtering with L0 penalty. It includes an adaptive polynomial estimator by minimizing the least squares error with constraints on the number of breaks in their (k + 1)-st discrete derivative, for a chosen integer k >= 0. It also includes generalized structure sparsity constraint, i.e., graph trend filtering. This package is implemented via the primal dual active set algorithm, which formulates estimates and residuals as primal and dual variables, and utilizes efficient active set selection strategies based on the properties of the primal and dual variables.
	"""
	
	cran = "FastSF" 

	version("0.1.1", md5="354150f344aa141b5e02e1c5c5046af4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
