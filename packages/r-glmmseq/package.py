# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmseq(RPackage):
	"""General Linear Mixed Models for Gene-Level Differential
Expression

	Using mixed effects models to analyse longitudinal gene expression can highlight differences between sample groups over time. The most widely used differential gene expression tools are unable to fit linear mixed effect models, and are less optimal for analysing longitudinal data. This package provides negative binomial and Gaussian mixed effects models to fit gene expression and other biological data across repeated samples. This is particularly useful for investigating changes in RNA-Sequencing gene expression between groups of individuals over time, as described in: Rivellese, F., Surace, A. E., Goldmann, K., Sciacca, E., Cubuk, C., Giorli, G., ... Lewis, M. J., & Pitzalis, C. (2022) Nature medicine <doi:10.1038/s41591-022-01789-0>.
	"""
	
	homepage = "https://myles-lewis.github.io/glmmSeq/"
	cran = "glmmSeq" 

	version("0.5.5", md5="1546cd7070ab2b4a2089a5477a7dde58")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
