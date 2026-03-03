# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperoverlap(RPackage):
	"""Overlap Detection in n-Dimensional Space

	Uses support vector machines to identify a perfectly separating hyperplane (linear or curvilinear) between two entities in high-dimensional space. If this plane exists, the entities do not overlap. Applications include overlap detection in morphological, resource or environmental dimensions. More details can be found in: Brown et al. (2020) <doi:10.1111/2041-210X.13363> .
	"""
	
	cran = "hyperoverlap" 

	version("1.1.1", md5="e9b96ce243dd9c7aa4ede4772d277e8e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-matlib", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
