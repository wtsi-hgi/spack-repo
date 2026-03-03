# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLudic(RPackage):
	"""Linkage Using Diagnosis Codes

	Probabilistic record linkage without direct identifiers using only 
    diagnosis codes. Method is detailed in: Hejblum, Weber, Liao, Palmer, 
    Churchill, Szolovits, Murphy, Kohane & Cai (2019) <doi: 10.1038/sdata.2018.298> ;
    Zhang, Hejblum, Weber, Palmer, Churchill, Szolovits, Murphy, Liao, Kohane 
    & Cai (2021) <doi: 10.1101/2021.05.02.21256490>.
	"""
	
	cran = "ludic" 

	version("0.2.0", md5="db36f2b26263387f9b7226cdc42102e7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-landpred", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
