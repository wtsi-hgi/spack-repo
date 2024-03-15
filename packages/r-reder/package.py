# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReder(RPackage):
	"""Interactive visualization and manipulation of nested networks

	RedeR is an R-based package combined with a stand-alone Java application for interactive visualization and manipulation of nested networks.
	"""
	
	homepage = "http://genomebiology.com/2012/13/4/R29"
	bioc = "RedeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RedeR_2.6.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RedeR/RedeR_2.6.1.tar.gz"]

	version("2.6.1", md5="75eeeea965803fa97dcd0ad6007539d8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("openjdk@11:", type=("build", "link", "run"))
