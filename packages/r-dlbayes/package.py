# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlbayes(RPackage):
	"""Use Dirichlet Laplace Prior to Solve Linear Regression Problem
and Do Variable Selection

	The Dirichlet Laplace shrinkage prior in Bayesian linear regression and variable selection, featuring:
    utility functions in implementing Dirichlet-Laplace priors such as visualization; 
    scalability in Bayesian linear regression; 
    penalized credible regions for variable selection.
	"""
	
	cran = "dlbayes" 

	version("0.1.0", md5="6260d5985eddc284d9679776951cd762")

	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
