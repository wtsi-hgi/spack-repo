# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScma(RPackage):
	"""Single-Case Meta-Analysis

	Perform meta-analysis of single-case experiments, including calculating various effect size measures (SMD, PND, PEM and NAP) and probability combining (additive and multiplicative method), as discussed in Bulte and Onghena (2013) <doi:10.22237/jmasm/1383280020>.
	"""
	
	cran = "SCMA" 

	version("1.3.1", md5="c2793f5a158a134af8ce33d0710292e6")

	depends_on("r@2.11.1:", type=("build", "run"))
