# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbdesign(RPackage):
	"""Design and Monitoring of Clinical Trials with Negative Binomial
Endpoint

	Calculate various functions needed for design and monitoring clinical trials with negative binomial endpoint
    with variable follow-up. This version has a few changes compared to the previous version 1.0.0, including 
    (1) correct a typo in Type 1 censoring, mtbnull=bnull and (2) restructure the code to account for shape parameter equal to zero, i.e. Poisson scenario. 
	"""
	
	cran = "NBDesign" 

	version("2.0.0", md5="0b7f261b98f8c7e2d0591e85de1552b2")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-pweall", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
