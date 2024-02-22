# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTesttwice(RPackage):
	"""Testing One Hypothesis Twice in Observational Studies

	Tests one hypothesis with several test statistics, correcting for multiple testing.  The central function in the package is testtwice().  In a sensitivity analysis, the method has the largest design sensitivity of its component tests.  The package implements the method and examples in Rosenbaum, P. R. (2012) <doi:10.1093/biomet/ass032> Testing one hypothesis twice in observational studies. Biometrika, 99(4), 763-774.  
	"""
	
	cran = "testtwice" 

	version("1.0.3", md5="99e23525c579fc046d39c7a03113ab34")

	depends_on("r-mvtnorm", type=("build", "run"))
