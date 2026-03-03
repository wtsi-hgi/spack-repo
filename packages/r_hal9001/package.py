# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHal9001(RPackage):
	"""The Scalable Highly Adaptive Lasso

	A scalable implementation of the highly adaptive lasso algorithm,
  including routines for constructing sparse matrices of basis functions of the
  observed data, as well as a custom implementation of Lasso regression tailored
  to enhance efficiency when the matrix of predictors is composed exclusively of
  indicator functions. For ease of use and increased flexibility, the Lasso
  fitting routines invoke code from the 'glmnet' package by default. The highly
  adaptive lasso was first formulated and described by MJ van der Laan (2017)
  <doi:10.1515/ijb-2015-0097>, with practical demonstrations of its performance
  given by Benkeser and van der Laan (2016) <doi:10.1109/DSAA.2016.93>. This
  implementation of the highly adaptive lasso algorithm was described by Hejazi,
  Coyle, and van der Laan (2020) <doi:10.21105/joss.02526>.
	"""
	
	homepage = "https://github.com/tlverse/hal9001"
	cran = "hal9001" 

	version("0.4.6", md5="82ca3e5d118e8bb592268d364eb1962f", url="https://cran.r-project.org/src/contrib/hal9001_0.4.6.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-origami@1.0.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
