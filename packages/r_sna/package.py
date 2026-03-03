# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSna(RPackage):
	"""Tools for Social Network Analysis

	A range of tools for social network analysis, including node and graph-level indices, structural distance and covariance methods, structural equivalence detection, network regression, random graph generation, and 2D/3D network visualization.
	"""
	
	homepage = "https://statnet.org"
	cran = "sna" 

	version("2.7-2", md5="c4eb81ede668f0f8214afffba144d6cf")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
