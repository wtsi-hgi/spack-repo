# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcemglm(RPackage):
	"""Maximum Likelihood Estimation for Generalized Linear Mixed
Models

	Maximum likelihood estimation for generalized linear mixed models via Monte Carlo EM.
    For a description of the algorithm see Brian S. Caffo, Wolfgang Jank and Galin L. Jones (2005)
	<DOI:10.1111/j.1467-9868.2005.00499.x>.
	"""
	
	cran = "mcemGLM" 

	version("1.1.3", md5="69f3667ea302af290e5e632f62dc1b8c")

	depends_on("r-trust", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
