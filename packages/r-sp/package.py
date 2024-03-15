# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSp(RPackage):
	"""Classes and Methods for Spatial Data.

	Classes and methods for spatial data; the classes document where the
	spatial location information resides, for 2D or 3D data. Utility functions
	are provided, e.g. for plotting data as maps, spatial selection, as well as
	methods for retrieving coordinates, for subsetting, print, summary, etc."""

	cran = "sp"

	license("GPL-2.0-or-later")

	version("2.1-3", md5="abcf7395f983cc55056f4b86b906b4bb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
