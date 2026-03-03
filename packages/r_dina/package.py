# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDina(RPackage):
	"""Bayesian Estimation of DINA Model

	Estimate the Deterministic Input, Noisy "And" Gate (DINA)
    cognitive diagnostic model parameters using the Gibbs sampler described
    by Culpepper (2015) <doi:10.3102/1076998615595403>.
	"""
	
	homepage = "https://github.com/tmsalab/dina"
	cran = "dina" 

	version("2.0.0", md5="74c2b51e02dbcf4e42c144e5fd501b46")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-simcdm", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.200:", type=("build", "run"))
	depends_on("r-rgen", type=("build", "run"))
