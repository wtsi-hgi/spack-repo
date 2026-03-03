# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyclertools(RPackage):
	"""Tools for Cycling Data Analysis

	A suite of functions for analysing cycling data.
	"""
	
	homepage = "https://github.com/jmackie4/cycleRtools"
	cran = "cycleRtools" 

	version("1.1.1", md5="69584db87c2a776ac0e762db0cf41e38")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))
