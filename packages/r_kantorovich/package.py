# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKantorovich(RPackage):
	"""Kantorovich Distance Between Probability Measures

	Computes the Kantorovich distance between two probability
    measures on a finite set. The Kantorovich distance is also known as
    the Monge-Kantorovich distance or the first Wasserstein distance.
	"""
	
	homepage = "https://github.com/stla/kantorovich"
	cran = "kantorovich" 

	version("3.1.0", md5="6bec922cefac868b59e0db07c019fc0d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-ompr", type=("build", "run"))
	depends_on("r-ompr-roi", type=("build", "run"))
	depends_on("r-roi-plugin-glpk", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
