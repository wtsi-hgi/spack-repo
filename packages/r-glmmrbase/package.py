# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmrbase(RPackage):
	"""Generalised Linear Mixed Models in R

	Specification, analysis, simulation, and fitting of generalised linear mixed models. 
  Includes Markov Chain Monte Carlo Maximum likelihood and Laplace approximation model fitting for a range of models, 
  non-linear fixed effect specifications, a wide range of flexible covariance functions that can be combined arbitrarily,
  robust and bias-corrected standard error estimation, power calculation, data simulation, and more. 
  See <https://samuel-watson.github.io/glmmr-web/> for a detailed manual.
	"""
	
	homepage = "https://github.com/samuel-watson/glmmrBase"
	cran = "glmmrBase" 

	version("0.7.1", md5="a72bc5b38e9d43c611d6073c9d1e62f5")
	version("0.6.2", md5="04ba15a4b7752b966ca9c27f1cd084eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.3.1:", type=("build", "run"))
	depends_on("r-rcpp@1.0.11:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rstan@2.32.1:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1.1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-sparsechol@0.3.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.32:", type=("build", "run"))
