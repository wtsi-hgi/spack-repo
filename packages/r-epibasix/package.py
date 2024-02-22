# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpibasix(RPackage):
	"""Elementary Epidemiological Functions for Epidemiology and
Biostatistics

	Contains elementary tools for analysis of
        common epidemiological problems, ranging from sample size
        estimation, through 2x2 contingency table analysis and basic
        measures of agreement (kappa, sensitivity/specificity).
        Appropriate print and summary statements are also written to
        facilitate interpretation wherever possible.  Source code is 	commented throughout to facilitate modification.  The target audience includes advanced undergraduate and graduate students
        in epidemiology or biostatistics courses, and clinical researchers.
	"""
	
	cran = "epibasix" 

	version("1.5", md5="b3de9355329a32dc7fe3a0db21677e2f")

	depends_on("r@2.1:", type=("build", "run"))
