# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoma(RPackage):
	"""General-Purpose Optimisation with the Self-Organising Migrating
Algorithm

	An R implementation of the Self-Organising Migrating Algorithm, a general-purpose, stochastic optimisation algorithm. The approach is similar to that of genetic algorithms, although it is based on the idea of a series of ``migrations'' by a fixed set of individuals, rather than the development of successive generations. It can be applied to any cost-minimisation problem with a bounded parameter space, and is robust to local minima.
	"""
	
	homepage = "https://github.com/jonclayden/soma/"
	cran = "soma" 

	version("1.2.0", md5="7ab2bd3bb48d063a9ad94d0faec4dab5")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-reportr@1.3:", type=("build", "run"))
