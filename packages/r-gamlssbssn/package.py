# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssbssn(RPackage):
	"""Bimodal Skew Symmetric Normal Distribution

	Density, distribution function, quantile function and random generation for the bimodal skew symmetric normal distribution of Hassan and El-Bassiouni (2016) <doi:10.1080/03610926.2014.882950>.
	"""
	
	cran = "gamlssbssn" 

	version("0.1.0", md5="5117d29a8796a12e245e5c1bf6ac7ed1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gamlss-dist@4.3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
