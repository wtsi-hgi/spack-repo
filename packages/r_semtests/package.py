# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemtests(RPackage):
	"""Goodness-of-Fit Testing for Structural Equation Models

	Supports eigenvalue block-averaging p-values (Foldnes, Grønneberg, 2018) <doi:10.1080/10705511.2017.1373021>,
    penalized eigenvalue block-averaging p-values (Foldnes, Moss, Grønneberg, WIP), penalized
    regression p-values (Foldnes, Moss, Grønneberg, WIP), as well as traditional p-values such as Satorra-Bentler. All p-values can
    be calculated using unbiased or biased gamma estimates (Du, Bentler, 2022) <doi:10.1080/10705511.2022.2063870> 
    and two choices of chi square statistics.
	"""
	
	cran = "semTests" 

	version("0.5.0", md5="956bd154804ba4e9eeaa9fa7bfd11a4b")

	depends_on("r-lavaan@0.6.16:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
