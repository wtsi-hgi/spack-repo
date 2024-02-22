# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBisque(RPackage):
	"""Approximate Bayesian Inference via Sparse Grid Quadrature
Evaluation (BISQuE) for Hierarchical Models

	Implementation of the 'bisque' strategy for approximate Bayesian posterior inference.  See Hewitt and Hoeting (2019) <arXiv:1904.07270> for complete details.  'bisque' combines conditioning with sparse grid quadrature rules to approximate marginal posterior quantities of hierarchical Bayesian models.  The resulting approximations are computationally efficient for many hierarchical Bayesian models.  The 'bisque' package allows approximate posterior inference for custom models; users only need to specify the conditional densities required for the approximation.
	"""
	
	cran = "bisque" 

	version("1.0.2", md5="0ceac23fd1ebcb5e052a59b6f4d1a49a")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mvquad", type=("build", "run"))
	depends_on("r-rcpp@0.12.4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3.1:", type=("build", "run"))
