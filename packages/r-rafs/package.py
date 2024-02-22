# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRafs(RPackage):
	"""Robust Aggregative Feature Selection

	A cross-validated minimal-optimal feature selection algorithm.
 It utilises popularity counting, hierarchical clustering with feature dissimilarity measures,
 and prefiltering with all-relevant feature selection method to obtain the minimal-optimal set of features.
	"""
	
	homepage = "https://www.mdfs.it/"
	cran = "RAFS" 

	version("0.2.3", md5="71f83cc20c8feb5cff3deae8a3b540f9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-mdfs@1.5.3:", type=("build", "run"))
	depends_on("r-splittools", type=("build", "run"))
