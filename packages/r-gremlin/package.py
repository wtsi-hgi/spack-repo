# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGremlin(RPackage):
	"""Mixed-Effects REML Incorporating Generalized Inverses

	Fit linear mixed-effects models using restricted (or residual)
    maximum likelihood (REML) and with generalized inverse matrices to specify
    covariance structures for random effects. In particular, the package is
    suited to fit quantitative genetic mixed models, often referred to as
    'animal models'. Implements the average information algorithm as the main
    tool to maximize the restricted log-likelihood, but with other algorithms
    available.
	"""
	
	homepage = "http://github.com/matthewwolak/gremlin"
	cran = "gremlin" 

	version("1.0.1", md5="74ea369e92b3fce1281a811bc7e9993d")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
