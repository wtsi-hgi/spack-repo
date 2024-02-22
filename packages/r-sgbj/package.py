# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgbj(RPackage):
	"""Survival Extension of the Generalized Berk-Jones Test

	Implements an extension of the Generalized Berk-Jones (GBJ) statistic for
    survival data, sGBJ. It computes the sGBJ statistic and its p-value for testing 
    the association between a gene set and a time-to-event outcome with possible 
    adjustment on additional covariates. Detailed method is available at Villain L, Ferte T, 
    Thiebaut R and Hejblum BP (2021) <doi:10.1101/2021.09.07.459329>.
	"""
	
	homepage = "https://github.com/lauravillain/sGBJ"
	cran = "sGBJ" 

	version("0.1.0", md5="ec05340243cab17883de3526da42d3f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gbj", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
