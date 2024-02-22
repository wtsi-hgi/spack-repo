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

	version("0.2.16", md5="1b9b2157b7c66aa59b266dfe5ec5a949")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
