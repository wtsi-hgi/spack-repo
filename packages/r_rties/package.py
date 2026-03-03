# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRties(RPackage):
	"""Modeling Interpersonal Dynamics

	The name of this package grew out of our research on temporal interpersonal 
    emotion systems (TIES), hence 'rties'. It provides tools for using a set of models to 
    investigate temporal processes in bivariate (e.g., dyadic) systems. The general approach
    is to model, one dyad at a time, the dynamics of a variable that is assessed repeatedly 
    from both partners, extract the parameter estimates for each dyad, and then use those 
    parameter estimates as input to a latent profile analysis to extract groups of dyads with
    qualitatively distinct dynamics. Finally, the profile memberships can be used to either 
    predict, or be predicted by, another variable of interest. Currently, 2 models are supported:
    1) inertia-coordination, and 2) a coupled-oscillator. Extended documentation is provided 
    in vignettes. Theoretical background can be found in Butler (2011) <doi:10.1177/1088868311411164> 
    and Butler & Barnard (2019) <doi:10.1097/PSY.0000000000000703>.
	"""
	
	cran = "rties" 

	version("5.0.0", md5="8822b25aca485271a81d5764881ff6fb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-datacombine", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-interactions", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
