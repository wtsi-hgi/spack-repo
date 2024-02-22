# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModqr(RPackage):
	"""Multiple-Output Directional Quantile Regression

	Contains basic tools for performing 
  multiple-output quantile regression and computing
  regression quantile contours by means of directional
  regression quantiles. In the location case, one can thus
  obtain halfspace depth contours in two to six dimensions.
  Hallin, M., Paindaveine, D. and Šiman, M. (2010)
  Multivariate quantiles and multiple-output regression quantiles:
  from L1 optimization to halfspace depth. Annals of Statistics 38, 635-669
  For more references about the method, see Help pages.
	"""
	
	cran = "modQR" 

	version("0.1.3", md5="e992e5b7f1abee1802a3e2e6dd218978")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-lpsolve@5.6.1:", type=("build", "run"))
	depends_on("r-geometry@0.3.1:", type=("build", "run"))
