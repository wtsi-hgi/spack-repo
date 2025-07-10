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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OPWeight_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OPWeight/OPWeight_1.24.0.tar.gz"]

	version("1.24.0", sha256="9aad60d90c305d7458575420478f55ee08564df2398e3d02ec200538348f90bd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
