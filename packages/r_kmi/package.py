# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmi(RPackage):
	"""Kaplan-Meier Multiple Imputation for the Analysis of Cumulative
Incidence Functions in the Competing Risks Setting

	Performs a Kaplan-Meier multiple imputation to recover the missing potential censoring information from competing risks events, so that standard right-censored methods could be applied to the imputed data sets to perform analyses of the cumulative incidence functions (Allignol and Beyersmann, 2010 <doi:10.1093/biostatistics/kxq018>).
	"""
	
	homepage = "https://github.com/aallignol/kmi"
	cran = "kmi" 

	version("0.5.5", md5="635c44bb6f2d03b3d21be52055407847")

	depends_on("r-mitools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
