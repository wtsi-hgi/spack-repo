# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsifs(RPackage):
	"""Stochastic Search Inconsistency Factor Selection

	Evaluating the consistency assumption of Network Meta-Analysis both globally and locally in the Bayesian framework. Inconsistencies are located by applying Bayesian variable selection to the inconsistency factors. The implementation of the method is described by Seitidis et al. (2022) <arXiv:2211.07258>.
	"""
	
	homepage = "https://github.com/georgiosseitidis/ssifs"
	cran = "ssifs" 

	version("1.0.2", md5="9ae764bf040af7cd6d0e93e42e7da2ad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-gtools@3.9.2.1:", type=("build", "run"))
	depends_on("r-igraph@1.3.1:", type=("build", "run"))
	depends_on("r-netmeta@2.6:", type=("build", "run"))
	depends_on("r-plyr@1.8.7:", type=("build", "run"))
	depends_on("r-r2jags@0.7.1:", type=("build", "run"))
	depends_on("r-revecor@0.99.3:", type=("build", "run"))
	depends_on("r-rdpack@2.3:", type=("build", "run"))
