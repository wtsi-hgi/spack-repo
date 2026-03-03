# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartsizer(RPackage):
	"""Power Analysis for a SMART Design

	A set of tools for determining the necessary sample size
    in order to identify the optimal dynamic treatment regime
    in a sequential, multiple assignment, randomized trial (SMART). 
    Utilizes multiple comparisons with the best methodology 
    to adjust for multiple comparisons.
    Designed for an arbitrary SMART design. Please see Artman (2018) <doi:10.1093/biostatistics/kxy064> for more details.
	"""
	
	cran = "smartsizer" 

	version("1.0.3", md5="9ea522057918be731d13c3c3a86f5f73")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
