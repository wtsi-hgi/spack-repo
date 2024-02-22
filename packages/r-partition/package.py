# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartition(RPackage):
	"""Agglomerative Partitioning Framework for Dimension Reduction

	A fast and flexible framework for agglomerative partitioning.
    'partition' uses an approach called Direct-Measure-Reduce to create
    new variables that maintain the user-specified minimum level of
    information. Each reduced variable is also interpretable: the original
    variables map to one and only one variable in the reduced data set.
    'partition' is flexible, as well: how variables are selected to
    reduce, how information loss is measured, and the way data is reduced
    can all be customized.  'partition' is based on the Partition
    framework discussed in Millstein et al. (2020) 
    <doi:10.1093/bioinformatics/btz661>.
	"""
	
	homepage = "https://uscbiostats.github.io/partition/"
	cran = "partition" 

	version("0.2.0", md5="86d62464d102f636d7ce69f8e59fdd94")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
