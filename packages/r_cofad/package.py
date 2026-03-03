# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCofad(RPackage):
	"""Contrast Analyses for Factorial Designs

	Contrast analysis for factorial designs is an alternative to the classical ANOVA approach with the advantage of testing focused hypothesis. The method is mainly based on Rosenthal, Rosnow and Rubin (2000, ISBN:978-0521659802) and Sedlmeier and Renkewitz (2018, ISBN:978-3868943214). 
	"""
	
	homepage = "https://gitlab.hrz.tu-chemnitz.de/burma--tu-chemnitz.de/cofad.git"
	cran = "cofad" 

	version("0.1.1", md5="a0e39c25b38b6d5ddb8c788c3989eee0")

	depends_on("r@3.1:", type=("build", "run"))
