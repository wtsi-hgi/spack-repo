# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REulerian(RPackage):
	"""eulerian: A package to find eulerian paths from graphs

	An eulerian path is a path in a graph which visits every edge exactly once. This package provides methods to handle eulerian paths or cycles.
	"""
	
	cran = "eulerian" 

	version("1.0", md5="43cdf38326f1dec79d8cea67a221379f")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
