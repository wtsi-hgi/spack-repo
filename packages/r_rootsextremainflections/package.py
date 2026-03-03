# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRootsextremainflections(RPackage):
	"""Finds Roots, Extrema and Inflection Points of a Curve

	Implementation of Taylor Regression Estimator (TRE), 
   Tulip Extreme Finding Estimator (TEFE), Bell Extreme Finding Estimator (BEFE),
   Integration Extreme Finding Estimator (IEFE) and 
   Integration Root Finding Estimator (IRFE) for roots, extrema and inflections of a curve .     
   Christopoulos, DT (2019) <doi:10.13140/RG.2.2.17158.32324> .
   Christopoulos, DT (2016) <doi:10.2139/ssrn.3043076> .
   Christopoulos, DT (2016) <https://veltech.edu.in/wp-content/uploads/2016/04/Paper-04-2016.pdf> .
   Christopoulos, DT (2014) <arXiv:1206.5478v2 [math.NA]> .
	"""
	
	cran = "RootsExtremaInflections" 

	version("1.2.1", md5="d209b473de771efa3ee38a581642c07c")

	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-inflection", type=("build", "run"))
