# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSldassay(RPackage):
	"""Software for Analyzing Limiting Dilution Assays

	Calculates maximum likelihood estimate, exact and asymptotic confidence intervals, and exact and asymptotic goodness of fit p-values for concentration of infectious units from serial limiting dilution assays. This package uses the likelihood equation, exact goodness of fit p-values, and exact confidence intervals described in Meyers et al. (1994) <http://jcm.asm.org/content/32/3/732.full.pdf>. This software is also implemented as a web application through the Shiny R package <https://iupm.shinyapps.io/sldassay/>.
	"""
	
	cran = "SLDAssay" 

	version("1.8", md5="0142a8d5ca323e8add8c8cb3f75431fd")

	depends_on("r@3.2.1:", type=("build", "run"))
