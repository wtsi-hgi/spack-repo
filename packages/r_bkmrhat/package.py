# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBkmrhat(RPackage):
	"""Parallel Chain Tools for Bayesian Kernel Machine Regression

	Bayesian kernel machine regression (from the 'bkmr' package)
    is a Bayesian semi-parametric generalized linear model approach under
    identity and probit links. There are a number of functions in this
    package that extend Bayesian kernel machine regression fits to allow
    multiple-chain inference and diagnostics, which leverage functions
    from the 'future', 'rstan', and 'coda' packages.  Reference: Bobb, J.
    F., Henn, B. C., Valeri, L., & Coull, B. A. (2018). Statistical
    software for analyzing the health effects of multiple concurrent
    exposures via Bayesian kernel machine regression. ;
    <doi:10.1186/s12940-018-0413-y>.
	"""
	
	cran = "bkmrhat" 

	version("1.1.3", md5="d584e10c4b5b7f2182d54dd30992f077")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bkmr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
