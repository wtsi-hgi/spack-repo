# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaforest(RPackage):
	"""Exploring Heterogeneity in Meta-Analysis using Random Forests

	Conduct random forests-based meta-analysis, obtain partial dependence plots for metaforest and classic meta-analyses, and cross-validate and tune metaforest- and classic meta-analyses in conjunction with the caret package. A requirement of classic meta-analysis is that the studies being aggregated are conceptually similar, and ideally, close replications. However, in many fields, there is substantial heterogeneity between studies on the same topic. Classic meta-analysis lacks the power to assess more than a handful of univariate moderators. MetaForest, by contrast, has substantial power to explore heterogeneity in meta-analysis. It can identify important moderators from a larger set of potential candidates (Van Lissa, 2020). This is an appealing quality, because many meta-analyses have small sample sizes. Moreover, MetaForest yields a measure of variable importance which can be used to identify important moderators, and offers partial prediction plots to explore the shape of the marginal relationship between moderators and effect size.
	"""
	
	cran = "metaforest" 

	version("0.1.4", md5="19cb3b4cad15d2ca828ded2a0b78e264")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
