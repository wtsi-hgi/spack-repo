# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdclassif(RPackage):
	"""High Dimensional Supervised Classification and Clustering

	Discriminant analysis and data clustering methods for high
    dimensional data, based on the assumption that high-dimensional data live in
    different subspaces with low dimensionality proposing a new parametrization of
    the Gaussian mixture model which combines the ideas of dimension reduction and
    constraints on the model.
	"""
	
	cran = "HDclassif" 

	version("2.2.1", md5="d05c3b4f53259fc684bb18e1f8d6c424")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
