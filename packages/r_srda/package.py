# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrda(RPackage):
	"""Sparse Redundancy Analysis

	Sparse redundancy analysis
	for high dimensional (biomedical) data. Directional multivariate analysis 
	to express the maximum variance in the predicted data set by a linear 
	combination of variables of the predictive data set. Implemented in a 
	partial least squares framework, for more details see Csala et al. (2017) <doi:10.1093/bioinformatics/btx374>.
	"""
	
	cran = "sRDA" 

	version("1.0.0", md5="9f60c753157869a2bda0f92c73f58913")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
