# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdtlcm(RPackage):
	"""Latent Class Analysis with Dirichlet Diffusion Tree Process
Prior

	Implements a Bayesian algorithm to fit latent class models,
    particularly useful for weakly separated latent classes. 
    Reference: Li et al. (2023) <arXiv:2306.04700>.
	"""
	
	homepage = "https://github.com/limengbinggz/ddtlcm"
	cran = "ddtlcm" 

	version("0.1.1", md5="cf797f991cd5df949e5f20f275a780b5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape@5.6.2:", type=("build", "run"))
	depends_on("r-data-table@1.14.4:", type=("build", "run"))
	depends_on("r-extradistr@1.9.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggpubr@0.6:", type=("build", "run"))
	depends_on("r-ggtext@0.1.2:", type=("build", "run"))
	depends_on("r-ggtree@3.4:", type=("build", "run"))
	depends_on("r-label-switching@1.8:", type=("build", "run"))
	depends_on("r-matrixstats@0.62:", type=("build", "run"))
	depends_on("r-phylobase@0.8.10:", type=("build", "run"))
	depends_on("r-polca@1.6.0.1:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
	depends_on("r-bayeslogit@2.1:", type=("build", "run"))
	depends_on("r-matrix@1.5.1:", type=("build", "run"))
	depends_on("r-rdpack@2.5:", type=("build", "run"))
	depends_on("r-r-utils@2.12.2:", type=("build", "run"))
