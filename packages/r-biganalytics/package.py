# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiganalytics(RPackage):
	"""Utilities for 'big.matrix' Objects from Package 'bigmemory'

	Extend the 'bigmemory' package with various analytics.
    Functions 'bigkmeans' and 'binit' may also be used with native R objects.
    For 'tapply'-like functions, the bigtabulate package may also be helpful.
    For linear algebra support, see 'bigalgebra'.  For mutex (locking) support
    for advanced shared-memory usage, see 'synchronicity'.
	"""
	
	homepage = "http://www.bigmemory.org"
	cran = "biganalytics" 

	version("1.1.21", md5="85078759889b06ac5a408175d5297560")
	version("1.1.22", md5="a6dadd3f2c7b62fd90ac527cbfa1fe02")

	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-biglm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
