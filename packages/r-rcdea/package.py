# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcdea(RPackage):
	"""Robust and Conditional Data Envelopment Analysis (DEA)

	With this package we provide an easy method to compute robust and conditional Data Envelopment Analysis (DEA), 
             Free Disposal Hull (FDH) and Benefit of the Doubt (BOD) scores. 
             The robust approach is based on the work of Cazals, Florens and Simar (2002) <doi:10.1016/S0304-4076(01)00080-X>. 
             The conditional approach is based on Daraio and Simar (2007) <doi:10.1007/s11123-007-0049-3>.
             Besides we provide graphs to help with the choice of m. 
             We relay on the 'Benchmarking' package to compute the efficiency scores and on the 'np' package to compute non parametric estimation of similarity among units.
	"""
	
	cran = "rcDEA" 

	version("1.0", md5="6917cf8e58417720b6bb1adda36ebccf")

	depends_on("r-np", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
