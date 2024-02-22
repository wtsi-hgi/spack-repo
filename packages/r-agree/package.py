# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgree(RPackage):
	"""Various Methods for Measuring Agreement

	Bland-Altman plot and scatter plot with identity line 
             for visualization and point and 
             interval estimates for different metrics related to 
             reproducibility/repeatability/agreement including
             the concordance correlation coefficient, 
             intraclass correlation coefficient,
             within-subject coefficient of variation,
             smallest detectable difference, 
             and mean normalized smallest detectable difference.
	"""
	
	cran = "agRee" 

	version("0.5-3", md5="9cc8df0cbc20daa8213cf53c0cc231a6")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-miscf@0.1.4:", type=("build", "run"))
	depends_on("r-lme4@1.0.4:", type=("build", "run"))
	depends_on("r-r2jags@0.3.11:", type=("build", "run"))
	depends_on("r-coda@0.16.1:", type=("build", "run"))
