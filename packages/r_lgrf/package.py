# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgrf(RPackage):
	"""Set-Based Tests for Genetic Association in Longitudinal Studies

	Functions for the longitudinal genetic random field method (He et al., 2015, <doi:10.1111/biom.12310>) to test the association between a longitudinally measured quantitative outcome and a set of genetic variants in a gene/region.
	"""
	
	cran = "LGRF" 

	version("1.0", md5="8ad433fd256d0df1a864fb490b163a0b")

	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
