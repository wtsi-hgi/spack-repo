# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPosratiodist(RPackage):
	"""Quotient of Random Variables Conditioned to the Positive
Quadrant

	Computes the exact probability density function of X/Y conditioned on positive quadrant for series of  bivariate distributions,for more details see Nadarajah,Song and Si (2019) <DOI:10.1080/03610926.2019.1576893>. 
	"""
	
	cran = "PosRatioDist" 

	version("1.2.1", md5="38f12fb0772b69885ac4fdfd9ca6e4af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
