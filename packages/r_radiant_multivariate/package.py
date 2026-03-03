# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiantMultivariate(RPackage):
	"""Multivariate Menu for Radiant: Business Analytics using R and
Shiny

	The Radiant Multivariate menu includes interfaces for perceptual
    mapping, factor analysis, cluster analysis, and conjoint analysis. The
    application extends the functionality in 'radiant.data'.
	"""
	
	homepage = "https://github.com/radiant-rstats/radiant.multivariate/"
	cran = "radiant.multivariate" 

	version("1.6.1", md5="243255c6699b1f744ff889b3e1942312")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-radiant-data@1.5:", type=("build", "run"))
	depends_on("r-radiant-model@1.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-psych@1.8.4:", type=("build", "run"))
	depends_on("r-gparotation@2014.11.1:", type=("build", "run"))
	depends_on("r-car@2.1.1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-polycor@0.7.10:", type=("build", "run"))
	depends_on("r-gower@0.2.1:", type=("build", "run"))
	depends_on("r-clustmixtype@0.2.1:", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
