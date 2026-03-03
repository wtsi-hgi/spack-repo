# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIarm(RPackage):
	"""Item Analysis in Rasch Models

	Tools to assess model fit and identify misfitting items for Rasch models (RM) and partial credit models (PCM). Included are item fit statistics, item characteristic curves, item-restscore association, conditional likelihood ratio tests, assessment of measurement error, estimates of the reliability and test targeting as described in Christensen et al. (Eds.) (2013, ISBN:978-1-84821-222-0).
	"""
	
	cran = "iarm" 

	version("0.4.3", md5="cce07e7b42f6641c40787a488bcf26fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-erm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-vcdextra", type=("build", "run"))
