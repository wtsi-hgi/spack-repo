# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnomasticdiversity(RPackage):
	"""Onomastic Diversity Measures

	Different measures which can be used to quantify similarities between regions. These measures are isonymy, isonymy between, Lasker distance, coefficients of Hedrick and Nei. In addition, it calculates biodiversity indices such as Margalef, Menhinick, Simpson, Shannon, Shannon-Wiener, Sheldon, Heip, Hill Numbers, Geometric Mean and Cressie and Read statistics.
	"""
	
	cran = "OnomasticDiversity" 

	version("0.1", md5="6d4f2a0ec1495590248ce62ea55f7b15")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
