# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMortcast(RPackage):
	"""Estimation and Projection of Age-Specific Mortality Rates

	Age-specific mortality rates are estimated and projected using 
    the Kannisto, Lee-Carter and related methods as described in 
    Sevcikova et al. (2016) <doi:10.1007/978-3-319-26603-9_15>.
	"""
	
	cran = "MortCast" 

	version("2.7-0", md5="b3ef522f4a8c4a2536b0dbff1b5f064a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wpp2017", type=("build", "run"))
