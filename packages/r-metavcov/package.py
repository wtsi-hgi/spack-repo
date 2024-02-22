# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetavcov(RPackage):
	"""Computing Variances and Covariances, Visualization and Missing
Data Solution for Multivariate Meta-Analysis

	Collection of functions to compute within-study covariances for different effect sizes, data visualization, and single and multiple imputations for missing data. Effect sizes include correlation (r), mean difference (MD), standardized mean difference (SMD), log odds ratio (logOR), log risk ratio (logRR), and risk difference (RD).
	"""
	
	homepage = "https://github.com/luminwin/metavcov"
	cran = "metavcov" 

	version("2.1.5", md5="87d60cc2111ce7f6b5f6401ed57c5e49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
