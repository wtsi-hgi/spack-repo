# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmonad(RPackage):
	"""A Monadic Pipeline System

	
    A monadic solution to pipeline analysis. All operations -- and the errors,
    warnings and messages they emit -- are merged into a directed graph. Infix
    binary operators mediate when values are stored, how exceptions are
    handled, and where pipelines branch and merge. The resulting structure may
    be queried for debugging or report generation. 'rmonad' complements, rather
    than competes with, non-monadic pipeline packages like 'magrittr' or
    'pipeR'. This work is funded by the NSF (award number 1546858).
	"""
	
	homepage = "https://github.com/arendsee/rmonad"
	cran = "rmonad" 

	version("0.7.0", md5="86e05a5a17844d3422a622052de0c7c6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
