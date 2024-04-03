# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThresholdrocsurvival(RPackage):
	"""Diagnostic Ability Assessment with Right-Censored Data at a
Fixed Time t

	We focus on the diagnostic ability assessment of medical tests when the outcome of interest is the status (alive or dead) of the subjects at a certain time-point t. This binary status is determined by right-censored times to event and it is unknown for those subjects censored before t. Here we provide three methods (unknown status exclusion, imputation of censored times and using time-dependent ROC curves) to evaluate the diagnostic ability of binary and continuous tests in this context. Two references for the methods used here are Skaltsa et al. (2010) <doi:10.1002/bimj.200900294> and Heagerty et al. (2000) <doi:10.1111/j.0006-341x.2000.00337.x>.
	"""
	
	cran = "ThresholdROCsurvival" 

	version("1.2.1", md5="9588522a59e4fae2c35bc65aebeaf1fc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-informativecensoring", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-thresholdroc", type=("build", "run"))
