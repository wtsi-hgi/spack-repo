# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdist(RPackage):
	"""Calculate Pairwise Distances

	A common framework for calculating distance matrices.
	"""
	
	homepage = "https://github.com/blasern/rdist"
	cran = "rdist" 

	version("0.0.5", md5="394847a1782d753eaa4fd196ba2b569e")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
