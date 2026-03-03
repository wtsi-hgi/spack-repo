# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwlmm(RPackage):
	"""PWIGLS for Two-Level Multivariate and Multilevel Linear Models

	Estimates two-level multilevel linear model and two-level multivariate linear multilevel model with weights following Probability Weighted Iterative Generalised Least Squares approach. For details see Veiga et al.(2014) <doi:10.1111/rssc.12020>.
	"""
	
	cran = "pwlmm" 

	version("1.1.1", md5="262bf39b7dc34a6fafac5694582147dd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
