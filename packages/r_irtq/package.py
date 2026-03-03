# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtq(RPackage):
	"""Unidimensional Item Response Theory Modeling

	Fit unidimensional item response theory (IRT) models to a mixture 
    of dichotomous and polytomous data, calibrate online item parameters 
    (i.e., pretest and operational items), estimate examinees' abilities, 
    and examine the IRT model-data fit on item-level in different ways 
    as well as provide useful functions related to IRT analyses such as 
    IRT model-data fit evaluation and differential item functioning analysis.
    The bring.flexmirt() and write.flexmirt() functions were written by modifying 
    the read.flexmirt() function (Pritikin & Falk (2022) <doi:10.1177/0146621620929431>).
    The bring.bilog() and bring.parscale() functions were written by modifying the read.bilog() 
    and read.parscale() functions, respectively (Weeks (2010) <doi:10.18637/jss.v035.i12>).
    The bisection() function was written by modifying the bisection() function 
    (Howard (2017, ISBN:9780367657918)). The code of the inverse test characteristic curve 
    scoring in the est_score() function was written by modifying the irt.eq.tse() function 
    (González (2014) <doi:10.18637/jss.v059.i07>). In est_score() function, the code of weighted 
    likelihood estimation method was written by referring to the Pi(), Ji(), and Ii() functions
    of the catR package (Magis & Barrada (2017) <doi:10.18637/jss.v076.c01>).
	"""
	
	cran = "irtQ" 

	version("0.2.0", md5="8dee4d07251c6308deefd66c0d8391d4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
