# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZenplots(RPackage):
	"""Zigzag Expanded Navigation Plots

	Graphical tools for visualizing high-dimensional data along a path
 of alternating one- and two-dimensional plots. Note that this
 includes interactive graphics plots based on 'loon' in turn based on 'tcltk'
 (included as part of the standard R distribution).  It also requires 'graph' from Bioconductor.
 For more detail on use and algorithms, see <doi:10.18637/jss.v095.i04>.
	"""
	
	homepage = "https://github.com/great-northern-diver/zenplots"
	cran = "zenplots" 

	version("1.0.6", md5="65e28bdd7b8c91c9d4323aaa07cbffd7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-pairviz", type=("build", "run"))
