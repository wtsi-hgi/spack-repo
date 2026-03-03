# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixsemirob(RPackage):
	"""Mixture Models: Parametric, Semiparametric, and Robust

	Various functions are provided to estimate parametric mixture models
    (with Gaussian, t, Laplace, log-concave distributions, etc.) and
    non-parametric mixture models. The package performs hypothesis tests
    and addresses label switching issues in mixture models.
    The package also allows for parameter estimation in mixture of regressions,
    proportion-varying mixture of regressions, and robust mixture of regressions. 
	"""
	
	cran = "MixSemiRob" 

	version("1.1.0", md5="ba01769e4604ac1aefcb02be232f9bbe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gofkernel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rlab", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
