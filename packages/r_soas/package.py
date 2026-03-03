# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoas(RPackage):
	"""Creation of Stratum Orthogonal Arrays

	Creates stratum orthogonal arrays (also known as strong orthogonal arrays). These are arrays with more levels per column than the typical orthogonal array, and whose low order projections behave like orthogonal arrays, when collapsing levels to coarser strata. Details are described in Groemping (2022) "A unifying implementation of stratum (aka strong) orthogonal arrays" <http://www1.bht-berlin.de/FB_II/reports/Report-2022-002.pdf>.
	"""
	
	homepage = "https://github.com/bertcarnell/SOAs"
	cran = "SOAs" 

	version("1.4", md5="cc6159159ad1e553884c8b7e278d8c68")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-doe-base@1.2:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-frf2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lhs@1.1.3:", type=("build", "run"))
	depends_on("r-conf-design", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
