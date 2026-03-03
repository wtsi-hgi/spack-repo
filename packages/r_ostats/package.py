# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROstats(RPackage):
	"""O-Stats, or Pairwise Community-Level Niche Overlap Statistics

	O-statistics, or overlap statistics, measure the degree of community-level trait overlap. 
    They are estimated by fitting nonparametric kernel density functions to each species’ trait 
    distribution and calculating their areas of overlap. For instance, the median pairwise overlap 
    for a community is calculated by first determining the overlap of each species pair 
    in trait space, and then taking the median overlap of each species pair in a community. 
    This median overlap value is called the O-statistic (O for overlap).
    The Ostats() function calculates separate univariate overlap statistics for each trait, 
    while the Ostats_multivariate() function calculates a single multivariate overlap statistic for all traits. 
    O-statistics can be evaluated against null models to obtain standardized effect sizes. 
    'Ostats' is part of the collaborative Macrosystems Biodiversity Project "Local- to continental-scale 
    drivers of biodiversity across the National Ecological Observatory Network (NEON)." 
    For more information on this project, see the Macrosystems Biodiversity Website 
    (<https://neon-biodiversity.github.io/>). Calculation of O-statistics is described in
    Read et al. (2018) <doi:10.1111/ecog.03641>, and a teaching module for introducing the
    underlying biological concepts at an undergraduate level is described in Grady et al.
    (2018) <http://tiee.esa.org/vol/v14/issues/figure_sets/grady/abstract.html>.
	"""
	
	homepage = "https://neon-biodiversity.github.io/Ostats/"
	cran = "Ostats" 

	version("0.2.0", md5="fd93e3c2dd27ade7346740065f8b9999")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-hypervolume", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
