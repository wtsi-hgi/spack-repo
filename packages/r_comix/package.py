# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComix(RPackage):
	"""Coarsened Mixtures of Hierarchical Skew Kernels

	Bayesian fit of a Dirichlet Process Mixture with hierarchical multivariate skew normal kernels and coarsened posteriors. For more information, see Gorsky, Chan and Ma (2020) <arXiv:2001.06451>.
	"""
	
	cran = "COMIX" 

	version("1.0.0", md5="165003e1880af52fcf29c6a707bb2179")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
