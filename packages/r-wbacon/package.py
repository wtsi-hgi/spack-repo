# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWbacon(RPackage):
	"""Weighted BACON Algorithms

	The BACON algorithms are methods for multivariate outlier
    nomination (detection) and robust linear regression by Billor, Hadi,
    and Velleman (2000) <doi:10.1016/S0167-9473(99)00101-2>. The extension
    to weighted problems is due to Beguin and Hulliger (2008)
    <https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X200800110616>; see
    also <doi:10.21105/joss.03238>.
	"""
	
	homepage = "https://github.com/tobiasschoch/wbacon"
	cran = "wbacon" 

	version("0.6-1", md5="f576373ed7b19f4a7053253ed8729318")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
