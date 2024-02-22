# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerbydesign(RPackage):
	"""Power Estimates for ANOVA Designs

	Functions for bootstrapping the power of ANOVA designs
    based on estimated means and standard deviations of the conditions.
    Please refer to the documentation of the boot.power.anova() function
    for further details.
	"""
	
	cran = "powerbydesign" 

	version("1.0.5", md5="07ca59da9467c8c3db46acde957c40ab")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
