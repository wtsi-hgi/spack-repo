# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromotionimpact(RPackage):
	"""Analysis & Measurement of Promotion Effectiveness

	Analysis and measurement of promotion effectiveness on a given target variable (e.g. daily sales). After converting promotion schedule into dummy or smoothed predictor variables, the package estimates the effects of these variables controlled for trend/periodicity/structural change using prophet by Taylor and Letham (2017) <doi:10.7287/peerj.preprints.3190v2> and some prespecified variables (e.g. start of a month).
	"""
	
	homepage = "https://github.com/ncsoft/promotionImpact"
	cran = "promotionImpact" 

	version("0.1.5", md5="bcc9899c24c2f1791770c72cc888825b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.17:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-kernsmooth@2.23.15:", type=("build", "run"))
	depends_on("r-ggpubr@0.1.8:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-strucchange@1.5.1:", type=("build", "run"))
	depends_on("r-lmtest@0.9:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-prophet@0.6.1:", type=("build", "run"))
