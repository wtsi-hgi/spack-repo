# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemacor(RPackage):
	"""Random Effects Meta-Analysis for Correlated Test Statistics

	Meta-analysis is widely used to summarize estimated effects sizes across multiple statistical tests. Standard fixed and random effect meta-analysis methods assume that the estimated of the effect sizes are statistically independent.  Here we relax this assumption and enable meta-analysis when the correlation matrix between effect size estimates is known.  Fixed effect meta-analysis uses the method of Lin and Sullivan (2009) <doi:10.1016/j.ajhg.2009.11.001>, and random effects meta-analysis uses the method of Han, et al. <doi:10.1093/hmg/ddw049>.
	"""
	
	homepage = "https://diseaseneurogenomics.github.io/remaCor/"
	cran = "remaCor" 

	version("0.0.18", md5="cc6ca79d2f7319e40e2ffe27a19ff598")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
