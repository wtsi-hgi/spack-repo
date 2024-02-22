# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssignr(RPackage):
	"""Infer Geographic Origin from Isotopic Data

	Routines for re-scaling isotope maps using known-origin tissue isotope data, assigning origin of unknown samples, and summarizing and assessing assignment results. Methods are adapted from Wunder (2010, in ISBN:9789048133536) and Vander Zanden, H. B. et al. (2014) <doi:10.1111/2041-210X.12229> as described in Ma, C. et al. (2020) <doi:10.1111/2041-210X.13426>.
	"""
	
	cran = "assignR" 

	version("2.4.0", md5="2ac3526084e31ac3979d364699999aac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-terra@1.7.23:", type=("build", "run"))
