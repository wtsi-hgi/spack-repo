# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopklists(RPackage):
	"""Inference, Aggregation and Visualization for Top-K Ranked Lists

	For multiple ranked input lists (full or partial) representing the same set of N objects, the package 'TopKLists' <doi:10.1515/sagmb-2014-0093> offers (1) statistical inference on the lengths of informative top-k lists, (2) stochastic aggregation of full or partial lists, and (3) graphical tools for the statistical exploration of input lists, and for the visualization of aggregation results. Note that RGtk2 and gWidgets2RGtk2 have been archived on CRAN. See <https://github.com/pievos101/TopKLists> for installation instructions.
	"""
	
	homepage = "http://topklists.r-forge.r-project.org"
	cran = "TopKLists" 

	version("1.0.8", md5="350da66b9e4a5ea3abee57194c5ff3ae")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
