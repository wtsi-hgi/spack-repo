# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfnetworks(RPackage):
	"""Tidy Geospatial Networks

	Provides a tidy approach to spatial network
    analysis, in the form of classes and functions that enable a seamless
    interaction between the network analysis package 'tidygraph' and the
    spatial analysis package 'sf'.
	"""
	
	homepage = "https://luukvdmeer.github.io/sfnetworks/"
	cran = "sfnetworks" 

	version("0.6.3", md5="b7b4e38e4a1abdbbedafc2ec836fb7f2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
