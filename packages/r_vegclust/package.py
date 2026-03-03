# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegclust(RPackage):
	"""Fuzzy Clustering of Vegetation Data

	A set of functions to: (1) perform fuzzy clustering of vegetation data (De Caceres et al, 2010) <doi:10.1111/j.1654-1103.2010.01211.x>; (2) to assess ecological community similarity on the basis of structure and composition (De Caceres et al, 2013) <doi:10.1111/2041-210X.12116>.
	"""
	
	homepage = "https://emf-creaf.github.io/vegclust/"
	cran = "vegclust" 

	version("2.0.2", md5="8be1c3e8d7fe5e43b628d4af18441847")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
