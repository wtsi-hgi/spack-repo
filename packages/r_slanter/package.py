# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlanter(RPackage):
	"""Slanted Matrices and Ordered Clustering

	Slanted matrices and ordered clustering for better visualization of similarity data.
	"""
	
	cran = "slanter" 

	version("0.2-0", md5="44dc0debee31c3a828dff5788abff294")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
