# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGclus(RPackage):
	"""Clustering Graphics

	Orders panels in scatterplot matrices and parallel coordinate
 displays by some merit index. Package contains various indices of merit,
 ordering functions, and enhanced versions of pairs and parcoord which
 color panels according to their merit level.
	"""
	
	cran = "gclus" 

	version("1.3.2", md5="3ff6434ccb88afcfc6628374a21e7338")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
