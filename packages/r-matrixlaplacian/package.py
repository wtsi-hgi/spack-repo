# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixlaplacian(RPackage):
	"""Normalized Laplacian Matrix and Laplacian Map

	Constructs the normalized Laplacian matrix of a square matrix, returns the eigenvectors (singular vectors) and visualization of normalized Laplacian map.
	"""
	
	cran = "matrixLaplacian" 

	version("1.0", md5="afe0ae5b28d9dbaf891d62025889958b")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
