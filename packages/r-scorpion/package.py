# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScorpion(RPackage):
	"""Single Cell Oriented Reconstruction of PANDA Individual
Optimized Networks

	Constructs gene regulatory networks from single-cell gene expression data using the PANDA (Passing Attributes between Networks for Data Assimilation) algorithm.
	"""
	
	cran = "SCORPION" 

	version("1.0.1", md5="b59bda852682d9dfe238c0c6bb6452cb")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
