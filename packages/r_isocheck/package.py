# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocheck(RPackage):
	"""Isomorphism Check for Multi-Stage Factorial Designs with
Randomization Restrictions

	Contains functions to check the isomorphism of multi-stage factorial designs with randomisation restrictions based on balanced spreads and balanced covering stars of PG(n-1,2) as described in Spencer, Ranjan and Mendivil (2019) <doi:10.1007/s42519-019-0064-5>.
	"""
	
	cran = "IsoCheck" 

	version("0.1.0", md5="8e17135521721ba30366b1ef278d774f")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
