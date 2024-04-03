# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinicran(RPackage):
	"""Create a Mini Version of CRAN Containing Only Selected Packages

	Makes it possible to create an internally consistent
    repository consisting of selected packages from CRAN-like repositories.
    The user specifies a set of desired packages, and 'miniCRAN' recursively
    reads the dependency tree for these packages, then downloads only this
    subset. The user can then install packages from this repository directly,
    rather than from CRAN.  This is useful in production settings, e.g. server
    behind a firewall, or remote locations with slow (or zero) Internet access.
	"""
	
	homepage = "https://github.com/andrie/miniCRAN"
	cran = "miniCRAN" 

	version("0.3.0", md5="bd43289898fb090332ee0e899fecedcf")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
