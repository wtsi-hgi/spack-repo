# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpcc(RPackage):
	"""Dynamic Programming for Convex Clustering

	Use dynamic programming method to solve l1 convex clustering with identical weights.
	"""
	
	cran = "dpcc" 

	version("1.0.0", md5="e346fd1f2ac5b4a11d3acada7816e35a")

	depends_on("r-rcpp", type=("build", "run"))
