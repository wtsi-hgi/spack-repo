# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZetadiv(RPackage):
	"""Functions to Compute Compositional Turnover Using Zeta Diversity

	Functions to compute compositional turnover using zeta-diversity,
    the number of species shared by multiple assemblages. The package includes
    functions to compute zeta-diversity for a specific number of
    assemblages and to compute zeta-diversity for a range of numbers of
    assemblages. It also includes functions to explain how zeta-diversity
    varies with distance and with differences in environmental variables
    between assemblages, using generalised linear models, linear models
    with negative constraints, generalised additive models,shape
    constrained additive models, and I-splines.
	"""
	
	cran = "zetadiv" 

	version("1.2.1", md5="9b5b8afc34baeaaffbc9815687d77ff7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
