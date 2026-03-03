# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunkycells(RPackage):
	"""Functional Data Analysis for Multiplexed Cell Images

	Compare variables of interest between (potentially large
    numbers of) spatial interactions and meta-variables. Spatial variables
    are summarized using K, or other, functions, and projected for use in
    a modified random forest model. The model allows comparison of
    functional and non-functional variables to each other and to noise,
    giving statistical significance to the results. Included are
    preparation, modeling, and interpreting tools along with example
    datasets, as described in VanderDoes et al., (2023)
    <doi:10.1101/2023.07.18.549619>.
	"""
	
	homepage = "https://github.com/jrvanderdoes/funkycells"
	cran = "funkycells" 

	version("1.1.1", md5="d4f4d65f330a8fcea9863ba1b826b718")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
