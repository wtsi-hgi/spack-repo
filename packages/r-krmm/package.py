# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKrmm(RPackage):
	"""Kernel Ridge Mixed Model

	Solves kernel ridge regression, within the the mixed model framework, for the linear, polynomial, Gaussian, Laplacian and ANOVA kernels. The model components (i.e. fixed and random effects) and variance parameters are estimated using the expectation-maximization (EM) algorithm. All the estimated components and parameters, e.g. BLUP of dual variables and BLUP of random predictor effects for the linear kernel (also known as RR-BLUP), are available. The kernel ridge mixed model (KRMM) is described in Jacquin L, Cao T-V and Ahmadi N (2016) A Unified and Comprehensible View of Parametric and Kernel Methods for Genomic Prediction with Application to Rice. Front. Genet. 7:145. <doi:10.3389/fgene.2016.00145>.
	"""
	
	cran = "KRMM" 

	version("1.0", md5="328717a14550999182da36687788dec6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
