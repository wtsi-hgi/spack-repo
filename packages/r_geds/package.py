# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeds(RPackage):
	"""Geometrically Designed Spline Regression

	Spline Regression, Generalized Additive Models, and Component-wise Gradient
  Boosting, utilizing Geometrically Designed (GeD) Splines. GeDS regression is a
  non-parametric method inspired by geometric principles, for fitting spline regression
  models with variable knots in one or two independent variables. It efficiently estimates
  the number of knots and their positions, as well as the spline order, assuming the
  response variable follows a distribution from the exponential family. GeDS models
  integrate the broader category of Generalized (Non-)Linear Models, offering a flexible
  approach to modeling complex relationships. A description of the method can be found in
  Kaishev et al. (2016) <doi:10.1007/s00180-015-0621-7> and Dimitrova et al. (2023)
  <doi:10.1016/j.amc.2022.127493>. Further extending its capabilities, GeDS's implementation
  includes Generalized Additive Models (GAM) and Functional Gradient Boosting (FGB),
  enabling versatile multivariate predictor modeling, as discussed in the forthcoming work of
  Dimitrova et al. (2024).
	"""
	
	homepage = "https://github.com/emilioluissaenzguillen/GeDS"
	cran = "GeDS" 

	version("0.2.0", md5="523bf10b03281f0d2ba3d04a07169d9c")
	version("0.1.4", md5="80b509c311dd3354c8a067fa92a830c6")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-th-data", type=("build", "run"))
