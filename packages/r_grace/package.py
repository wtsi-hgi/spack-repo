# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrace(RPackage):
	"""Graph-Constrained Estimation and Hypothesis Tests

	Use the graph-constrained estimation (Grace) procedure (Zhao and Shojaie, 2016 <doi:10.1111/biom.12418>) to estimate graph-guided linear regression coefficients and use the Grace/GraceI/GraceR tests to perform graph-guided hypothesis tests on the association between the response and the predictors.
	"""
	
	homepage = "http://onlinelibrary.wiley.com/doi/10.1111/biom.12418/abstract"
	cran = "Grace" 

	version("0.5.3", md5="f85a7d51ad4c6fe913b73467e56076cb")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-scalreg", type=("build", "run"))
