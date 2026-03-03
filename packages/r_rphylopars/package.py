# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRphylopars(RPackage):
	"""Phylogenetic Comparative Tools for Missing Data and
Within-Species Variation

	Tools for performing phylogenetic comparative methods for datasets with with multiple observations per species (intraspecific variation or measurement error) and/or missing data (Goolsby et al. 2017). Performs ancestral state reconstruction and missing data imputation on the estimated evolutionary model, which can be specified as Brownian Motion, Ornstein-Uhlenbeck, Early-Burst, Pagel's lambda, kappa, or delta, or a star phylogeny.
	"""
	
	homepage = "https://github.com/ericgoolsby/Rphylopars/wiki"
	cran = "Rphylopars" 

	version("0.3.10", md5="b257f5d29ff003f8303d5711fb29030f")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-phylolm", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
