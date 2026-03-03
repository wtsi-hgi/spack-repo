# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenridge(RPackage):
	"""Generalized Ridge Trace Plots for Ridge Regression

	The genridge package introduces generalizations of the standard univariate
  ridge trace plot used in ridge regression and related methods.  These graphical methods
  show both bias (actually, shrinkage) and precision, by plotting the covariance ellipsoids of the estimated
  coefficients, rather than just the estimates themselves.  2D and 3D plotting methods are provided,
  both in the space of the predictor variables and in the transformed space of the PCA/SVD of the
  predictors.  
	"""
	
	homepage = "https://friendly.github.io/genridge/"
	cran = "genridge" 

	version("0.7.0", md5="8929980c5d008c3444d326e607c10e7f")

	depends_on("r@2.11.1:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
