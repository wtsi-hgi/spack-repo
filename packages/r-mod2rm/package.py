# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMod2rm(RPackage):
	"""Moderation Analysis for Two-Instance Repeated Measures Designs

	Multiple moderation analysis for two-instance repeated measures designs, with up to three simultaneous moderators (dichotomous and/or continuous) with additive or multiplicative relationship. Includes analyses of simple slopes and conditional effects at (automatically determined or manually set) values of the moderator(s), as well as an implementation of the Johnson-Neyman procedure for determining regions of significance in single moderator models. Based on Montoya, A. K. (2018) "Moderation analysis in two-instance repeated measures designs: Probing methods and multiple moderator models" <doi:10.3758/s13428-018-1088-6> .
	"""
	
	cran = "mod2rm" 

	version("0.2.1", md5="9c5320fd12286f0af107bc8b92c41fad")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
