# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpweight(RPackage):
	"""Optimal p-value weighting with independent information

	This package perform weighted-pvalue based multiple hypothesis test and provides corresponding information such as ranking probability, weight, significant tests, etc . To conduct this testing procedure, the testing method apply a probabilistic relationship between the test rank and the corresponding test effect size.
	"""
	
	homepage = "https://github.com/mshasan/OPWeight"
	bioc = "OPWeight" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/OPWeight_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/OPWeight/OPWeight_1.24.0.tar.gz"]

	version("1.24.0", md5="83d9a0007e617f317f9424a4c228c50a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
