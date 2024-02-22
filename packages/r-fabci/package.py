# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabci(RPackage):
	"""FAB Confidence Intervals

	Frequentist assisted by Bayes (FAB) confidence interval
    construction. See 'Adaptive multigroup confidence intervals with constant
    coverage' by Yu and Hoff <DOI:10.1093/biomet/asy009> and  
    'Exact adaptive confidence intervals for linear regression coefficients'
    by Hoff and Yu <DOI:10.1214/18-EJS1517>.
	"""
	
	cran = "fabCI" 

	version("0.2", md5="41937b274277b6f0cd6191c837f0fd49")

	depends_on("r-mass", type=("build", "run"))
