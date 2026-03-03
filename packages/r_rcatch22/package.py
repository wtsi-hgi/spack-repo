# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcatch22(RPackage):
	"""Calculation of 22 CAnonical Time-Series CHaracteristics

	Calculate 22 summary statistics coded in C on time-series vectors to enable 
    pattern detection, classification, and regression applications in the 
    feature space as proposed by Lubba et al. (2019) <doi:10.1007/s10618-019-00647-x>.
	"""
	
	cran = "Rcatch22" 

	version("0.2.1", md5="548ca2046243e4946fc12749e2bb6471", url="https://cran.r-project.org/src/contrib/Rcatch22_0.2.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
