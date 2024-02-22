# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresize(RPackage):
	"""Precision Based Sample Size Calculation

	Bland (2009) <doi:10.1136/bmj.b3985> recommended to
    base study sizes on the width of the confidence interval rather the power of 
    a statistical test. The goal of 'presize' is to provide functions for such 
    precision based sample size calculations. For a given sample size, the 
    functions will return the precision (width of the confidence interval), and 
    vice versa. 
	"""
	
	homepage = "https://github.com/CTU-Bern/presize"
	cran = "presize" 

	version("0.3.7", md5="7b5d18828173a5e6ecdacf27ef3eb710")

	depends_on("r-kappasize@1.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
