# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReda(RPackage):
	"""Recurrent Event Data Analysis

	Contains implementations of recurrent event data analysis routines
    including (1) survival and recurrent event data simulation from
    stochastic process point of view by the thinning method
    proposed by Lewis and Shedler (1979) <doi:10.1002/nav.3800260304>
    and the inversion method introduced in Cinlar (1975, ISBN:978-0486497976),
    (2) the mean cumulative function (MCF) estimation by the
    Nelson-Aalen estimator of the cumulative hazard rate function,
    (3) two-sample recurrent event responses comparison with the pseudo-score
    tests proposed by Lawless and Nadeau (1995) <doi:10.2307/1269617>,
    (4) gamma frailty model with spline rate function following
    Fu, et al. (2016) <doi:10.1080/10543406.2014.992524>.
	"""
	
	homepage = "https://wwenjie.org/reda"
	cran = "reda" 

	version("0.5.4", md5="14a5641aecada80ed0b7926402f492fd")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-splines2@0.4.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
