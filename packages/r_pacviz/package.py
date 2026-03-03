# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPacviz(RPackage):
	"""Pac-Man Visualization Package

	Provides a broad-view perspective on data via
    linear mapping of data onto a radial coordinate system. The package
    contains functions to visualize the residual values of linear
    regression and Cartesian data in the defined radial scheme. See the
    'pacviz' documentation page for more information:
    <https://pacviz.sriley.dev/>.
	"""
	
	cran = "pacviz" 

	version("1.0.3", md5="e238194702dbed7c3c1b020a5fb50014")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
