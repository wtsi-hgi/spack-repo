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

    version("3.4.0", tag="RELEASE_3_21")
	version("2.6.1", sha256="e76f580867e8bedd189d4a06cca48c61f023615863e4f59c6227d2a01f27a8df")
	version("2.6.0", md5="033b5763d95dc222256a4ef85b7e3a99")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("openjdk@11:", type=("build", "link", "run"))
