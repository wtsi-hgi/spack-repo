# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiglasso(RPackage):
	"""Hierarchical Integrative Group LASSO

	
    Environmental health studies are increasingly measuring multiple pollutants
    to characterize the joint health effects attributable to exposure mixtures.
    However, the underlying dose-response relationship between toxicants and
    health outcomes of interest may be highly nonlinear, with possible nonlinear
    interaction effects. Hierarchical integrative group least absolute shrinkage
    and selection operator (HiGLASSO), developed by Boss et al (2020)
    <arXiv:2003.12844>, is a general framework to identify noteworthy nonlinear 
    main and interaction effects in the presence of group structures among a set
    of exposures.
	"""
	
	cran = "higlasso" 

	version("0.9.0", md5="ba70f6470d49d1ca70bbcf8f7d961a7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gcdnet", type=("build", "run"))
	depends_on("r-gglasso", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
