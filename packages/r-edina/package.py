# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdina(RPackage):
	"""Bayesian Estimation of an Exploratory Deterministic Input, Noisy
and Gate Model

	Perform a Bayesian estimation of the exploratory 
    deterministic input, noisy and gate (EDINA)
    cognitive diagnostic model described by Chen et al. (2018)
    <doi:10.1007/s11336-017-9579-4>.
	"""
	
	homepage = "https://github.com/tmsalab/edina"
	cran = "edina" 

	version("0.1.1", md5="921666b93981fe7560c3c5f2544eae6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jjb", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rgen", type=("build", "run"))
