# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImsig(RPackage):
	"""Immune Cell Gene Signatures for Profiling the Microenvironment
of Solid Tumours

	Estimate the relative abundance of tissue-infiltrating immune subpopulations abundances using gene expression data. 
	"""
	
	homepage = "https://github.com/ajitjohnson/imsig/"
	cran = "imsig" 

	version("1.1.3", md5="5dfaefafec663542b9b69171760fcf29")

	depends_on("r-hiclimr@1.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
	depends_on("r-igraph@1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-survival@2.4:", type=("build", "run"))
