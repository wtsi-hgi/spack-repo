# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustgeo(RPackage):
	"""Hierarchical Clustering with Spatial Constraints

	Implements a Ward-like hierarchical clustering
    algorithm including soft spatial/geographical constraints.
	"""
	
	cran = "ClustGeo" 

	version("2.1", md5="a9901f9913acf0d1c8f577abb59907d7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
