# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypervolume(RPackage):
	"""High Dimensional Geometry, Set Operations, Projection, and
Inference Using Kernel Density Estimation, Support Vector
Machines, and Convex Hulls

	Estimates the shape and volume of high-dimensional datasets and performs set operations: intersection / overlap, union, unique components, inclusion test, and hole detection. Uses stochastic geometry approach to high-dimensional kernel density estimation, support vector machine delineation, and convex hull generation. Applications include modeling trait and niche hypervolumes and species distribution modeling.
	"""
	
	cran = "hypervolume" 

	version("3.1.3", md5="7a1bbe095a610cd6a25d3fd557030c97")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-hitandrun", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-palmerpenguins", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
