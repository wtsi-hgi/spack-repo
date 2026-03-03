# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmgaussian(RPackage):
	"""Expectation-Maximization Algorithm for Multivariate Normal
(Gaussian) with Missing Data

	Initially designed to distribute code for estimating the Gaussian
  graphical model with Lasso regularization, also known as the graphical lasso
  (glasso), using an Expectation-Maximization (EM) algorithm based on work by
  Städler and Bühlmann (2012) <doi:10.1007/s11222-010-9219-7>. As a byproduct,
  code for estimating means and covariances (or the precision matrix) under a
  multivariate normal (Gaussian) distribution is also available.
	"""
	
	cran = "EMgaussian" 

	version("0.2.1", md5="584e5b7e109783c939156259f78bbd8f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
