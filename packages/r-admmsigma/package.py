# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmmsigma(RPackage):
	"""Penalized Precision Matrix Estimation via ADMM

	Estimates a penalized precision matrix via the alternating direction method of multipliers (ADMM) algorithm. It currently supports a general elastic-net penalty that allows for both ridge and lasso-type penalties as special cases. This package is an alternative to the 'glasso' package.
	See Boyd et al (2010) <doi:10.1561/2200000016> for details regarding the estimation method.
	"""
	
	homepage = "https://github.com/MGallow/ADMMsigma"
	cran = "ADMMsigma"

	version("2.1", md5="53ea3de8add49b92daeb6e6a9001fcdc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
