# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultifear(RPackage):
	"""Multiverse Analyses for Conditioning Data

	A suite of functions for performing analyses, based on a multiverse approach, for conditioning data. Specifically, given the appropriate data, the functions are able to perform t-tests, analyses of variance, and mixed models for the provided data and return summary statistics and plots. The function is also able to return for all those tests p-values, confidence intervals, and Bayes factors. The methods are described in Lonsdorf, Gerlicher, Klingelhofer-Jens, & Krypotos (2022) <doi:10.1016/j.brat.2022.104072>.
	"""
	
	homepage = "https://github.com/AngelosPsy/multifear"
	cran = "multifear" 

	version("0.1.3", md5="da61e61ce90702320037e18506c5778c")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-ez@4.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-effsize@0.7.8:", type=("build", "run"))
	depends_on("r-nlme@3.1.144:", type=("build", "run"))
	depends_on("r-bayesfactor@0.9.12.4.2:", type=("build", "run"))
	depends_on("r-bayestestr@0.10:", type=("build", "run"))
	depends_on("r-broom@0.5.5:", type=("build", "run"))
	depends_on("r-effectsize@0.4.1:", type=("build", "run"))
	depends_on("r-esc@0.5.1:", type=("build", "run"))
	depends_on("r-forestplot@1.10:", type=("build", "run"))
	depends_on("r-bootstrap@2019.6:", type=("build", "run"))
