# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmbstan(RPackage):
	"""MCMC Sampling from 'TMB' Model Object using 'Stan'

	Enables all 'rstan' functionality for a 'TMB' model object, in particular MCMC sampling and chain visualization. Sampling can be performed with or without Laplace approximation for the random effects. This is demonstrated in Monnahan & Kristensen (2018) <DOI:10.1371/journal.pone.0197954>.
	"""
	
	cran = "tmbstan" 

	version("1.0.91", md5="d7cfbfd800e6b143b09d23a0ca411b0a")

	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-stanheaders", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
