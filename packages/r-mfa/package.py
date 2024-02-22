# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfa(RPackage):
	"""Bayesian hierarchical mixture of factor analyzers for modelling genomic bifurcations

	MFA models genomic bifurcations using a Bayesian hierarchical mixture of factor analysers.
	"""
	
	bioc = "mfa" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mfa_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mfa/mfa_1.24.0.tar.gz"]

	version("1.24.0", md5="37fa2e82d83636458e9a20cc72069dcd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggmcmc", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
