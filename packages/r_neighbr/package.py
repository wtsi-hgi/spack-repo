# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeighbr(RPackage):
	"""Classification, Regression, Clustering with K Nearest Neighbors

	Classification, regression, and clustering with k nearest neighbors
    algorithm. Implements several distance and similarity measures, covering
    continuous and logical features. Outputs ranked neighbors. Most features of
    this package are directly based on the PMML specification for KNN.
	"""
	
	cran = "neighbr" 

	version("1.0.3", md5="d273c8966da0497d1fb53c445a294bb3")

	depends_on("r@3.3:", type=("build", "run"))
