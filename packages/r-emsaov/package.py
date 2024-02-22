# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmsaov(RPackage):
	"""The Analysis of Variance with EMS

	Provides the analysis of variance table including the expected mean squares (EMS) for various types of experimental design. When some variables are random effects or we use special experimental design such as nested design, repeated-measures design, or split-plot design, it is not easy to find the appropriate test, especially denominator for F-statistic which depends on EMS. 
	"""
	
	cran = "EMSaov" 

	version("2.3", md5="bc520de577bc287ed805cfaeed71323e")

	depends_on("r-shiny", type=("build", "run"))
