# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakaway(RPackage):
	"""Species Richness Estimation and Modeling

	Understanding the drivers of microbial diversity is an important frontier of microbial ecology, and investigating the diversity of samples from microbial ecosystems is a common step in any microbiome analysis. 'breakaway' is the premier package for statistical analysis of microbial diversity. 'breakaway' implements the latest and greatest estimates of species richness, described in Willis and Bunge (2015) <doi:10.1111/biom.12332>, Willis et al. (2017) <doi:10.1111/rssc.12206>, and Willis (2016) <arXiv:1604.02598>, as well as the most commonly used estimates, including the objective Bayes approach described in Barger and Bunge (2010) <doi:10.1214/10-BA527>.
	"""
	
	homepage = "https://adw96.github.io/breakaway/"
	cran = "breakaway" 

	version("4.8.4", md5="94225c9f1d159e31704079beda962469")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
