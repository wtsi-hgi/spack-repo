# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFclust(RPackage):
	"""Fuzzy Clustering

	Algorithms for fuzzy clustering, cluster validity indices and plots for cluster validity and visualizing fuzzy clustering results.
	"""
	
	cran = "fclust" 

	version("2.1.1.1", md5="abb86acb585a9c8f5f083d37da674204")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7:", type=("build", "run"))
