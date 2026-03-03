# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtpcr(RPackage):
	"""qPCR Data Analysis

	Various methods are employed for statistical analysis and graphical presentation of real-time PCR (quantitative PCR  or qPCR) data. 'rtpcr' handles amplification efficiency calculation and statistical analysis of real-time PCR data based on one reference gene. By accounting for amplification efficiency values, 'rtpcr' was developed using a general calculation method described by Ganger et al. (2017) <doi:10.1186/s12859-017-1949-5>, covering both the Livak and Pfaffl methods. Based on the experimental conditions, the functions of the 'rtpcr' package use t-test (for experiments with a two-level factor) or analysis of variance (for cases where more than two levels or factors exist) to calculate the fold change or relative expression. The functions also provide standard deviations and confidence limits for means, apply statistical mean comparisons, and present letter mean grouping. To facilitate using 'rtpcr', different datasets have been employed in the examples and the outputs are explained. An outstanding feature of 'rtpcr' package is providing publication-ready bar plots with various controlling arguments for experiments with up to three different factors. The 'rtpcr' package is user-friendly and easy to work with and provides an applicable resource for analyzing real-time PCR data.
	"""
	
	cran = "rtpcr" 

	version("1.0.0", md5="c0df6a500c9d13326ce8ec26942024ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
