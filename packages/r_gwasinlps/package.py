# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasinlps(RPackage):
	"""Non-Local Prior Based Iterative Variable Selection Tool for
Genome-Wide Association Studies

	Performs variable selection with data from Genome-wide association studies (GWAS), or other high-dimensional data with continuous, binary or survival outcomes, combining in an iterative framework the computational efficiency of the structured screen-and-select variable selection strategy based on some association learning and the parsimonious uncertainty quantification provided by the use of non-local priors (see Sanyal et al., 2019 <DOI:10.1093/bioinformatics/bty472>). 
	"""
	
	homepage = "https://nilotpalsanyal.github.io/GWASinlps/"
	cran = "GWASinlps" 

	version("2.2", md5="5efc1e27066e9c97dbab8346668fe57d")

	depends_on("r-mombf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-fastglm", type=("build", "run"))
	depends_on("r-horseshoe", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
