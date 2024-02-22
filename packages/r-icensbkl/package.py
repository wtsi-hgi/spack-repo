# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcensbkl(RPackage):
	"""Accompanion to the Book on Interval Censoring by Bogaerts,
Komarek, and Lesaffre

	Contains datasets and several smaller functions suitable for analysis of interval-censored data. The package complements the book Bogaerts, Komárek and Lesaffre (2017, ISBN: 978-1-4200-7747-6) "Survival Analysis with Interval-Censored Data: A Practical Approach" <https://www.routledge.com/Survival-Analysis-with-Interval-Censored-Data-A-Practical-Approach-with/Bogaerts-Komarek-Lesaffre/p/book/9781420077476>. Full R code related to the examples presented in the book can be found at <https://ibiostat.be/online-resources/icbook/supplemental>. Packages mentioned in the "Suggests" section are used in those examples.
	"""
	
	homepage = "https://ibiostat.be/online-resources/icbook/supplemental/"
	cran = "icensBKL" 

	version("1.5", md5="6975c25eaa4ef7ebe66d47a8a19d70d4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-icens", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-smoothsurv", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
