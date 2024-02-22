# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCxhull(RPackage):
	"""Convex Hull

	Computes the convex hull in arbitrary dimension, based on the
    Qhull library (<http://www.qhull.org>). The package provides a
    complete description of the convex hull: edges, ridges, facets,
    adjacencies. Triangulation is optional.
	"""
	
	homepage = "https://github.com/stla/cxhull"
	cran = "cxhull" 

	version("0.7.4", md5="130459a673637a7f1bb4b848f0035bc9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
