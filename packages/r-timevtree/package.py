# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimevtree(RPackage):
	"""Survival Analysis of Time Varying Coefficients Using a
Tree-Based Approach

	Estimates time varying regression effects under Cox type models in
    survival data using classification and regression tree. The codes in this package were 
    originally written in S-Plus for the paper "Survival Analysis with Time-Varying Regression
    Effects Using a Tree-Based Approach," by Xu, R. and Adak, S. (2002) <doi:10.1111/j.0006-341X.2002.00305.x>, Biometrics, 58: 305-315.
    Development of this package was supported by NIH grants AG053983 and AG057707,
    and by the UCSD Altman Translational Research Institute, NIH grant UL1TR001442.
    The content is solely the responsibility of the authors and does not necessarily
    represent the official views of the NIH.
    The example data are from the Honolulu Heart Program/Honolulu Asia Aging Study (HHP/HAAS).
	"""
	
	cran = "TimeVTree" 

	version("0.3.1", md5="55d2720ea72ed45bdd532299e1def68b")

	depends_on("r-survival", type=("build", "run"))
