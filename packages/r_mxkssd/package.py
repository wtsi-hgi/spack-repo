# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMxkssd(RPackage):
	"""Efficient Mixed-Level k-Circulant Supersaturated Designs

	Generates efficient balanced mixed-level k-circulant supersaturated designs by interchanging the elements of the generator vector. Attempts to generate a supersaturated design that has EfNOD efficiency more than user specified efficiency level (mef). Displays the progress of generation of an efficient mixed-level k-circulant design through a progress bar. The progress of 100 per cent means that one full round of interchange is completed. More than one full round (typically 4-5 rounds) of interchange may be required for larger designs. For more details, please see Mandal, B.N., Gupta V. K. and Parsad, R. (2011). Construction of Efficient Mixed-Level k-Circulant Supersaturated Designs, Journal of Statistical Theory and Practice, 5:4, 627-648, <doi:10.1080/15598608.2011.10483735>.
	"""
	
	cran = "mxkssd" 

	version("1.2", md5="4340bff889228dd9175dbf3070b4cc41")

	depends_on("r@2.13:", type=("build", "run"))
