# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastpcs(RPackage):
	"""FastPCS Robust Fit of Multivariate Location and Scatter

	The FastPCS algorithm of Vakili and Schmitt (2014) <doi:10.1016/j.csda.2013.07.021> for robust estimation of multivariate location and scatter and multivariate outliers detection. 
	"""
	
	cran = "FastPCS" 

	version("0.1.4", md5="a8f31dd9fa51ff60d2c68618b1d70620")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
